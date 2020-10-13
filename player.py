
from animate import Animate
from statblock import StatBlock


class Player(Animate):
    def __init__(self, name, id, role, race, gender, level):
        super().__init__(name, id)      # should inherit everything this way
        self.statBlock = StatBlock()    # empty stat block
        self.role = role                # Distinct just in case we add multi-classing.
        # self.role2 = None             # We can adjust this later on
        self.race = race
        self.gender = gender
        self.level = level
        self.exp = 0                    # This should be changed depending on the player's level?
        self.maxInvWeight = 200         # Arbitrary value
        self.companion = None           # We can add functionality to adjust later

    weapon = None           # a player is either wielding a weapon, or isn't
    armor = None            # a player either is wearing armor, or ain't.
    feats = []
    spellSlots = []         # Make cell 1 hold number of Lvl 1 Spell Slots, cell 2 for lvl 2, etc.

    # Accessors
    # ==================================
    def get_level(self):
        return self.level

    def get_exp(self):
        return self.exp

    def get_role(self):
        # if self.role2 is not None:
        #     return self.role1, self.role2
        # else:
        return self.role

    def get_race(self):
        return self.race

    def get_weapon(self):
        return self.weapon

    # Mutators
    # ==================================
    def level_up(self):
        self.level += 1

    def mod_level(self, value):
        self.level = value

    def gain_exp(self, amount):
        self.exp += amount

    def mod_role(self, role):
        self.role = role

    def mod_race(self, race):
        self.race = race

    # def add_multiclass(self, multiclass):
    #     self.role2 = multiclass

    def swap_weapon(self, id):
        for i in self.inventory:
            if self.inventory[i].id == id:
                temp = self.weapon
                self.weapon = self.inventory[i]
                self.inventory[i] = temp
                return 0                        # meaning successful swap
        return -1                               # weapon not found


