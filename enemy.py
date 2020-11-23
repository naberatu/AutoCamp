
from animate import Animate


class Enemy(Animate):
    def __init__(self, name, entity_id, race, role, level, stat_block):
        super().__init__(name, entity_id, race, role, level, stat_block)      # should inherit everything this way
        self.expYield = 0
        self.is_enemy = True
        self.maxInvSize = 10            # Arbitrary value
        self.weapon = None
        self.stat_block = stat_block

    # Accessors
    # ==================================
    def get_exp_yield(self):
        return self.expYield

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
    def mod_exp_yield(self, amount):
        self.expYield = amount

