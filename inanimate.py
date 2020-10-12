
from entity import Entity


class Inanimate(Entity):
    def __init__(self, name, id, isItem, max_stack=None):
        super().__init__(name, id)    # should inherit everything this way
        self.isItem = isItem

        if isItem:
            self.itemType = "item"
        else:
            self.itemType = "prop"

        if max_stack is not None:
            self.maxStack = max_stack
        else:
            self.maxStack = 1

        self.tileSize = 1
        self.visible = False

    # Accessors
    # ==================================
    def set_stack_size(self, size):
        self.maxStack = size

    def get_type(self):
        return self.itemType

    # Mutators
    # ==================================
    def get_stack_size(self):
        return self.maxStack

    def mod_type(self, item_type):
        self.itemType = item_type

