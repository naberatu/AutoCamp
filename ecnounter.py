
from entity import Entity


class Encounter:
    def __init__(self):
        self.something = 0
        self.currentEntity = None
        self.acceptor = None

    def inv_use(self, hero_id):
        if len(self.currentEntity.get_inv()) == 0:
            print("[ER] You have nothing to give!")
        elif id in self.currentEntity.get_inv():
            self.currentEntity.get_inv()[self.something].use()
            self.currentEntity.inv_remove(id)
            print("[OK] You gave", self.acceptor.get_name(), " ", id, "!")
        else:
            print("[ER] You don’t have that!")

    def inv_give(self, acceptor, hero_id):
        if len(self.currentEntity.get_inv()) == 0:
            print("[ER] You have nothing to give!")
        elif id in self.currentEntity.get_inv():
            self.acceptor.inv_add(id)
            self.currentEntity.inv_remove(id)
            print("[OK] You gave", acceptor.get_name(), " ", id, "!")
        else:
            print("[ER] You can’t give that!")

    def inv_equip(self, is_armor, hero_id):
        if id in self.currentEntity.get_inv():
            item_class = None
            if is_armor:
                item_class = "armor"
                temp = self.currentEntity.get_armor()
                self.currentEntity.set_armor(id)
                self.currentEntity.inv_remove(id)
                self.currentEntity.inv_add(temp)
            elif not is_armor:
                item_class = "weapon"
                temp = self.currentEntity.get_weapon()
                self.currentEntity.set_weapon(id)
                self.currentEntity.inv_remove(id)
                self.currentEntity.inv_add(temp)
                print("[OK]: You have swapped your: ", item_class, "!")
            else:
                print("[ER]: It’s not in your inventory!")

