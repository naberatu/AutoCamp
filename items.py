
from inanimate import Inanimate
import pickle


catalog = dict()
custom = dict()

try:
    catalog = pickle.load(open("items_main.camp", "rb"))
except:
    # Simple Weapons
    catalog["Shortsword"] = Inanimate("Shortsword", item_code=1, cost=15, details="A steel shortsword.", weight=2, alpha=1, beta=6, gamma="piercing")
    catalog["Club"] = Inanimate("Club", item_code=1, cost=1, details="A wooden club.", weight=2, alpha=1, beta=4, gamma="bludgeoning")
    catalog["Dagger"] = Inanimate("Dagger", item_code=1, cost=2, details="An iron dagger.", weight=1, alpha=1, beta=4, gamma="piercing")
    catalog["Greatclub"] = Inanimate("Greatclub", item_code=1, cost=2, details="A massive club.", weight=10, alpha=1, beta=8, gamma="bludgeoning")
    catalog["Handaxe"] = Inanimate("Handaxe", item_code=1, cost=5, details="A simple handaxe.", weight=2, alpha=1, beta=6, gamma="slashing")
    catalog["Javelin"] = Inanimate("Javelin", item_code=1, cost=5, details="A sturdy javelin.", weight=2, alpha=1, beta=6, gamma="slashing")
    catalog["Light Hammer"] = Inanimate("Light Hammer", item_code=1, cost=2, details="A smaller, lighter hammer.", weight=2, alpha=1, beta=4, gamma="bludgeoning")
    catalog["Mace"] = Inanimate("Mace", item_code=1, cost=5, details="A weapon with a bladed head.", weight=4, alpha=1, beta=6, gamma="bludgeoning")
    catalog["Quarterstaff"] = Inanimate("Quarterstaff", item_code=1, cost=2, details="A light and powerful staff.", weight=4, alpha=1, beta=6, gamma="bludgeoning")
    catalog["Sickle"] = Inanimate("Sickle", item_code=1, cost=1, details="A sharp sickle.", weight=2, alpha=1, beta=6, gamma="slashing")
    catalog["Spear"] = Inanimate("Spear", item_code=1, cost=1, details="A sharpened spear.", weight=3, alpha=1, beta=6, gamma="piercing")


    # Martial Melee Weapons
    # catalog["Battleaxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # catalog["Flail"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # catalog["Glaive"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # catalog["Greataxe"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # catalog["Greatsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # catalog["Halberd"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # catalog["Lance"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # catalog["Longsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # catalog["Maul"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # catalog["Morningstar"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Pike"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Rapier"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Scimitar"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Shortsword"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Trident"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["War Pick"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Warhammer"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Whip"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    #
    # # Ranged Weapons
    # catalog["Crossbow (Light)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Dart"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Shortbow"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Sling"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    #
    # # Martial Ranged Weapons
    # catalog["Blowgun"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Crossbow (Hand)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Crossbow (Heavy)"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Longbow"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")
    # catalog["Net"] = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4).set_properties(1, 6, "slashing")

    # Armor
    catalog["Padded Armor"] = Inanimate("Padded Armor", item_code=2, cost=5, details="Provides +11 AC", weight=8, alpha=11, beta="dexterity", gamma=True)
    catalog["Leather Armor"] = Inanimate("Leather Armor", item_code=2, cost=10, details="Provides +11 AC", weight=10, alpha=11, beta="dexterity")
    catalog["Studded Leather Armor"] = Inanimate("Studded Leather Armor", item_code=2, cost=45, details="Provides +12 AC", weight=13,alpha=12, beta="dexterity")
    catalog["Hide Armor"] = Inanimate("Hide Armor", item_code=2, cost=10, details="Provides +12 AC", weight=12, alpha=12, beta="dexterity")
    catalog["Chain Shirt"] = Inanimate("Chain Shirt", item_code=2, cost=50, details="Provides +13 AC", weight=20, alpha=13, beta="dexterity")
    catalog["Scale Mail"] = Inanimate("Scale Mail", item_code=2, cost=50, details="Provides +14 AC", weight=45, alpha=14, beta="dexterity", gamma=True)
    catalog["Breastplate"] = Inanimate("Breastplate", item_code=2, cost=400, details="Provides +14 AC", weight=20, alpha=14, beta="dexterity")
    catalog["Half Plate"] = Inanimate("Half Plate", item_code=2, cost=750, details="Provides +15 AC", weight=40, alpha=15, beta="dexterity", gamma=True)
    catalog["Ring Mail"] = Inanimate("Ring Mail", item_code=2, cost=30, details="Provides +14 AC", weight=40, alpha=14, beta=None, gamma=True)
    catalog["Chain Mail"] = Inanimate("Chain Mail", item_code=2, cost=75, details="Provides +16 AC", weight=55, alpha=16, beta=None, gamma=True)
    catalog["Splint Armor"] = Inanimate("Splint Armor", item_code=2, cost=200, details="Provides +17 AC", weight=60, alpha=17, beta=None, gamma=True)
    catalog["Plate Armor"] = Inanimate("Plate Armor", item_code=2, cost=1500, details="Provides +18 AC", weight=65, alpha=18, beta=None, gamma=True)

    # Consumables
    catalog["Mana Potion"] = Inanimate("Mana Potion", item_code=3, cost=30, details="Restores Mana", max_stack=6, weight=0.5, alpha="medicine", beta=1.0)
    # catalog["Mana Potion"] = Inanimate("Mana Potion", item_code=3, cost=30, details="Restores Mana", max_stack=6, weight=0.5, alpha="medicine", beta=1.0)

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
