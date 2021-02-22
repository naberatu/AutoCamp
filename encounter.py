from player import Player
from statblock import StatBlock
from random import randint
from math import floor
from animate import Animate
import items
import campaign


class Encounter:

    def __init__(self, name, is_shop=False, is_combat=False, vendor=None):
        self.name = name
        self.animateList = list()
        self.currentEntity = None
        self.is_shop = is_shop
        self.vendor = vendor
        self.is_combat = is_combat
        self.running_loop = True
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
        self.vend_commands = {
            "buy": "Purchase something from the vendor",
            "haggle": "Attempt to haggle with the vendor",
            "roll": "Roll di(ce)",
            "move": "Change your current location",
            "inv": "View more options regarding the party's inventory",
            "stats": "View a party member's stats",
            "rest": "Allow party members a moment of rest to recover",
            "exit": "save and quit."
        }

    def get_name(self):
        return self.name

    # ===============================================================================
    # Misc Helper Methods
    # ===============================================================================
    @staticmethod
    def displayCmds(cmd_list):
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
                    print(
                        "[ER] invalid input! Please select a party member by inputting a number or enter 'cancel' to return")
                except IndexError:
                    print("[ER] invalid input! Please select a valid party member or enter 'cancel' to return")
        if giving:
            self.currentEntity = giver
            return self.animateList[chosenPC]
        else:
            self.currentEntity = self.animateList[chosenPC]
            return "success"

    @staticmethod
    def prompt(ask, *args):
        while True:
            response = input(ask)
            if response in args:
                break
        return response

    # ===============================================================================
    # Dice Rolling Methods
    # ===============================================================================
    @staticmethod
    def rollDice(rolls, number_of_faces, print_results=True, set_form=False):
        total = 0
        values = list()

        if (rolls < 1) or (type(rolls) != int):
            print("Rolls must be whole numbers > 1!!")
            return total

        valid_faces = [4, 6, 8, 10, 12, 20]
        if number_of_faces not in valid_faces:
            print(str(number_of_faces) + " is not a valid number of faces!!")
            print("Valid dice are: d4, d6, d8, d10, d12, and d20.")
            return total

        for roll in range(rolls):
            result = randint(1, number_of_faces)
            if set_form:
                values.append(result)
            total += result

            if print_results:
                print("Rolling D{} {} of {}... Result is {}".format(number_of_faces, roll + 1, rolls, result))

        if set_form:
            return values
        elif print_results:
            print("Final total is... {}!!".format(total))
        return total

    @staticmethod
    def modifier(stat, ent):
        return floor(((ent.get_stat(stat)) - 10) / 2)

    def performCheck(self, stat, skill, ent, advantage=False, disadvantage=False, print_results=True):
        roll = 0
        roll1 = self.rollDice(1, 20, False)
        roll2 = self.rollDice(1, 20, False)
        if (advantage and disadvantage) or (not advantage and not disadvantage):
            roll = roll1
        elif advantage:
            roll = max(roll1, roll2)
        elif disadvantage:
            roll = min(roll1, roll2)

        mod = self.modifier(stat, ent)
        if print_results:
            print("{} rolled {} with {} modifier {}".format(ent.get_name(), roll, stat, mod))
        if skill is not None:
            roll += mod + ent.get_stat(skill)
        else:
            roll += mod
        if print_results:
            print("Result is... {}!!".format(roll))
        return roll

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

    # ===============================================================================
    # Stat-Relevant Method(s)
    # ===============================================================================
    def statsBranch(self):
        print("Whose stats would you like to view?")
        choice = self.choosePC()
        if choice == "cancel":
            pass
        else:
            self.currentEntity.showStats()

    def print_wares(self):
        print(("=" * 77) + "\n" + self.vendor.name + "'s Wares\n" + ("=" * 77))
        for item, quantity in self.vendor.inventory.items():
            print("{:<20}".format(item).ljust(20) + "\t\tx" + str(quantity) + "\t\t\t" + str(
                items.catalog[item].get_cost()) + " cp")
        print("=" * 77)

    # ===============================================================================
    # Inventory Methods
    # ===============================================================================
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

    def inv_give(self, recipient, item_name, amount=1):
        if not recipient.get_iff() and self.currentEntity.inv_remove(item_name, amount=amount, discarding=True,
                                                                     notify=False) \
                and recipient.inv_add(item_name, amount=amount):
            print("[OK] You gave", recipient.get_name(), amount, item_name, "!")
        else:
            print("[ER] Cannot give", item_name, "to", recipient.get_name(), "!")

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

    # ===============================================================================
    # Vendor Methods
    # ===============================================================================

    def buyBranch(self):
        buying = True
        while buying:
            to_buy = input("What would you like to buy?\n>")
            if to_buy == "cancel":
                break
            elif to_buy not in self.vendor.inventory.keys():
                print("[ER] That item is not being sold!")
            else:
                try:
                    buy_quantity = int(input("How many would you like to buy?\n>"))
                    if buy_quantity == "cancel":
                        break
                    elif buy_quantity > self.vendor.inventory[to_buy] or buy_quantity < 1:
                        print("[ER] You can not buy that amount!")
                    else:
                        print("Who is making this purchase?")
                        buyer = self.choosePC()
                        if buyer == "cancel":
                            pass
                        else:
                            cost = items.catalog[to_buy].get_cost() * buy_quantity
                            purchased = self.currentEntity.money_deduct(cost)
                            if purchased:
                                self.currentEntity.inv_add(to_buy, amount=buy_quantity)
                                self.vendor.inventory[to_buy] -= buy_quantity
                                if self.vendor.inventory[to_buy] == 0:
                                    del self.vendor.inventory[to_buy]
                                print("Purchase successful!")
                                break
                except ValueError:
                    print("[ER] Please enter a numeric quantity of {} to buy!".format(to_buy))

    def hag_loop(self, to_haggle, haggle_quantity, buying=False, selling=False):
        approved = False
        while not approved:
            try:
                if buying:
                    haggleAmnt = input("How much are you willing to spend (in copper pieces)?\n> ")
                else:
                    haggleAmnt = input("How much are you willing to sell for (in copper pieces)?\n> ")
                if haggleAmnt == "cancel":
                    break
                rollNeeded = self.prompt(
                    "Do you need to roll for [Deception], [Intimidation], or [Persuasion]? (If not necessary [0])\n> ",
                    "Deception", "deception", "Intimidation", "intimidation", "persuasion", "Persuasion", "0", "cancel")
                if rollNeeded == "cancel":
                    break
                elif rollNeeded.lower() in ["persuasion", "deception", "intimidation"]:
                    advOrDisadv = self.prompt("Are you at an [adv]antage, a [dis]advantage, or [0]neither?\n> ", "0",
                                              "adv", "dis")
                    if advOrDisadv == "cancel":
                        break
                    elif advOrDisadv == "adv":
                        self.performCheck("Charisma", rollNeeded.capitalize(), self.currentEntity, advantage=True)
                    elif advOrDisadv == "dis":
                        self.performCheck("Charisma", rollNeeded.capitalize(), self.currentEntity, disadvantage=True)
                    else:
                        self.performCheck("Charisma", rollNeeded.capitalize(), self.currentEntity)

                input("Hand the AutoCamp to your DM! (Press ENTER once handed over)")
                DM_approve = self.prompt("Does the vendor accept this haggle? (Y/N)\n> ", "y", "n", "Y", "N")
                input("Hand the AutoCamp to the current player! (Press ENTER once handed over)")

                if DM_approve.lower() == "n":
                    print("Haggle failed! Try again or [cancel]")
                    continue
                elif buying:
                    purchased = self.currentEntity.money_deduct(int(haggleAmnt))
                    if purchased:
                        self.currentEntity.inv_add(to_haggle, amount=int(haggle_quantity))
                        self.vendor.inventory[to_haggle] -= int(haggle_quantity)
                        if self.vendor.inventory[to_haggle] == 0:
                            del self.vendor.inventory[to_haggle]
                        print("Haggle successful! Haggle again or [cancel]")
                    break
                elif selling:
                    self.currentEntity.inv_remove(to_haggle, amount=int(haggle_quantity), haggling=True, haggle_cost=int(haggleAmnt))
                    if to_haggle in self.vendor.inventory.keys():
                        self.vendor.inventory[to_haggle] += int(haggle_quantity)
                    else:
                        self.vendor.inventory[to_haggle] = int(haggle_quantity)
                    print("Haggle successful! Haggle again or [cancel]")
                    break
            except ValueError:
                print("[ER] Please enter a numeric quantity of copper to haggle with!")

    def hag_buy(self):
        buying = True
        while buying:
            to_buy = input("What would you like to haggle for?\n> ")
            if to_buy == "cancel":
                break
            elif to_buy not in self.vendor.inventory.keys():
                print("[ER] That item is not being sold!")
            else:
                try:
                    buy_quantity = input("How many would you like to haggle for?\n> ")
                    if buy_quantity == "cancel":
                        break
                    elif int(buy_quantity) > self.vendor.inventory[to_buy] or int(buy_quantity) < 1:
                        print("[ER] You can not haggle for that amount!")
                    else:
                        print("Who is haggling?")
                        buyer = self.choosePC()
                        if buyer == "cancel":
                            pass
                        else:
                            self.hag_loop(to_buy, buy_quantity, buying=True)

                except ValueError:
                    print("[ER] Please enter a numeric quantity of {} to haggle for!".format(to_buy))

    def hag_sell(self):
        print("Who's trying to haggle away their stuff?")
        seller = self.choosePC()
        if seller == "cancel":
            pass
        else:
            selling = True
            while selling:
                invNotEmpty = self.currentEntity.inv_print()
                if not invNotEmpty:
                    self.currentEntity.inv_print(list_inv=False)
                to_sell = input("What would you like to haggle away?\n> ")
                if to_sell == "cancel":
                    break
                else:
                    try:
                        sell_quantity = input("How many would you like to haggle away?\n> ")
                        if sell_quantity == "cancel":
                            break
                        # elif to_sell != self.currentEntity.weapon and to_sell != self.currentEntity.armor:
                        #     if int(sell_quantity) > self.currentEntity.inventory[to_sell] or int(sell_quantity) < 1:
                        #         print("[ER] You can not haggle away that amount!")
                        else:
                            self.hag_loop(to_sell, sell_quantity, selling=True)
                    except ValueError:
                        print("[ER] Please enter a numeric quantity of {} to haggle for!".format(to_sell))

    def haggleBranch(self):
        buyOrSell = self.prompt("Would you like to haggle over the [merchant]'s wares or someone in the [party]'s?\n> ",
                                "merchant", "party", "cancel").lower()
        if buyOrSell == "cancel":
            pass
        if buyOrSell == "merchant":
            self.hag_buy()

        if buyOrSell == "party":
            self.hag_sell()

    # ===============================================================================
    # Resting Methods
    # ===============================================================================
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

    # ===============================================================================
    # The Loops
    # ===============================================================================
    def genLoop(self):
        self.running_loop = True
        while self.running_loop:
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
                break

            elif action == "rest":
                self.restBranch()

            elif action == "exit":
                print("Thank you for playing!")
                exit()

    def vendLoop(self):
        self.running_loop = True
        while self.running_loop:
            self.print_wares()
            print("Current Location: {}\nWhat would you like to do?".format(self.name))
            self.displayCmds(self.vend_commands)
            action = input("> ")
            action = action.lower().strip()

            if action not in self.vend_commands.keys():
                print("[ER] Invalid command! Please enter one of the commands above!")

            elif action == "buy":
                self.buyBranch()

            elif action == "haggle":
                self.haggleBranch()

            elif action == "roll":
                self.diceBranch()

            elif action == "stats":
                self.statsBranch()

            elif action == "inv":
                self.invBranch()

            elif action == "move":
                break

            elif action == "rest":
                self.restBranch()

            elif action == "exit":
                print("Thank you for playing!")
                exit()


