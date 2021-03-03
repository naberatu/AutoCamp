
class Entity:
    def __init__(self, name, icon="./assets/item_drop.png"):
        self.name = name                # must have a name to be created
        self.coors = [0, 0, 0]       # done separately, since this refers to on-SCREEN appearance
        self.tileSize = 1
        self.icon = icon

    # Accessors
    # ==================================
    def get_name(self):
        return self.name

    def get_icon(self):
        return self.icon
    def get_tile_size(self):
        return self.tileSize

    def get_coors(self):
        return self.coors

    # Mutators
    # ==================================
    def set_name(self, value):
        self.name = value

    def set_tile_size(self, value):
        self.tileSize = value

    def set_coors(self, x=0, y=0, z=0):
        self.coors[0] = x
        self.coors[1] = y
        self.coors[2] = z


