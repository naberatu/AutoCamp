
from animate import Animate
from statblock import StatBlock


class Enemy(Animate):
    def __init__(self, name, race=None, role=None, level=1, stat_block=StatBlock()):
        super().__init__(name, race, role, level, stat_block)      # should inherit everything this way
        self.exp = 0
        self.companion = None
        self.type_tag = "enemy"
        self.is_enemy = True
        self.maxInvSize = 10            # Arbitrary value
        self.weapon = None
        self.stat_block = stat_block
        self.stat_block.modify_stat("Max HP", 25)

    # Accessors
    # ==================================
    def get_exp_yield(self):
        return self.exp

    def inv_print(self):
        print("[ER] Enemies have no inventory!")
        return False

    # Mutators
    # ==================================
    def mod_exp_yield(self, amount):
        self.exp = amount

