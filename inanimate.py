
from entity import Entity


class Inanimate(Entity):
    def __init__(self, name, entity_id, item_code, cost=None, details=None, max_stack=None, weight=None, tile_size=None):
        super().__init__(name, entity_id)    # should inherit everything this way

        self.item_type = item_code
        self.details = details
        self.weight = weight
        self.quantity = 1
        self.cost = cost
        self.properties = None
        self.visible = True

        # Added Features:
        # =========================
        if self.item_type == 0:
            self.is_prop = True
        elif self.item_type == 1:
            self.is_weapon = True
            self.properties = {"damage": 0,
                               "damage_type": None,
                               "modifier": None}
        elif self.item_type == 2:
            self.is_armor = True
            self.properties = {"armor_class": 0,
                               "modifier": None,
                               "stealth": True}
        elif self.item_type == 3:
            self.is_consumable = True
            self.properties = {"type": "healing",
                               "strength": None}
        else:
            self.is_prop, self.is_weapon, self.is_armor, self.is_consumable = False
            # this means it's a standard item, like a ring, or book, or something.
        # =========================

        if tile_size is None:
            self.tile_size = 1
        else:
            self.tile_size = tile_size

        if max_stack is None:
            self.maxStack = 1
        else:
            self.maxStack = max_stack

    # Accessors
    # ==================================
    def get_stack_size(self):
        return self.maxStack

    def get_quantity(self):
        return self.quantity

    def get_weight(self):
        return self.weight

    def get_cost(self):
        return self.cost

    def get_use(self):
        return self.details

    def get_property(self, name):
        if self.properties.keys().__contains__(name):
            return self.properties[name]
        else:
            print("[ER] This item does not have that property!")
            return None

    def check_visibility(self):
        return self.visible

    # Mutators
    # ==================================
    def set_stack_size(self, size):
        self.maxStack = size

    def set_quantity(self, amount):
        self.quantity = amount

    def acquire_one(self):
        self.quantity += 1

    def set_weight(self, value):
        self.weight = value

    def set_visibility(self, value):
        self.visible = value

    def change_use(self, string):
        self.details = string

    def set_cost(self, value):
        self.cost = value

    def set_property(self, name, value):
        if self.properties.keys().__contains__(name):
            self.propertiesp[name] = value
        else:
            print("[ER] This item does not have that property!")

    def use(self):
        if self.item_type:
            print("[OK] Usage: ", self.details)
            # if self.consumable:
                # Actually use the item
        else:
            print("[ER] This cannot be used!")
