#
# from inanimate import Inanimate
# import pickle
#
#
# class Items:
#     def __init__(self):
#         self.c_items = dict()
#         self.custom = dict()
#
#         try:
#             self.c_items = pickle.load(open("items_main.camp", "rb"))
#         except:
#             # Simple Weapons
#             self.c_items["Iron Sword"] = Inanimate("Iron Sword", 0, 1, 20, "An Iron Sword", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Club"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Dagger"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["GreatClub"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Handaxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Javelin"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Light Hammer"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Mace"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Quarterstaff"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Sickle"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Spear"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#
#             # Martial Melee Weapons
#             self.c_items["Battleaxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Flail"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Glaive"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Greataxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Greatsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Halberd"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Lance"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Longsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Maul"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Morningstar"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Pike"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Rapier"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Scimitar"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Shortsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Trident"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["War Pick"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Warhammer"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Whip"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#
#             # Ranged Weapons
#             self.c_items["Crossbow (Light)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Dart"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Shortbow"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Sling"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#
#             # Martial Ranged Weapons
#             self.c_items["Blowgun"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Crossbow (Hand)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Crossbow (Heavy)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Longbow"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.c_items["Net"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#
#             # Armor
#             self.c_items["Padded Armor"] = Inanimate("Padded Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(11, "dexterity", True)
#             self.c_items["Leather Armor"] = Inanimate("Leather Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(11, "dexterity")
#             self.c_items["Studded Leather Armor"] = Inanimate("Studded Leather Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(12, "dexterity")
#             self.c_items["Hide Armor"] = Inanimate("Hide Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(12, "dexterity")
#             self.c_items["Chain Shirt"] = Inanimate("Chain Shirt", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(13, "dexterity")
#             self.c_items["Scale Mail"] = Inanimate("Scale Mail", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(14, "dexterity", True)
#             self.c_items["Breastplate"] = Inanimate("Breastplate", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(14, "dexterity")
#             self.c_items["Half Plate"] = Inanimate("Half Plate", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(15, "dexterity", True)
#             self.c_items["Ring Mail"] = Inanimate("Ring Mail", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(14, None, True)
#             self.c_items["Chain Mail"] = Inanimate("Chain Mail", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(16, None, True)
#             self.c_items["Splint Armor"] = Inanimate("Splint Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(17, None, True)
#             self.c_items["Plate Armor"] = Inanimate("Plate Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(18, None, True)
#
#             # Consumables
#             self.c_items["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#             self.c_items["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#             self.c_items["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#             self.c_items["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#             self.c_items["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#
#             pickle.dump(self.c_items, open("items_main.camp", "wb"))
#
#         try:
#             self.custom = pickle.load(open("items_custom.camp", "rb"))
#         except: pass
#
#     # end init
#
#     def get_item(self, name, is_custom=False):
#         if is_custom:
#             return self.custom.get(name)
#         else:
#             return self.c_items.get(name)
#
#     def add_item(self, item_type, is_custom=False):
#
#         if is_custom:
#             pickle.dump(self.custom, open("items_custom.camp", "wb"))
#         else:
#             pickle.dump(self.c_items, open("items_main.camp", "wb"))
#
#     def get_catalog(self):
#         return self.c_items
#
#     def get_custom(self):
#         return self.custom
