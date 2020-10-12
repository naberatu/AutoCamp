
from entity import Entity
from statblock import StatBlock


class Animate(Entity):

    def __init__(self, name, id):
        super().__init__(name, id)    # should inherit everything this way
        self.statBlock = StatBlock()  # empty stat block
        self.inventory = list()

    # Accessors
    # ==================================
    def get_stat(self, stat):
        self.statBlock.get_stat(stat)

    def add_to_inv(self, *args, **kwargs):
        self.inventory.append(args)
        self.inventory.append(kwargs)

    # Mutators
    # ==================================
    def set_stats(self, stat, num, faces=None):
        if faces is None:
            self.statBlock.modify_stat(stat, num)
        else:
            self.statBlock.modify_stat(stat, num, faces)

    def get_inv(self):
        return self.inventory

    def get_inv_item(self, name):
        for i in self.inventory:
            if self.inventory[i].name == name:
                return self.inventory[name]
        return -1

