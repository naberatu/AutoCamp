
from animate import Animate
import random
import items
from statblock import StatBlock

role_dict = {
    "Barbarian": 12,
    "Bard": 8,
    "Cleric": 8,
    "Druid": 8,
    "Fighter": 10,
    "Monk": 8,
    "Paladin": 10,
    "Ranger": 10,
    "Rogue": 8,
    "Sorcerer": 6,
    "Warlock": 8,
    "Wizard": 6,
    "Artificer": 8,
    "Blood Hunter": 10
}


class Player(Animate):
    def __init__(self, name, race=None, role=None, level=1, stat_block=StatBlock(), entity_id=random.randint(0, 99999)):
        super().__init__(name, race, role, level, stat_block)      # should inherit everything this way

        self.entity_id = entity_id
        self.exp = 0                    # This should be changed depending on the player's level?
        self.is_enemy = False
        self.maxInvWeight = 210         # Arbitrary value
        self.companion = None           # We can add functionality to adjust later
        self.stat_block = stat_block
        # self.stat_block.modify_stat("Proficiency Bonus", 2)

        if race == ("Dwarf" or "Gnome" or "Halfling"):
            self.stat_block.modify_stat("Speed", 25)
        else:
            self.stat_block.modify_stat("Speed", 30)

        self.stat_block.modify_stat("Hit Dice", role_dict[role])
        if self.level == 1:
            self.stat_block.modify_stat("Max HP", role_dict[role])
            self.stat_block.modify_stat("Current HP", role_dict[role])

        self.weapon = None              # a player is either wielding a weapon, or isn't
        self.armor = None               # a player either is wearing armor, or ain't.
        self.money = {"gold": 0, "silver": 0, "copper": 0}      # The player's Money.
        self.feats = list()
        self.spellSlots = list()        # Make cell 1 hold number of Lvl 1 Spell Slots, cell 2 for lvl 2, etc.
        self.death_strikes = 0
        self.death_evasions = 0
        self.is_stable = True

    # ==================================
    # Inventory
    # ==================================
    def money_add(self, copper=1, silver=0, gold=0):    # Gives the player money.
        # If illogical values are placed, don't bother.
        if copper < 0 or silver < 0 or gold < 0:
            return

        self.money["copper"] += copper
        self.money["silver"] += silver
        self.money["gold"] += gold

        if copper >= 10:
            new_c = self.money["copper"] % 10
            old_c = self.money["copper"] - new_c
            self.money["copper"] = new_c
            self.money_add(0, int(old_c / 10), 0)

        if silver >= 10:
            new_s = self.money["silver"] % 10
            old_s = self.money["silver"] - new_s
            self.money["silver"] = new_s
            self.money_add(0, 0, int(old_s / 10))

    def inv_add(self, item, amount=1):
        if self.inv_is_full():
            return

        if items.catalog[item].get_is_weapon() and self.weapon is None:
            self.weapon = items.catalog[item]
        elif self.inv_scheme == "weight":
            added_weight = item.get_weight() * amount
            if self.get_inv_size() + added_weight <= self.inv_max:
                if item in self.inventory:
                    self.inventory[item] += amount
                else:
                    self.inventory[item] = amount
            else:
                print("[ER] It's too much to carry!")
        else:
            if item in self.inventory:
                self.inventory[item] += amount
            else:
                self.inventory[item] = amount

    def inv_equip(self, item, is_weapon=True):
        # If it doesn't exist, don't bother.
        if item not in self.inventory.keys():
            print("[ER] Item not found!")
            return

        # If it's not a weapon, then check if it's armor.
        is_armor = False
        if not is_weapon:
            is_armor = items.catalog[item].get_is_armor()

        # If it's neither weapon nor armor, don't do anything.
        if not is_weapon and not is_armor:
            print("[ER] You can't equip that!")
            return

        # Perform the swap
        if is_weapon:
            if self.weapon:
                self.inv_add(self.weapon)
            self.weapon = item
            self.inv_remove(item)
        elif is_armor:
            if self.armor:
                self.inv_add(self.armor)
            self.armor = item
            self.inv_remove(item)

    def inv_print(self, list_equipped=True):
        if self.inventory == {}:
            print("[ER] Your inventory is empty!")
            return False

        print("\n=============================================================================")
        print(self.name + "\'s Inventory")
        print("=============================================================================")

        print("Gold: " + "{:<4}".format(self.money["gold"])
              + "\t\tSilver: " + "{:<4}".format(self.money["silver"])
              + "\tCopper: " + "{:<4}".format(self.money["copper"]) )

        if list_equipped:
            if (self.get_armor() is None) and (self.get_weapon() is None):
                print("Weapon: " + "{:<20}".format("None")
                      + "\tArmor: " + "{:<20}".format("None"))
            elif self.get_armor() is None:
                print("Weapon: " + "{:<20}".format(self.get_weapon())
                      + "\tArmor: " + "{:<20}".format("None"))
            elif self.get_weapon() is None:
                print("Weapon: " + "{:<20}".format("None")
                      + "\tArmor: " + "{:<20}".format(self.get_armor()))
            else:
                print("Weapon: " + "{:<20}".format(self.get_weapon())
                      + "\tArmor: " + "{:<20}".format(self.get_armor()))

        print("-----------------------------------------------------------------------------")
        for item, quantity in self.inventory.items():
            print("{:<20}".format(item).ljust(20) + "\t\tx" + str(quantity))
        print("=============================================================================")
        return True

    def inv_remove(self, item, amount=1, discarding=True, selling=False, notify=True):
        if self.inventory == {}:
            print("[ER] Your inventory is empty!")
            return False
        try:
            if selling:
                earnings = item.get_cost() * amount

            if self.inv_use(item):
                self.inventory[item] -= amount
                if self.inventory[item] <= 0:
                    del self.inventory[item]
                if discarding and notify:
                    print("[OK] You have discarded", amount, item, "!")
                return True
            else:
                print("[ER] You cannot discard this item")
        except:
            return False

    def set_inv_scheme(self, scheme=None):
        if scheme == "slot" or scheme == "weight" or scheme is None:
            self.inv_scheme = scheme
        else:
            print("[ER] Invalid inventory scheme!")

    def get_inv_scheme(self):
        return self.inv_scheme

    def set_inv_max_size(self, size):
        self.inv_max = size

    def get_inv_max(self):
        return self.inv_max

    def inv_use(self, item):
        if (self.weapon == item or self.armor == item) and self.inventory[item] == 1:
            return False
        else:
            return True

    # ==================================
    # Accessors
    # ==================================
    def get_exp(self):
        return self.exp

    def get_weapon(self):
        return self.weapon

    def get_armor(self):
        return self.armor

    def get_companion(self):
        return self.companion

    def get_death_strikes(self):
        return self.death_strikes

    def get_death_evasions(self):
        return self.death_evasions

    def inv_is_full(self, notify=True):
        # -------------------------------------------------------
        if self.inv_scheme == "slot":
            if len(self.inventory) == self.inv_max:
                if notify:
                    print("[ER] Your inventory is full!")
                return True
            else:
                return False
        # -------------------------------------------------------
        elif self.inv_scheme == "weight":
            if self.get_inv_size() >= self.inv_max:
                if notify:
                    print("[ER] Your inventory is full!")
                return True
            else:
                return False
        # -------------------------------------------------------
        elif self.inv_scheme is None:
            return False

    def get_inv_size(self):
        if self.inv_scheme == "slot":
            return len(self.inventory)
        elif self.inv_scheme == "weight":
            total_weight = 0
            for i in self.inventory:
                total_weight += i[0].get_weight * i[1]
            return total_weight
        else:
            print("[OK] Your inventory is infinite!")
            return -1

    # def find_item(self, item_name, notify=True):
    #     for item in self.inventory:
    #         if item.get_name() == item_name:
    #             if notify:
    #                 print("[OK] Aha, found it!")
    #             return item
    #     if notify:
    #         print("[ER] You don't have this item!")
    #     return False

    # ==================================
    # Mutators
    # ==================================
    def gain_exp(self, amount):
        self.exp += amount

    # def swap_weapon(self, item):
    #     for i in self.inventory:
    #         if self.inventory[i].entity_id == item:
    #             temp = self.weapon
    #             self.weapon = self.inventory[i]
    #             self.inventory[i] = temp
    #             return 0                        # meaning successful swap
    #     return -1                               # weapon not found

    def set_armor(self, item):
        self.armor = item

    def set_weapon(self, item):
        self.weapon = item

    def set_companion(self, friend):
        self.companion = friend

    def set_death_strikes(self, strikes):
       self.death_strikes = strikes

    def set_death_evasions(self, evasions):
       self.death_evasions = evasions

    def set_stability(self, stability_status):
       self.is_stable = stability_status