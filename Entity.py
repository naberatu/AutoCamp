import base64

class Entity():

    def __init__(self, name, weight, tileSize, stackSize):
        self.name = name
        self.weight = weight
        self.tileSize = tileSize
        self.stackSize = stackSize
        coors = (0, 0, 0)

        # Code about storing images
            # with open("null.png", "rb") as imageFile:
            #     thumbnail = base64.b64encode(file.read())
            #
            # thumbnail = Image.open(io.BytesIO(thumbnail))
            # thumbnail.show()

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_tile_size(self):
        return self.tileSize

    def get_stack_size(self):
        return self.stackSize


