
from entity import Entity


class Inanimate(Entity):
    def __init__(self, name, entity_id, is_item, is_consumable, details=None, max_stack=None, weight=None, tile_size=None):
        super().__init__(name, entity_id)    # should inherit everything this way
        self.isItem = is_item
        self.details = details
        self.weight = weight
        self.quantity = 1
        self.consumable = is_consumable     # New consumable modifier.

        if tile_size is None:
            self.tile_size = 1
        else:
            self.tile_size = tile_size

        if max_stack is not None:
            self.maxStack = max_stack
        else:
            self.maxStack = 1

        self.visible = True

    # Accessors
    # ==================================
    def get_stack_size(self):
        return self.maxStack

    def get_quantity(self):
        return self.quantity

    def get_type(self):
        return self.itemType

    def get_weight(self):
        return self.weight

    def get_use(self):
        return self.details

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

    def mod_type(self, item_type):
        self.itemType = item_type

    def set_weight(self, value):
        self.weight = value

    def set_visibility(self, value):
        self.visible = value

    def change_use(self, string):
        self.details = string

    def use(self):
        if self.isItem:
            print("[OK] Usage: ", self.details)
            # if self.consumable:
                # Actually use the item
        else:
            print("[ER] This cannot be used!")
