
from animate import Animate
from statblock import StatBlock


class Enemy(Animate):
    def __init__(self, name, id, role, race, level):
        super().__init__(name, id)      # should inherit everything this way
        self.statBlock = StatBlock()    # empty stat block
        self.role = role
        self.race = race
        self.level = level
        self.expYield = 0
        self.maxInvSize = 10         # Arbitrary value

    weapon = None
    inventory = []

    # Accessors
    # ==================================
    def get_level(self):
        return self.level

    def get_exp_yield(self):
        return self.expYield

    def get_role(self):
        return self.role

    def get_race(self):
        return self.race

    # Mutators
    # ==================================
    def mod_level(self, value):
        self.level = value

    def mod_exp_yield(self, amount):
        self.expYield = amount

    def mod_role(self, role):
        self.role1 = role

    def mod_race(self, race):
        self.race = race
