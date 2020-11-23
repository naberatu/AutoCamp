
from animate import Animate
import random

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
    def __init__(self, name, entity_id, race, role, level, stat_block):
        super().__init__(name, entity_id, race, role, level, stat_block)      # should inherit everything this way
        self.exp = 0                    # This should be changed depending on the player's level?
        self.is_enemy = False
        self.maxInvWeight = 200         # Arbitrary value
        self.companion = None           # We can add functionality to adjust later
        self.stat_block = stat_block
        self.stat_block.modify_stat("Proficiency Bonus", 2)

        # Updates
        # ===============================================================================
        if race == ("Dwarf" or "Gnome" or "Halfling"):
            self.stat_block.modify_stat("Speed", 20)
        else:
            self.stat_block.modify_stat("Speed", 30)

        self.stat_block.modify_stat("Hit Dice", role_dict[role])
        if self.level == 1:
            self.stat_block.modify_stat("Max HP", role_dict[role])
            self.stat_block.modify_stat("Current HP", role_dict[role])
        # ===============================================================================

        self.weapon = None              # a player is either wielding a weapon, or isn't
        self.armor = None               # a player either is wearing armor, or ain't.
        self.feats = list()
        self.spellSlots = list()        # Make cell 1 hold number of Lvl 1 Spell Slots, cell 2 for lvl 2, etc.

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

    def print_inv(self, list_equipped):
        if self.inventory == {}:
            print("[ER] Your inventory is empty!")
            return

        print("=============================================================================")
        print(self.name + "\'s Inventory")
        print("-----------------------------------------------------------------------------")

        if list_equipped:
            print("Weapon: " + "{:<20}".format(self.get_weapon().get_name())
                  + "\tArmor: " + "{:<20}".format(self.get_armor().get_name()))
            print("=============================================================================")

        for item, quantity in self.inventory.items():
            print("{:<20}".format(item.get_name()).ljust(20) + "\t\tx" + str(quantity))
        print("=============================================================================")

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
