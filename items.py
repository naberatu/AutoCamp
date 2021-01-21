
from inanimate import Inanimate
import pickle


catalog = dict()
custom = dict()

try:
    catalog = pickle.load(open("items_main.camp", "rb"))
except:
    # Simple Weapons
    catalog["Iron Sword"] = Inanimate("Iron Sword", 0, 1, 20, "An Iron Sword", 1, 4).set_properties(1, 6, "slashing")
    catalog["Club"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Dagger"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["GreatClub"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Handaxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Javelin"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Light Hammer"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Mace"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Quarterstaff"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Sickle"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Spear"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # Martial Melee Weapons
    catalog["Battleaxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Flail"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Glaive"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Greataxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Greatsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Halberd"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Lance"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Longsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Maul"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Morningstar"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Pike"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Rapier"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Scimitar"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Shortsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Trident"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["War Pick"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Warhammer"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Whip"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # Ranged Weapons
    catalog["Crossbow (Light)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Dart"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Shortbow"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Sling"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # Martial Ranged Weapons
    catalog["Blowgun"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Crossbow (Hand)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Crossbow (Heavy)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Longbow"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    catalog["Net"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # Armor
    catalog["Padded Armor"] = Inanimate("Padded Armor", 1, 2, 20, "Provides +11 AC", 1, 6).set_properties(11, "dexterity", True)
    catalog["Leather Armor"] = Inanimate("Leather Armor", 1, 2, 20, "Provides +11 AC", 1, 6).set_properties(11, "dexterity")
    catalog["Studded Leather Armor"] = Inanimate("Studded Leather Armor", 1, 2, 20, "Provides +12 AC", 1, 6).set_properties(12, "dexterity")
    catalog["Hide Armor"] = Inanimate("Hide Armor", 1, 2, 20, "Provides +12 AC", 1, 6).set_properties(12, "dexterity")
    catalog["Chain Shirt"] = Inanimate("Chain Shirt", 1, 2, 20, "Provides +13 AC", 1, 6).set_properties(13, "dexterity")
    catalog["Scale Mail"] = Inanimate("Scale Mail", 1, 2, 20, "Provides +14 AC", 1, 6).set_properties(14, "dexterity", True)
    catalog["Breastplate"] = Inanimate("Breastplate", 1, 2, 20, "Provides +14 AC", 1, 6).set_properties(14, "dexterity")
    catalog["Half Plate"] = Inanimate("Half Plate", 1, 2, 20, "Provides +15 AC", 1, 6).set_properties(15, "dexterity", True)
    catalog["Ring Mail"] = Inanimate("Ring Mail", 1, 2, 20, "Provides +14 AC", 1, 6).set_properties(14, None, True)
    catalog["Chain Mail"] = Inanimate("Chain Mail", 1, 2, 20, "Provides +16 AC", 1, 6).set_properties(16, None, True)
    catalog["Splint Armor"] = Inanimate("Splint Armor", 1, 2, 20, "Provides +17 AC", 1, 6).set_properties(17, None, True)
    catalog["Plate Armor"] = Inanimate("Plate Armor", 1, 2, 20, "Provides +18 AC", 1, 6).set_properties(18, None, True)

    # Consumables
    catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
    # catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
    # catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
    # catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)
    # catalog["Mana Potion"] = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)

    pickle.dump(catalog, open("items_main.camp", "wb"))

try:
    custom = pickle.load(open("items_custom.camp", "rb"))
except: pass


def get_item(self, name, is_custom=False):
    if is_custom:
        return custom.get(name)
    else:
        return catalog.get(name)


def add_item(self, item_type, is_custom=False):

    if is_custom:
        pickle.dump(custom, open("items_custom.camp", "wb"))
    else:
        pickle.dump(catalog, open("items_main.camp", "wb"))
