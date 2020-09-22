class Entity():

    def __init__(self, name, weight=None, tileSize=None, stackSize=None):

        self.name = name
        self.coors = [-1, -1, -1]

        if weight is not None:
            self.weight = weight
        if tileSize is not None:
            self.tileSize = tileSize
        if stackSize is not None:
            self.stackSize = stackSize

        # Code about storing images
            # with open("null.png", "rb") as imageFile:
            #     thumbnail = base64.b64encode(file.read())
            #
            # thumbnail = Image.open(io.BytesIO(thumbnail))
            # thumbnail.show()

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
            self.coors = (x)



