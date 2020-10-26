
from animate import Animate


class Enemy(Animate):
    def __init__(self, name, entity_id, race, role, level):
        super().__init__(name, entity_id, race, role, level)      # should inherit everything this way
        self.expYield = 0
        self.is_enemy = True
        self.maxInvSize = 10            # Arbitrary value
        self.weapon = None

    # Accessors
    # ==================================
    def get_exp_yield(self):
        return self.expYield

    # Mutators
    # ==================================
    def mod_exp_yield(self, amount):
        self.expYield = amount

