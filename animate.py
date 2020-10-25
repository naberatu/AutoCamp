
from entity import Entity
from statblock import StatBlock


class Animate(Entity):
    def __init__(self, name, entity_id, race, role, level, stat_block=None):
        super().__init__(name, entity_id)       # should inherit everything this way

        if stat_block is not None:
            self.stat_block = stat_block
        else:
            self.stat_block = StatBlock()       # empty stat block

        self.race = race
        self.role = role
        self.level = level
        self.inventory = dict()                 # Key is Item, Value is quantity.

    # Accessors
    # ==================================
    def get_level(self):
        return self.level

    def get_role(self):
        return self.role

    def get_race(self):
        return self.race

    def get_stat(self, stat):
        self.stat_block.get_stat(stat)

    def get_inv(self):
        return self.inventory

    def get_inv_item(self, name):
        for i in self.inventory:
            if i.name == name:
                print("[OK] Aha, found it!")
                return i

        print("[ER] You don't have this item!")

    def print_inv(self):
        print(self.name, "'s Inventory:\n")
        for i in self.inventory:
            print("\n| ", i.get_name(), "\t\t - x", i.get_quantity())

    # Mutators
    # ==================================
    def level_up(self):
        if self.level < 20:
            self.level += 1
            print("[OK] Level Updated to ", self.level, "!")
        else:
            print("[ER] Already at max level!")

    def mod_level(self, value):
        if (value > 0) and (value < 21):
            self.level = value
            print("[OK] Level Updated to ", value, "!")
        else:
            print("[ER] Invalid Level!")

    def mod_role(self, role):
        self.role = role

    def mod_race(self, race):
        self.race = race

    def set_stats(self, stat, num, faces=None):
        if faces is None:
            self.statBlock.modify_stat(stat, num)
        else:
            self.statBlock.modify_stat(stat, num, faces)

    def inv_add(self, *args, **kwargs):
        self.inventory.append(args)
        self.inventory.append(kwargs)

    def inv_remove(self, entity_id, discarding):
        for i in self.inventory:
            if i.get_id() == entity_id:
                try:
                    temp = i.get_name()
                    i.remove(i)
                    if discarding:
                        print("[OK] You have tossed away ", temp)
                    return
                except:
                    print("[ER] Where is that blasted thing?")
                    return





