
class Entity:
    def __init__(self, name, id):
        self.name = name                # must have a name to be created
        self.id = id                    # internal id
        self.coors = [-1, -1, -1]       # coordinates that do not appear on screen
        self.thumbnail = 0              # eventually replaced by actual file

    # Accessors
    # ==================================
    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_coors(self):
        return self.coors

    def get_thumbnail(self):
        return self.thumbnail

    # Mutators
    # ==================================
    def set_name(self, value):
        self.name = value

    def set_id(self, value):
        self.id = value

    def set_thumbnail(self, image):
        self.thumbnail = image

    def set_coors(self, x=None, y=None, z=None):
        if x is not None:
            self.coors[0] = x
        if y is not None:
            self.coors[1] = y
        if z is not None:
            self.coors[2] = z

