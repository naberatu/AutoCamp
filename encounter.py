from player import Player
from statblock import StatBlock
from random import randint
from math import floor
from animate import Animate
import items
# import campaign


class Encounter:
    def __init__(self, name, is_shop=False, is_combat=False, anim=None, bkgd="./assets/tavern.jpg", vendor=None):
        self.name = name

        if anim is None:
            anim = list()

        self.animate_list = anim

        self.bkgd = bkgd
        self.is_shop = is_shop
        self.vendor = vendor
        self.is_combat = is_combat
        self.running_loop = True

    def get_name(self):
        return self.name

    def get_bg(self):
        return self.bkgd

    def load_players(self, player_list):
        for ent in self.animate_list:
            if type(ent) == Player:
                return

        for pl in player_list:
            self.animate_list.append(pl)

    def save_players(self):
        returning = list()
        non_player = list()
        for ent in self.animate_list:
            if type(ent) == Player:
                returning.append(ent)
            else:
                non_player.append(ent)
        self.animate_list = non_player
        return returning

    def read_players(self):
        player_list = list()
        for ent in self.animate_list:
            if type(ent) == Player:
                player_list.append(ent)

        return player_list

    def get_anim(self):
        return self.animate_list

    def new_player(self, np):
        self.animate_list.append(np)

    def rem_player(self, e_id):
        to_remove = None
        for pl in self.animate_list:
            if pl.entity_id == e_id:
                to_remove = pl
                break
        if to_remove is not None:
            self.animate_list.remove(to_remove)

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
            for pchar in self.animate_list:
                if giving and pchar == giver:
                    pass
                else:
                    print("> {:<3}: {}".format(self.animate_list.index(pchar) + 1, pchar.get_name()))
            chosenPC = input("> ")
            if chosenPC == "cancel":
                return "cancel"
            else:
                try:
                    chosenPC = int(chosenPC) - 1
                    if giving and giver == self.animate_list[chosenPC]:
                        print("[ER] You can't give an item to yourself! Please pick another party member!")
                    elif 0 <= chosenPC < len(self.animate_list):
                        choosing = False
                except ValueError:
                    print(
                        "[ER] invalid input! Please select a party member by inputting a number or enter 'cancel' to return")
                except IndexError:
                    print("[ER] invalid input! Please select a valid party member or enter 'cancel' to return")
        if giving:
            self.currentEntity = giver
            return self.animate_list[chosenPC]
        else:
            self.currentEntity = self.animate_list[chosenPC]
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
        crit_hit = False
        roll1 = self.rollDice(1, 20, False)
        roll2 = self.rollDice(1, 20, False)
        if (advantage and disadvantage) or (not advantage and not disadvantage):
            roll = roll1
        elif advantage:
            roll = max(roll1, roll2)
        elif disadvantage:
            roll = min(roll1, roll2)

        if roll >= 20:
            crit_hit = True

        mod = self.modifier(stat, ent)
        if print_results:
            print("{} rolled {} with {} modifier {}".format(ent.get_name(), roll, stat, mod))
        if skill is not None:
            roll += mod + ent.get_stat(skill)
        else:
            roll += mod
        if print_results:
            print("Result is... {}!!".format(roll))

        return [roll, crit_hit]

    def print_wares(self):
        print(("=" * 77) + "\n" + self.vendor.name + "'s Wares\n" + ("=" * 77))
        for item, quantity in self.vendor.inventory.items():
            print("{:<20}".format(item).ljust(20) + "\t\tx" + str(quantity) + "\t\t\t" + str(
                items.c_items[item].get_cost()) + " cp")
        print("=" * 77)

    # ===============================================================================
    # Inventory Methods
    # ===============================================================================
    def inv_give(self, giver, recipient, item_name, amount=1, notify=False):
        friend = not recipient.get_iff()
        rem_success = giver.inv_remove(item_name, amount=amount, discarding=True, notify=False)
        add_success = recipient.inv_add(item_name, amount=amount)

        if notify:
            if friend and rem_success and add_success:
                print("[OK] You gave", recipient.get_name(), amount, item_name, "!")
            else:
                print("[ER] Cannot give", item_name, "to", recipient.get_name(), "!")

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
                            cost = items.c_items[to_buy].get_cost() * buy_quantity
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
                        self.performCheck("Charisma", rollNeeded.capitalize(), self.currentEntity, advantage=True)[0]
                    elif advOrDisadv == "dis":
                        self.performCheck("Charisma", rollNeeded.capitalize(), self.currentEntity, disadvantage=True)[0]
                    else:
                        self.performCheck("Charisma", rollNeeded.capitalize(), self.currentEntity)[0]

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
    # The Loops
    # ===============================================================================
    # def genLoop(self):
    #     self.running_loop = True
    #     while self.running_loop:
    #         print("Current Location: {}\nWhat would you like to do?".format(self.name))
    #         self.displayCmds(self.commands)
    #         action = input("> ")
    #         action = action.lower().strip()
    #
    #         if action not in self.commands.keys():
    #             print("[ER] Invalid command! Please enter one of the commands above!")
    #
    #         elif action == "roll":
    #             self.diceBranch()
    #
    #         elif action == "stats":
    #             self.statsBranch()
    #
    #         elif action == "inv":
    #             self.invBranch()
    #
    #         elif action == "move":
    #             break
    #
    #         elif action == "rest":
    #             self.restBranch()
    #
    #         elif action == "exit":
    #             print("Thank you for playing!")
    #             exit()
    #
    # def vendLoop(self):
    #     self.running_loop = True
    #     while self.running_loop:
    #         self.print_wares()
    #         print("Current Location: {}\nWhat would you like to do?".format(self.name))
    #         self.displayCmds(self.vend_commands)
    #         action = input("> ")
    #         action = action.lower().strip()
    #
    #         if action not in self.vend_commands.keys():
    #             print("[ER] Invalid command! Please enter one of the commands above!")
    #
    #         elif action == "buy":
    #             self.buyBranch()
    #
    #         elif action == "haggle":
    #             self.haggleBranch()
    #
    #         elif action == "roll":
    #             self.diceBranch()
    #
    #         elif action == "stats":
    #             self.statsBranch()
    #
    #         elif action == "inv":
    #             self.invBranch()
    #
    #         elif action == "move":
    #             break
    #
    #         elif action == "rest":
    #             self.restBranch()
    #
    #         elif action == "exit":
    #             print("Thank you for playing!")
    #             exit()
