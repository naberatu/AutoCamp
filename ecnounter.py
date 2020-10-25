
from entity import Entity


class Encounter:
    def __init__(self):
        self.something = 0              # just a temporary value until we can establish this
        self.currentEntity = None

    def inv_use(self, entity_id):
        if len(self.currentEntity.get_inv()) == 0:
            print("[ER] You have nothing to give!")
        elif entity_id in self.currentEntity.get_inv():
            item_name = self.currentEntity.get_inv()[self.something].use()
            self.currentEntity.inv_remove(entity_id, False)
            print("[OK] You used ", item_name, "!")
        else:
            print("[ER] You don’t have that!")

    def inv_give(self, acceptor, entity_id):
        if len(self.currentEntity.get_inv()) == 0:
            print("[ER] You have nothing to give!")
        elif entity_id in self.currentEntity.get_inv():
            acceptor.inv_add(entity_id)
            self.currentEntity.inv_remove(entity_id, False)
            print("[OK] You gave", acceptor.get_name(), " ", entity_id, "!")
        else:
            print("[ER] You can’t give that!")

    def inv_equip(self, is_armor, entity_id):
        if entity_id in self.currentEntity.get_inv():
            item_class = None
            if is_armor:
                item_class = "armor"
                temp = self.currentEntity.get_armor()
                self.currentEntity.set_armor(entity_id)
                self.currentEntity.inv_remove(entity_id, False)
                self.currentEntity.inv_add(temp)
            elif not is_armor:
                item_class = "weapon"
                temp = self.currentEntity.get_weapon()
                self.currentEntity.set_weapon(entity_id)
                self.currentEntity.inv_remove(entity_id, False)
                self.currentEntity.inv_add(temp)
                print("[OK]: You have swapped your: ", item_class, "!")
            else:
                print("[ER]: It’s not in your inventory!")

