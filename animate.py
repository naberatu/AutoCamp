
from entity import Entity
from statblock import StatBlock


class Animate(Entity):

    def __init__(self, name, hero_id):
        super().__init__(name, hero_id)    # should inherit everything this way
        self.statBlock = StatBlock()  # empty stat block
        self.inventory = list()

    # Accessors
    # ==================================
    def get_stat(self, stat):
        self.statBlock.get_stat(stat)

    def get_inv(self):
        return self.inventory

    def get_inv_item(self, name):
        for i in self.inventory:
            if self.inventory[i].name == name:
                return self.inventory[name]
        return -1

    # Mutators
    # ==================================
    def set_stats(self, stat, num, faces=None):
        if faces is None:
            self.statBlock.modify_stat(stat, num)
        else:
            self.statBlock.modify_stat(stat, num, faces)

    def inv_add(self, *args, **kwargs):
        self.inventory.append(args)
        self.inventory.append(kwargs)

    def inv_remove(self, hero_id, discarding):
        for i in self.inventory:
            if self.inventory[i].get_id() == hero_id:
                try:
                    temp = self.inventory[i].get_name()
                    self.inventory.remove(self.inventory[i])
                    if discarding:
                        print("[OK] You have tossed away ", temp)
                    return
                except:
                    print("[ER] Where is that blasted thing?")
                    return





