
from entity import Entity
from statblock import StatBlock
import random


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
        self.inv_max = 20                       # maximum inventory capacity possible
        self.inv_scheme = "slot"                # whether the inventory stores by slot, item weight, or infinite
        self.is_enemy = None
        self.is_stealthy = False
        self.is_surprised = False

    # ==================================
    # Accessors
    # ==================================
    def get_stat_block(self):
        return self.stat_block

    def get_level(self):
        return self.level

    def get_role(self):
        return self.role

    def get_race(self):
        return self.race

    def get_stat(self, stat):
        return self.stat_block.get_stat(stat)

    def get_inv(self):
        return self.inventory

    def get_iff(self):
        return self.is_enemy

    def get_inv_max(self):
        return self.inv_max

    def get_inv_scheme(self):
        return self.inv_scheme

    def inv_is_full(self):
        # -------------------------------------------------------
        if self.inv_scheme == "slot":
            if len(self.inventory) == self.inv_max:
                return True
            else:
                return False
        # -------------------------------------------------------
        elif self.inv_scheme == "weight":
            if self.get_inv_size() >= self.inv_max:
                return True
            else:
                return False
        # -------------------------------------------------------
        elif self.inv_scheme is None:
            return False

    def get_inv_size(self):
        if self.inv_scheme == "slot":
            return len(self.inventory)
        elif self.inv_scheme == "weight":
            total_weight = 0
            for i in self.inventory:
                total_weight += i[0].get_weight * i[1]
            return total_weight
        else:
            print("[OK] Your inventory is infinite!")
            return -1

    def get_inv_item(self, item, notify=True):
        if item in self.inventory.keys():
            if notify:
                print("[OK] Aha, found it!")
            return item
        print("[ER] You don't have this item!")
        return None

    # ==================================
    # Mutators
    # ==================================
    def level_up(self):
        if self.level < 20:
            self.level += 1
            new_hp = random.randint(1, self.stat_block.get_stat("Hit Dice"))
            old_hp = self.stat_block.get_stat("Max HP")
            self.stat_block.modify_stat("Max HP", old_hp + new_hp)
            self.stat_block.modify_stat("Current HP", old_hp + new_hp)
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

    def set_stats(self, stat, num):
        self.stat_block.modify_stat(stat, num)

    def set_surprise(self, surprise_status):
        self.is_surprised = surprise_status

    def set_stealth(self, stealth_status):
        self.is_stealthy = stealth_status

    def set_iff(self, iff):
        self.is_enemy = iff

    def set_inv_scheme(self, scheme=None):
        if scheme == "slot" or scheme == "weight" or scheme is None:
            self.inv_scheme = scheme
        else:
            print("[ER] Invalid inventory scheme!")

    def set_inv_max_size(self, size):
        self.inv_max = size

    def inv_add(self, item, amount):
        if self.inv_is_full():
            print("[ER] Your inventory is full!")
        elif self.inv_scheme == "weight":
            added_weight = item.get_weight() * amount
            if self.get_inv_size() + added_weight <= self.inv_max:
                if item in self.inventory:
                    self.inventory[item] += amount
                else:
                    self.inventory[item] = amount
            else:
                print("[ER] It's too much to carry!")
        else:
            if item in self.inventory:
                self.inventory[item] += amount
            else:
                self.inventory[item] = amount

    def inv_remove(self, item, amount, discarding, selling, notify=True):
        if self.inventory == {}:
            print("[ER] You have nothing to give!")
            return None

        item = self.get_inv_item(item, notify)

        if item is None:
            print("[ER] You don't have that!")
            return None
        else:
            if selling:
                earnings = item.get_cost() * amount

            self.inventory[item] -= amount
            if self.inventory[item] <= 0:
                del self.inventory[item]
            if discarding:
                print("[OK] You have tossed away ", amount, " ", item.get_name(), "!")
            return item
