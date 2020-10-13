
from animate import Animate
from statblock import StatBlock


class NCC(Animate):
    def __init__(self, name, id, role, race):
        super().__init__(name, id)      # should inherit everything this way
        self.statBlock = StatBlock()    # empty stat block
        self.role = role               # Distinct just in case we add multi-classing.
        self.race = race

    # Accessors
    # ==================================
    def get_role(self):
        return self.role

    def get_race(self):
        return self.race

    # Mutators
    # ==================================
    def mod_role(self, role):
        self.role = role

    def mod_race(self, race):
        self.race = race
