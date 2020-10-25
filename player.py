
from animate import Animate


class Player(Animate):
    def __init__(self, name, entity_id, race, role, level):
        super().__init__(name, entity_id, race, role, level)      # should inherit everything this way
        self.exp = 0                    # This should be changed depending on the player's level?
        self.maxInvWeight = 200         # Arbitrary value
        self.companion = None           # We can add functionality to adjust later

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

    # Mutators
    # ==================================
    def gain_exp(self, amount):
        self.exp += amount

    def swap_weapon(self, entity_id):
        for i in self.inventory:
            if self.inventory[i].entity_id == entity_id:
                temp = self.weapon
                self.weapon = self.inventory[i]
                self.inventory[i] = temp
                return 0                        # meaning successful swap
        return -1                               # weapon not found


