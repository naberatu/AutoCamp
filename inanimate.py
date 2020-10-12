
from entity import Entity


class Inanimate(Entity):

    def __init__(self, name, id, isItem, max_stack=None):
        super().__init__(name, id)    # should inherit everything this way
        self.isItem = isItem

        if max_stack is not None:
            self.maxStack = max_stack
        else:
            self.maxStack = 1

        self.tileSize = 1
        self.visible = False

    def set_stack_size(self, size):
        self.maxStack = size

    def get_stack_size(self):
        return self.maxStack
