
class Entity:
    def __init__(self, name, entity_id):
        self.name = name                # must have a name to be created
        self.entity_id = entity_id
        self.coors = [1, 1, 1]       # done separately, since this refers to on-screen appearance
        self.tileSize = 1

    # Accessors
    # ==================================
    def get_name(self):
        return self.name

    def get_tile_size(self):
        return self.tileSize

    def get_coors(self):
        return self.coors

    def get_id(self):
        return self.entity_id

    # Mutators
    # ==================================
    def set_name(self, value):
        self.name = value

    def set_tile_size(self, value):
        self.tileSize = value

    def set_coors(self, x=1, y=1, z=1):
        self.coors[0] = x
        self.coors[1] = y
        self.coors[2] = z

    def set_id(self, new_id):
        self.entity_id = new_id
