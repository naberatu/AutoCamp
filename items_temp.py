#
# from inanimate import Inanimate
# import pickle
#
#
# class Items:
#     def __init__(self):
#         self.catalog = dict()
#         self.custom = dict()
#
#         try:
#             self.catalog = pickle.load(open("items_main.camp", "rb"))
#         except:
#             # Simple Weapons
#             self.catalog["Iron Sword"] = Inanimate("Iron Sword", 0, 1, 20, "An Iron Sword", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Club"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Dagger"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["GreatClub"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Handaxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Javelin"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Light Hammer"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Mace"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Quarterstaff"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Sickle"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Spear"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#
#             # Martial Melee Weapons
#             self.catalog["Battleaxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Flail"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Glaive"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Greataxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Greatsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Halberd"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Lance"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Longsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Maul"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Morningstar"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Pike"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Rapier"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Scimitar"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Shortsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Trident"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["War Pick"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Warhammer"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Whip"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#
#             # Ranged Weapons
#             self.catalog["Crossbow (Light)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Dart"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Shortbow"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Sling"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#
#             # Martial Ranged Weapons
#             self.catalog["Blowgun"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Crossbow (Hand)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Crossbow (Heavy)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Longbow"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#             self.catalog["Net"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
#
#             # Armor
#             self.catalog["Padded Armor"] = Inanimate("Padded Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(11, "dexterity", True)
#             self.catalog["Leather Armor"] = Inanimate("Leather Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(11, "dexterity")
#             self.catalog["Studded Leather Armor"] = Inanimate("Studded Leather Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(12, "dexterity")
#             self.catalog["Hide Armor"] = Inanimate("Hide Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(12, "dexterity")
#             self.catalog["Chain Shirt"] = Inanimate("Chain Shirt", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(13, "dexterity")
#             self.catalog["Scale Mail"] = Inanimate("Scale Mail", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(14, "dexterity", True)
#             self.catalog["Breastplate"] = Inanimate("Breastplate", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(14, "dexterity")
#             self.catalog["Half Plate"] = Inanimate("Half Plate", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(15, "dexterity", True)
#             self.catalog["Ring Mail"] = Inanimate("Ring Mail", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(14, None, True)
#             self.catalog["Chain Mail"] = Inanimate("Chain Mail", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(16, None, True)
#             self.catalog["Splint Armor"] = Inanimate("Splint Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(17, None, True)
#             self.catalog["Plate Armor"] = Inanimate("Plate Armor", 1, 2, 20, "Provides +10 AC", 1, 6).set_properties(18, None, True)
#
#             # Consumables
#             self.catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#             self.catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#             self.catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#             self.catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#             self.catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
#
#             pickle.dump(self.catalog, open("items_main.camp", "wb"))
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
#             return self.catalog.get(name)
#
#     def add_item(self, item_type, is_custom=False):
#
#         if is_custom:
#             pickle.dump(self.custom, open("items_custom.camp", "wb"))
#         else:
#             pickle.dump(self.catalog, open("items_main.camp", "wb"))
#
#     def get_catalog(self):
#         return self.catalog
#
#     def get_custom(self):
#         return self.custom
