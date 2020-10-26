
from entity import Entity


class Encounter:
    def __init__(self):
        self.something = 0              # just a temporary value until we can establish this
        self.currentEntity = None

    def inv_use(self, item_id, inv):        # pass in self.currentEntity.get_inv()
        item = inv.inv_remove(item_id, False)
        if item is not None:
            print("[OK] You used ", item.get_name(), "!")

    def inv_give(self, acceptor, item_id, inv):
        item = inv.get_inv_item(item_id)
        if item is not None and not acceptor.is_enemy():
            inv.inv_remove(item_id, False)
            acceptor.inv_add(item)
            print("[OK] You gave", acceptor.get_name(), " ", item.get_name(), "!")
        elif item is not None and acceptor.is_enemy():
            print("[ER] You can’t give that to ", acceptor.get_name(), "!")

    def inv_equip(self, is_armor, item_id, inv):
        item = inv.inv_remove(item_id, False)
        if is_armor:
            armor = self.currentEntity.get_armor()
            self.currentEntity.inv_add(armor)
            self.currentEntity.set_armor(item)
            print("[OK]: You have swapped your armor!")
        else:
            weapon = self.currentEntity.get_weapon()
            self.currentEntity.inv_add(weapon)
            self.currentEntity.set_armor(item)
            print("[OK]: You have swapped your weapon!")
