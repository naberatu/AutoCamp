
from entity import Entity

class Inanimate(Entity):

    def __init__(self, name, id, isItem, maxStack=None):
        super().__init__(name, id)    # should inherit everything this way
        self.isItem = isItem

        if maxStack is not None:
            self.maxStack = maxStack
        else:
            self.maxStack = 1

        self.tileSize = 1

    def set_stack_size(self, size):
        self.maxStack = size

    def get_stack_size(self):
        return self.maxStack
