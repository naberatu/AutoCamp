from encounter import Encounter
import pickle
from random import randint
from math import floor


class NCEncounter(Encounter):

    def __init__(self, max_inventory, name, is_shop=False):
        super().__init__(max_inventory)
        self.name = name
        self.is_shop = is_shop
        self.running_general = True
        self.commands = {
            "roll": "Roll di(ce)",
            "move": "Change your current location",
            "inv": "View more options regarding the party's inventory",
            "stats": "View a party member's stats",
            "rest": "Allow party members a moment of rest to recover",
            "exit": "save and quit."
        }
        self.inv_commands = {
            "use": "Use an item in this member's inventory",
            "equip": "Arrange this member's equipment",
            "dequip": "Remove this member's current equipment",
            "discard": "Discard an item from this member's inventory",
            "give": "Give an item from this member's inventory to another member",
            "sell": "Sell an item in exchange for currency",
            "cancel": "return to command menu",
        }

    def displayCmds(self, cmd_list):
        for cmd, desc in cmd_list.items():
            print("> {:<8}: {}".format(cmd, desc))

    def choosePC(self, giving=False, giver=None):
        choosing = True
        chosenPC = 0

        while choosing:
            for pchar in self.animateList:
                if giving and pchar == giver:
                    pass
                else:
                    print("> {:<3}: {}".format(self.animateList.index(pchar) + 1, pchar.get_name()))
            chosenPC = input("> ")
            if chosenPC == "cancel":
                return "cancel"
            else:
                try:
                    chosenPC = int(chosenPC) - 1
                    if giving and giver == self.animateList[chosenPC]:
                        print("[ER] You can't give an item to yourself! Please pick another party member!")
                    elif 0 <= chosenPC < len(self.animateList):
                        choosing = False
                except ValueError:
                    print("[ER] invalid input! Please select a party member by inputting a number or enter 'cancel' to return")
                except IndexError:
                    print("[ER] invalid input! Please select a valid party member or enter 'cancel' to return")
        if giving:
            self.currentEntity = giver
            return self.animateList[chosenPC]
        else:
            self.currentEntity = self.animateList[chosenPC]
            return "success"

    def diceBranch(self):
        rolling = True
        while rolling:
            rolls = input("\nInput dice throw (\"num dice\"d\"num faces\"):\n> ")
            if rolls == "cancel":
                break
            try:
                rolls, faces = rolls.lower().split("d")
                self.rollDice(int(rolls), int(faces))
                print()
                rolling = False
            except ValueError:
                print("[ER] Please use the format \"num dice\"d\"num faces\")")

    def statsBranch(self):
        print("Whose stats would you like to view?")
        choice = self.choosePC()
        if choice == "cancel":
            pass
        else:
            self.currentEntity.showStats()

    def discardBranch(self, discarding=False, selling=False):
        term = None
        if discarding:
            term = "discard"
        elif selling:
            term = "sell"

        while discarding or selling:
            item_name = input("What would you like to " + term + "?\n> ")
            if item_name == "cancel":
                break
            item_amount = input("How many would you like to " + term + "?\n> ")
            if item_amount == "cancel":
                break
            elif term == "discard":
                discarding = not self.currentEntity.inv_remove(item_name, amount=item_amount, discarding=True)
            elif term == "sell":
                selling = not self.currentEntity.inv_remove(item_name, amount=item_amount, selling=True, notify=True)

    def equipBranch(self):
        equipping = True
        # self.currentEntity.inv_add("Spear")      # For testing
        while equipping:
            to_equip = input("What would you like to equip?\n> ")
            if to_equip == "cancel":
                break
            else:
                self.currentEntity.inv_equip(to_equip)
                equipping = False

    def useBranch(self):
        flag = False
        while not flag:
            to_use = input("What would you like to use?\n> ")
            if to_use == "cancel":
                break
            else:
                flag = self.currentEntity.inv_remove(to_use, using=True)

    # Look at next
    def giveBranch(self):
        giving = True
        giver = self.currentEntity
        while giving:

            to_give = input("What would you like to give?\n> ")
            if to_give == "cancel":
                break

            give_quantity = input("How many would you like to give?\n> ")
            if give_quantity == "cancel":
                break

            print("Who is receiving this?\n")
            recipient = self.choosePC(True, giver)
            if recipient == "cancel":
                break
            try:
                self.inv_give(recipient, to_give, give_quantity)
            except:
                print("[ER] Could not complete that!")

    def invBranch(self):
        print("Whose inventory would you like to view?")
        choice = self.choosePC()
        if choice == "cancel":
            pass
        else:
            viewing_inv = True
            while viewing_inv:
                invNotEmpty = self.currentEntity.inv_print()
                if not invNotEmpty:
                    self.currentEntity.inv_print(list_inv=False)

                print("What would you like to do with {}'s inventory?".format(self.currentEntity.get_name()))

                self.displayCmds(self.inv_commands)
                inv_action = input("> ")

                if inv_action not in self.inv_commands:
                    print("[ER] Invalid command! Please enter one of the commands above")

                elif inv_action == "cancel":
                    viewing_inv = False

                elif inv_action == "discard":
                    self.discardBranch(discarding=True)

                elif inv_action == "equip":
                    self.equipBranch()

                elif inv_action == "use":
                    self.useBranch()

                elif inv_action == "give":
                    self.giveBranch()

                elif inv_action == "sell":
                    self.discardBranch(selling=True)

                elif inv_action == "dequip":
                    toBeRemoved = input("What would you like to remove?\n> ")
                    self.currentEntity.inv_dequip(toBeRemoved)

    def prompt(self, ask, *args):
        while True:
            response = input(ask)
            if response in args:
                break
        return response

    def shortRest(self, dreamer):
        sResting = True
        while sResting:
            if dreamer.get_stat("Hit Dice Quantity") <= 0:
                print("[ER] {} has no more hit dice!".format(dreamer.name))
                break
            roll = randint(1, dreamer.get_stat("Hit Dice")) + self.modifier("Constitution", dreamer)
            if roll < 0:
                roll = 0
            dreamer.set_stats("Current HP", dreamer.get_stat("Current HP") + roll)
            print("{} has gained {} HP! Their HP is now {} /{}!".format(dreamer.name, roll,
                                                                        dreamer.get_stat("Current HP"),
                                                                        dreamer.get_stat("Max HP")))
            dreamer.set_stats("Hit Dice Quantity", dreamer.get_stat("Hit Dice Quantity") - 1)
            again = self.prompt("Would you like to take another short rest? (Y/N)\n> ", "y", "n", "Y", "N").lower()
            if again == "n":
                break

    def longRest(self, dreamer):
        if dreamer.get_stat("Current HP") < 1:
            print("[ER] A character must have at least 1 HP to benefit from a long rest!")
        else:
            dreamer.set_stats("Current HP", dreamer.get_stat("Max HP"))
            print("{} is now at full HP!".format(dreamer.name))
            if dreamer.get_stat("Hit Dice Quantity") < dreamer.level:
                recover = floor(dreamer.level / 2)
                dreamer.set_stats("Hit Dice Quantity", dreamer.get_stat("Hit Dice Quantity") + recover)
                if dreamer.get_stat("Hit Dice Quantity") > dreamer.level:
                    dreamer.set_stats("Hit Dice Quantity", dreamer.level)

    def restBranch(self):
        resting = True
        deciding = True
        while resting:
            print("Who would like to rest?")
            response = self.choosePC()
            dreamer = self.currentEntity
            if response == "cancel":
                break
            while deciding:
                restLen = self.prompt("Would you like to take a [short] rest or a [long] rest?\n>", "cancel", "short",
                                      "long")
                if restLen == "cancel":
                    break
                elif restLen == "short":
                    self.shortRest(dreamer)
                elif restLen == "long":
                    self.longRest(dreamer)

    def genLoop(self):
        while self.running_general:
            print("Current Location: {}\nWhat would you like to do?".format(self.name))
            self.displayCmds(self.commands)
            action = input("> ")
            action = action.lower().strip()

            if action not in self.commands.keys():
                print("[ER] Invalid command! Please enter one of the commands above!")

            elif action == "roll":
                self.diceBranch()

            elif action == "stats":
                self.statsBranch()

            elif action == "inv":
                self.invBranch()

            elif action == "move":
                print("SORRY!! Currently not implemented. :)")

            elif action == "rest":
                self.restBranch()

            elif action == "exit":
                print("Thank you for playing!")
                break


if __name__ == "__main__":
    nce = NCEncounter("slot", "town")
    nce.animateList = pickle.load(open("players.camp", "rb"))
    nce.genLoop()
    pickle.dump(nce.animateList, open("players.camp", "wb"))
