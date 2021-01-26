from encounter import Encounter
import pickle


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
            "rest" : "Allow party members a moment of rest to recover"
        }
        self.inv_commands = {
            "use": "Use an item in this member's inventory",
            "equip": "Arrange this member's equipment",
            "discard": "Discard an item from this member's inventory",
            "give" : "Give an item from this member's inventory to another member",
            "cancel": "return to command menu"
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
                    print("[ER] invalid input! Please select a party member or enter 'cancel' to return")
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
            rolls, faces = rolls.lower().split("d")
            self.rollDice(int(rolls), int(faces))
            print()
            rolling = False

    def statsBranch(self):
        print("Whose stats would you like to view?")
        choice = self.choosePC()
        if choice == "cancel":
            pass
        else:
            self.currentEntity.showStats()

    def discardBranch(self):
        discarding = True
        while discarding:
            to_discard = input("What would you like to discard?\n> ")
            if to_discard == "cancel":
                break
            discard_quantity = input("How many would you like to discard?\n> ")
            if discard_quantity == "cancel":
                break
            else:
                discarding = not self.currentEntity.inv_remove(to_discard, amount=discard_quantity, discarding=True)

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
                self.currentEntity.inv_print()

                print("What would you like to do with {}'s inventory?".format(self.currentEntity.get_name()))

                self.displayCmds(self.inv_commands)
                inv_action = input("> ")

                if inv_action not in self.inv_commands:
                    print("[ER] Invalid command! Please enter one of the commands above")

                elif inv_action == "cancel":
                    viewing_inv = False

                elif inv_action == "discard":
                    self.discardBranch()

                elif inv_action == "equip":
                    self.equipBranch()

                elif inv_action == "use":
                    self.useBranch()

                elif inv_action == "give":
                    self.giveBranch()

    def genLoop(self):
        while self.running_general:

            print("What would you like to do?")
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
                print("SORRY!! Currently not implemented. :)")


if __name__ == "__main__":
    nce = NCEncounter("slot", "town")
    nce.animateList = pickle.load(open("players.camp", "rb"))
    nce.genLoop()
    pickle.dump(nce.animateList, open("players.camp", "wb"))
