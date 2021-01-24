from encounter import Encounter
from inanimate import Inanimate
from random import randint
from player import Player
from statblock import StatBlock
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
            try:
                rolls = input("How many dice?\n> ")
                if rolls == "cancel":
                    rolling = False
                    continue
                faces = input("How many faces?\n> ")
                if faces == "cancel":
                    rolling = False
                    continue
                self.rollDice(int(rolls), int(faces))
                print()
                rolling = False
            except ValueError:
                print(
                    "[ER] Invalid input! Number of dice must be a whole number > 1.\n\t Valid dice are: d4, d6, d8, d10, d12, and d20.")

    def statsBranch(self):
        print("Whose stats would you like to view?")
        choice = self.choosePC()
        if choice == "cancel":
            pass
        else:
            self.showStats()

    # def getItemQuantity(self, name, ent):
    #     pcInventory = ent.get_inv()
    #     for obj in pcInventory:
    #         if obj.get_name() == name:
    #             return pcInventory[obj]

    # def itemFromName(self, name):
    #     pcInventory = self.currentEntity.get_inv()
    #     for obj in pcInventory:
    #         if obj.get_name() == name:
    #             return obj

    # def isWearing(self, name):
    #     if self.currentEntity.get_armor() == self.itemFromName(name):
    #         return True
    #     elif self.currentEntity.get_weapon() == self.itemFromName(name):
    #         return True
    #     else:
    #         return False

    # def inv_dequip(self, name):
    #     if self.itemFromName(name) == self.currentEntity.get_armor():
    #         self.currentEntity.set_armor(None)
    #     elif self.itemFromName(name) == self.currentEntity.get_weapon():
    #         self.currentEntity.set_weapon(None)

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
        self.currentEntity.inv_add("Spear")
        while equipping:
            to_equip = input("What would you like to equip?\n> ")
            if to_equip == "cancel":
                break
            # elif to_equip not in [x.get_name() for x in self.currentEntity.get_inv().keys()]:
            #     print("[ER] {} not in inventory! Please select something in your inventory".format(
            #         to_equip))
            # elif self.isWearing(to_equip):
            #     print("[ER] {} is already wearing {}!".format(self.currentEntity.get_name(), to_equip))
            # elif self.itemFromName(to_equip).is_armor == False and self.itemFromName(to_equip).is_weapon == False:
            #     print("[ER]: The item you are trying to equip is neither armor nor a weapon!")
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

    def giveBranch(self):
        giving = True
        giver = self.currentEntity
        while giving:
            to_give = input("What would you like to give?\n> ")
            if to_give == "cancel":
                giving = False
                continue
            elif to_give not in [x.get_name() for x in self.currentEntity.get_inv().keys()]:
                print("[ER] {} not in inventory! Please select something in your inventory".format(to_give))
                continue

            give_quantity = input("How many would you like to give?\n> ")
            try:
                if give_quantity == "cancel":
                    giving = False
                    continue
                elif int(give_quantity) < 0 or int(give_quantity) > self.getItemQuantity(
                        to_give, self.currentEntity):
                    print("[ER] You can not give away that many!")
                else:
                    print("Who is receiving this?\n")
                    recipient = self.choosePC(True, giver)
                    if recipient == "cancel":
                        giving = False
                        continue
                    elif self.getItemQuantity(to_give, recipient) == self.itemFromName(to_give).maxStack:
                        print("[ER] Can not give item to {}, they have the maximum limit for that item!".format(recipient.get_name()))
                        continue
                    elif self.isWearing(to_give):
                        self.inv_dequip(to_give)
                    self.inv_give(recipient, self.itemFromName(to_give), int(give_quantity))
                    giving = False
            except ValueError:
                print("[ER] Please input a positive whole number to give away!")

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
    NCE1 = NCEncounter("placeholder", "town")

    # dagger = Inanimate("Rusty Butter Knife", 4, 25,
    #                    "Jagged at the edges from facing too many slices of toast. Still smells faintly of butter.",
    #                    1, 1)
    # sword = Inanimate("Iron Sword", 1, 20, "Deals +2 Damage", 1, 4)
    # armor = Inanimate("Chainmail", 2, 20, "Provides +10 AC", 1, 6)
    # potion = Inanimate("Mana Potion", 3, 30, "Restores Mana", 6, 0.5)
    # monies = Inanimate("Gold", 5, 1, "Ooo, shiny!!", 1000000, 0.1)

    # dagger.is_weapon = True
    # sword.is_weapon = True
    # armor.is_armor = True
    # potion.is_consumable = True
    #
    # players = [Player("Fjord", randint(1, 10000), "Orc", "Warlock", 1, StatBlock()),
    #            Player("Jester Lavorre", randint(1, 10000), "Tiefling", "Cleric", 1, StatBlock()),
    #            Player("Caleb Widowgast", randint(1, 10000), "Human", "Wizard", 1, StatBlock()),
    #            Player("Yasha Nyoodrin", randint(1, 10000), "Aasimar", "Barbarian", 1, StatBlock()),
    #            Player("Veth Brenatto", randint(1, 10000), "Goblin", "Rogue", 1, StatBlock())]
    #
    # for p in players:
    #     p.inv_add(sword, 1)
    #     p.inv_add(armor, 1)
    #     p.inv_add(potion, randint(1, 6))
    #     p.inv_add(dagger, 1)
    #     p.inv_add(monies, randint(1, 1000))
    #     p.set_weapon(sword)
    #     p.set_armor(armor)
    #     NCE1.add_entity(p)

    NCE1.animateList = pickle.load(open("players.camp", "rb"))

    NCE1.genLoop()
