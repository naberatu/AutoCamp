import pygame


class Entity:
    def __init__(self, name, weight=None, tile_size=None, stack_size=None):

        self.name = name                # must have a name to be created
        self.coors = [-1, -1, -1]       # done separately, since this refers to on-screen appearance

        if weight is not None:
            self.weight = weight
        if tile_size is not None:
            self.tileSize = tile_size
        if stack_size is not None:
            self.stackSize = stack_size

    # Accessors
    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_tile_size(self):
        return self.tileSize

    def get_stack_size(self):
        return self.stackSize

    def get_coors(self):
        return self.coors

    # Mutators
    def set_name(self, value):
        self.name = value

    def set_weight(self, value):
        self.weight = value

    def set_tile_size(self, value):
        self.tileSize = value

    def set_stack_size(self, value):
        self.stackSize = value

    def set_coors(self, x=None, y=None, z=None):
        if x is not None:
            self.coors[0] = x
        if y is not None:
            self.coors[1] = y
        if z is not None:
            self.coors[2] = z
