
from animate import Animate
from statblock import StatBlock


class Player(Animate):
    def __init__(self, name, id, role, race, gender, level):
        super().__init__(name, id)      # should inherit everything this way
        self.statBlock = StatBlock()    # empty stat block
        self.role1 = role               # Distinct just in case we add multi-classing.
        self.role2 = None               # We can adjust this later on
        self.race = race
        self.gender = gender
        self.level = level
        self.exp = 0                    # This should be changed depending on the player's level?
        self.maxInvWeight = 200         # Arbitrary value
        self.companion = None           # We can add functionality to adjust later

    weapon = None       # a player is either wielding a weapon, or isn't
    armor = None        # a player either is wearing armor, or ain't.
    inventory = []      # an array of X items?
    feats = []
    # spells = spells()     # could be a class that stores spells in a dictionary??
    spellSlots = []         # Make cell 1 hold number of Lvl 1 Spell Slots, cell 2 for lvl 2, etc.


    # Accessors
    # ==================================
    def get_level(self):
        return self.level

    def get_exp(self):
        return self.exp

    def get_role(self):
        if self.role2 is not None:
            return self.role1, self.role2
        else:
            return self.role1

    def get_race(self):
        return self.race

    # Mutators
    # ==================================
    def level_up(self):
        self.level += 1

    def mod_level(self, value):
        self.level = value

    def gain_exp(self, amount):
        self.exp += amount

    def mod_role(self, role):
        self.role1 = role

    def mod_race(self, race):
        self.race = race

    def add_multiclass(self, multiclass):
        self.role2 = multiclass