if __name__ == "__main__":

    nce1 = Encounter("Town")
    nce2 = Encounter("Mountains")
    nce3 = Encounter("Forest")
    nce4 = Encounter("Caves")
    nce5 = Encounter("Temmie's", is_shop=True)

    encounters = [nce1, nce2, nce3, nce4, nce5]

    sBlocks = [StatBlock(), StatBlock(), StatBlock(), StatBlock(), StatBlock()]

    players = [
        Player("Fjord", "Orc", "Warlock", stat_block=sBlocks[0]),
        Player("Jester Lavorre", "Tiefling", "Cleric", stat_block=sBlocks[1]),
        Player("Caleb Widowgast", "Human", "Wizard", stat_block=sBlocks[2]),
        Player("Yasha Nyoodrin", "Aasimar", "Barbarian", stat_block=sBlocks[3]),
        Player("Veth Brenatto", "Goblin", "Rogue", stat_block=sBlocks[4])]

    for p in players:
        p.inv_add("Shortsword")
        p.inv_add("Dagger")
        p.inv_add("Chain Mail")
        p.inv_add("Padded Armor")
        p.inv_add("Mana Potion", randint(1, 6))
        p.inv_equip("Chain Mail")
        p.level_up()
        p.level_up()
        p.level_up()
        p.set_stats("Current HP", 1)
        p.set_stats("Constitution", randint(1, 17))
        p.money_add(5, 7, 300)

    for enc in encounters:
        enc.animateList = players

    # (self, name, race=None, role=None, level=1, stat_block=StatBlock())
    merchant = Animate("Tem", "Temmie", "Vendor")

    merchant.inventory["Spear"] = 3
    merchant.inventory["Padded Armor"] = 3
    merchant.inventory["Mana Potion"] = 10
    merchant.inventory["Scale Mail"] = 2

    nce5.vendor = merchant

    # nce1.genLoop()
    nce5.vendLoop()
