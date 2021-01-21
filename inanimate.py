
from entity import Entity


class Inanimate(Entity):
    def __init__(self, name, entity_id, item_code, cost=1, details="This is an item.", max_stack=1, weight=1, tile_size=1):
        super().__init__(name, entity_id)    # should inherit everything this way

        self.details = details
        self.weight = weight
        self.quantity = 1
        self.cost = cost
        self.properties = None
        self.visible = True
        self.is_prop = False
        self.is_weapon = False
        self.is_armor = False
        self.is_consumable = False

        if item_code == 0:
            self.is_prop = True
        elif item_code == 1:
            self.is_weapon = True
            self.properties = {"dmg_dice": 1,
                               "dmg_sides": 4,
                               "dmg_type": None }
        elif item_code == 2:
            self.is_armor = True
            self.properties = {"armor_class": 0,
                               "modifier": None,
                               "stealth_dis": False }
        elif item_code == 3:
            self.is_consumable = True
            self.properties = {"type": "healing",
                               "strength": 1}

        self.tile_size = tile_size
        self.maxStack = max_stack

    # Accessors
    # ==================================
    def get_stack_size(self):
        return self.maxStack

    def get_quantity(self):
        return self.quantity

    def get_weight(self):
        return self.weight

    def get_cost(self):
        return self.cost

    def get_use(self):
        return self.details

    def get_is_weapon(self):
        return self.is_weapon

    def get_is_armor(self):
        return self.is_armor

    def get_property(self, name):
        if self.properties.keys().__contains__(name):
            return self.properties[name]
        else:
            print("[ER] This item does not have that property!")
            return None

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

    def set_weight(self, value):
        self.weight = value

    def set_visibility(self, value):
        self.visible = value

    def change_use(self, string):
        self.details = string

    def set_cost(self, value):
        self.cost = value

    def set_properties(self, *args):
        if len(args) == 3 and self.is_weapon:
            self.properties["dmg_dice"] = args[0]
            self.properties["dmg_sides"] = args[1]
            self.properties["dmg_type"] = args[2]
        elif len(args) >= 2 and self.is_armor:
            self.properties["armor_class"] = args[0]
            self.properties["modifier"] = args[1]
            try:
                self.properties["stealth_dis"] = args[2]
            except:
                self.properties["stealth_dis"] = False
        elif len(args) == 2 and self.is_consumable:
            self.properties["type"] = args[0]
            self.properties["strength"] = args[1]
        else:
            print("[ER] Invalid inputs to properties.")

    def set_property(self, name, value):
        if self.properties.keys().__contains__(name):
            self.properties[name] = value
        else:
            print("[ER] This item does not have that property!")

    # def use(self):
    #     if self.item_type:
    #         print("[OK] Usage: ", self.details)
    #         if self.consumable:
    #             Actually use the item
        # else:
        #     print("[ER] This cannot be used!")
