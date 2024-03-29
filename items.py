
from inanimate import Inanimate
import pickle


c_items = dict()
custom = dict()

try:
    c_items = pickle.load(open("items_main.camp", "rb"))
except:

    # Weapons ==========================================================================================================
    # # Simple Melee Weapons
    c_items["Club"] = Inanimate("Club", item_code=1, cost=10, details="A wooden club. {Light}", weight=2, alpha=1, beta=4, gamma="bludgeoning", delta=0)
    c_items["Dagger"] = Inanimate("Dagger", item_code=1, cost=200, details="An iron dagger. {Finesse, light, thrown (range 20/60)}", weight=1, alpha=1, beta=4, gamma="piercing", delta=0)
    c_items["Greatclub"] = Inanimate("Greatclub", item_code=1, cost=20, details="A massive club. {Two-handed}", weight=10, alpha=1, beta=8, gamma="bludgeoning", delta=0)
    c_items["Handaxe"] = Inanimate("Handaxe", item_code=1, cost=500, details="A simple handaxe. {Light, thrown (range 20/60)}", weight=2, alpha=1, beta=6, gamma="slashing", delta=0)
    c_items["Javelin"] = Inanimate("Javelin", item_code=1, cost=50, details="A sturdy javelin. {Thrown (range 30/120)}", weight=2, alpha=1, beta=6, gamma="slashing", delta=0)
    c_items["Light Hammer"] = Inanimate("Light Hammer", item_code=1, cost=200, details="A smaller, lighter hammer. {Light, thrown (range 20/60)}", weight=2, alpha=1, beta=4, gamma="bludgeoning", delta=0)
    c_items["Mace"] = Inanimate("Mace", item_code=1, cost=5, details="A weapon with a bladed head.", weight=4, alpha=1, beta=6, gamma="bludgeoning", delta=0)
    c_items["Quarterstaff"] = Inanimate("Quarterstaff", item_code=1, cost=200, details="A light and powerful staff. {Versatile (1d8)}", weight=4, alpha=1, beta=6, gamma="bludgeoning", delta=0)
    c_items["Sickle"] = Inanimate("Sickle", item_code=1, cost=100, details="A sharp sickle. {Light}", weight=2, alpha=1, beta=6, gamma="slashing", delta=0)
    c_items["Spear"] = Inanimate("Spear", item_code=1, cost=100, details="A sharpened spear. {Thrown (range 20/60), versatile (1d8)}", weight=3, alpha=1, beta=6, gamma="piercing", delta=0)

    # # Simple Ranged Weapons
    c_items["Crossbow (Light)"] = Inanimate("Crossbow (Light)", item_code=1, cost=2500, details="A light-weight crossbow. {Ammunition (range 80/320), loading, two-handed}", weight=5, alpha=1, beta=8, gamma="piercing", delta=1)
    c_items["Dart"] = Inanimate("Dart", item_code=1, cost=5, details="A small, pointed projectile. {Finesse, thrown (range 20/60)}", weight=.25, alpha=1, beta=4, gamma="piercing", delta=1)
    c_items["Shortbow"] = Inanimate("Shortbow", item_code=1, cost=2500, details="A smaller arrow-shooter. {Ammunition (range 80/320), two-handed}", weight=2, alpha=1, beta=6, gamma="piercing", delta=1)
    c_items["Sling"] = Inanimate("Sling", item_code=1, cost=10, details="A forked stick with a leather strap. {Ammunition (range 30/120)}", weight=0, alpha=1, beta=4, gamma="bludgeoning", delta=1)

    # # Martial Melee Weapons
    c_items["Battleaxe"] = Inanimate("Battleaxe", item_code=1, cost=1000, details="An axe, ready for battle. {Versatile (1d10)}", weight=4, alpha=1, beta=8, gamma="slashing", delta=0)
    c_items["Flail"] = Inanimate("Flail", item_code=1, cost=1000, details="A wooden staff with a short heavy stick swinging from it.", weight=2, alpha=1, beta=8, gamma="bludgeoning", delta=0)
    c_items["Glaive"] = Inanimate("Glaive", item_code=1, cost=2000, details="A sword. {Heavy, reach, two-handed}", weight=6, alpha=1, beta=10, gamma="slashing", delta=0)
    c_items["Greataxe"] = Inanimate("Greataxe", item_code=1, cost=3000, details="A large, heavy battleaxe with a double-bladed head. {Heavy, two-handed}", weight=7, alpha=1, beta=12, gamma="slashing", delta=0)
    c_items["Greatsword"] = Inanimate("Greatsword", item_code=1, cost=5000, details="A massive, two-handed Medieval sword. {Heavy, two-handed}", weight=6, alpha=2, beta=6, gamma="slashing", delta=0)
    c_items["Halberd"] = Inanimate("Halberd", item_code=1, cost=2000, details="A combined spear and battleaxe. {Heavy, reach, two-handed}", weight=6, alpha=1, beta=10, gamma="slashing", delta=0)
    c_items["Lance"] = Inanimate("Lance", item_code=1, cost=1000, details="A long weapon for thrusting, having a wooden shaft and a pointed steel head. {Reach, special}", weight=6, alpha=1, beta=12, gamma="piercing", delta=0)
    c_items["Longsword"] = Inanimate("Longsword", item_code=1, cost=1500, details="A straight double-edged blade. {Versatile (1d10)}", weight=3, alpha=1, beta=8, gamma="slashing", delta=0)
    c_items["Maul"] = Inanimate("Maul", item_code=1, cost=1000, details="A heavy wooden-headed hammer. {Heavy, two-handed}", weight=10, alpha=2, beta=6, gamma="bludgeoning", delta=0)
    c_items["Morningstar"] = Inanimate("Morningstar", item_code=1, cost=1500, details="A club with a heavy spiked head.", weight=4, alpha=1, beta=8, gamma="piercing", delta=0)
    c_items["Pike"] = Inanimate("Pike", item_code=1, cost=500, details="A long wooden shaft with a pointed metal head. {Heavy, reach, two-handed}", weight=18, alpha=1, beta=10, gamma="piercing", delta=0)
    c_items["Rapier"] = Inanimate("Rapier", item_code=1, cost=2500, details="A thin, light sharp-pointed sword used for thrusting. {Finesse}", weight=2, alpha=1, beta=8, gamma="piercing", delta=0)
    c_items["Scimitar"] = Inanimate("Scimitar", item_code=1, cost=2500, details="A short sword with a curved blade that broadens toward the point. {Finesse, light}", weight=3, alpha=1, beta=6, gamma="slashing", delta=0)
    c_items["Shortsword"] = Inanimate("Shortsword", item_code=1, cost=1000, details="A steel shortsword. {Finesse, light}", weight=2, alpha=1, beta=6, gamma="piercing", delta=0)
    c_items["Trident"] = Inanimate("Trident", item_code=1, cost=500, details="A three-pronged spear. {Thrown (range 20/60), versatile (1d8)}", weight=4, alpha=1, beta=6, gamma="piercing", delta=0)
    c_items["War Pick"] = Inanimate("War Pick", item_code=1, cost=500, details="A war hammer with a very long spike on the reverse of the hammer head.", weight=2, alpha=1, beta=8, gamma="piercing", delta=0)
    c_items["Warhammer"] = Inanimate("Warhammer", item_code=1, cost=1500, details="A long-handled metal hammer. {Versatile (1d10)}", weight=2, alpha=1, beta=8, gamma="bludgeoning", delta=0)
    c_items["Whip"] = Inanimate("Whip", item_code=1, cost=200, details="A strip of leather fastened to a handle. {Finesse, reach}", weight=3, alpha=1, beta=4, gamma="slashing", delta=0)

    # # Martial Ranged Weapons
    # For the blowgun, does 1 piercing dmg
    c_items["Blowgun"] = Inanimate("Blowgun", item_code=1, cost=1000, details="A long tube. {Ammunition (range 25/100), loading}", weight=1, alpha=1, beta=1, gamma="piercing", delta=1)
    c_items["Crossbow (Hand)"] = Inanimate("Crossbow (Hand)", item_code=1, cost=7500, details="A smaller crossbow. {Ammunition (range 30/120), light, loading}", weight=3, alpha=1, beta=6, gamma="piercing", delta=1)
    c_items["Crossbow (Heavy)"] = Inanimate("Crossbow (Heavy)", item_code=1, cost=5000, details="A heavy-weight crossbow. {Ammunition (range 100/400), heavy, loading, two-handed}", weight=18, alpha=1, beta=10, gamma="piercing", delta=1)
    c_items["Longbow"] = Inanimate("Longbow", item_code=1, cost=5000, details="A large bow drawn by hand. {Ammunition (range 150/600), heavy, two-handed}", weight=2, alpha=1, beta=8, gamma="piercing", delta=1)
    # For the net, does no dmg
    c_items["Net"] = Inanimate("Net", item_code=1, cost=100, details="An open-meshed fabric woven together at regular intervals. {Special, thrown (range 5/15)}", weight=3)

    # Armor ============================================================================================================
    # # Light Armor
    c_items["Padded Armor"] = Inanimate("Padded Armor", item_code=2, cost=500, details="Provides +11 AC", weight=8, alpha=11, beta="dexterity", gamma=True)
    c_items["Leather Armor"] = Inanimate("Leather Armor", item_code=2, cost=1000, details="Provides +11 AC", weight=10, alpha=11, beta="dexterity")
    c_items["Studded Leather Armor"] = Inanimate("Studded Leather Armor", item_code=2, cost=4500, details="Provides +12 AC", weight=13, alpha=12, beta="dexterity")

    # # Medium Armor
    c_items["Hide Armor"] = Inanimate("Hide Armor", item_code=2, cost=1000, details="Provides +12 AC", weight=12, alpha=12, beta="dexterity2")
    c_items["Chain Shirt"] = Inanimate("Chain Shirt", item_code=2, cost=5000, details="Provides +13 AC", weight=20, alpha=13, beta="dexterity2")
    c_items["Scale Mail"] = Inanimate("Scale Mail", item_code=2, cost=5000, details="Provides +14 AC", weight=45, alpha=14, beta="dexterity2", gamma=True)
    c_items["Breastplate"] = Inanimate("Breastplate", item_code=2, cost=40000, details="Provides +14 AC", weight=20, alpha=14, beta="dexterity2")
    c_items["Half Plate"] = Inanimate("Half Plate", item_code=2, cost=75000, details="Provides +15 AC", weight=40, alpha=15, beta="dexterity2", gamma=True)

    # # Heavy Armor
    c_items["Ring Mail"] = Inanimate("Ring Mail", item_code=2, cost=3000, details="Provides +14 AC", weight=40, alpha=14, beta=None, gamma=True)
    c_items["Chain Mail"] = Inanimate("Chain Mail", item_code=2, cost=7500, details="Provides +16 AC", weight=55, alpha=16, beta=None, gamma=True)
    c_items["Splint Armor"] = Inanimate("Splint Armor", item_code=2, cost=20000, details="Provides +17 AC", weight=60, alpha=17, beta=None, gamma=True)
    c_items["Plate Armor"] = Inanimate("Plate Armor", item_code=2, cost=150000, details="Provides +18 AC", weight=65, alpha=18, beta=None, gamma=True)

    # # Shield
    c_items["Shield"] = Inanimate("Shield", item_code=2, cost=1000, details="Provides +2 AC", weight=6, alpha=2, beta=None, gamma=False)

    # c_items[""] = Inanimate("", item_code=3, cost=, details="", max_stack=100, weight=, alpha="", beta=1.0)
    # Adventuring Gear =================================================================================================
    # TYPES LISTED: weapon, medicine, ammunition, utility
    # # Consumable
    c_items["Acid (Vial)"] = Inanimate("Acid (Vial)", item_code=3, cost=2500, details="Can be thrown 5-20 feet away, shattering on impact. Counts as a ranged attack against a creature/object. If it hits, target takes 2d6 acid damage.", max_stack=100, weight=1, alpha="weapon", beta=1.0)
    c_items["Alchemist's Fire (Flask)"] = Inanimate("Alchemist's Fire (Flask)", item_code=3, cost=5000, details="A sticky adhesive fluid that ignites when exposed to air. Can be thrown up to 20 feet, shatters on impact. Counts as a ranged attack against a creature/object. If it hits, target takes 1d4 fire damage at the start of each turn.", max_stack=100, weight=1, alpha="weapon", beta=1.0)
    c_items["Arrows (20)"] = Inanimate("Arrows (20)", item_code=3, cost=100, details="Arrows are used with a weapon that has the ammunition property to make a ranged attack.", max_stack=100, weight=1, alpha="ammunition", beta=1.0)
    c_items["Blowgun Needles (50)"] = Inanimate("Blowgun Needles (50)", item_code=3, cost=100, details="Blowgun needles are used with a weapon that has the ammunition property to make a ranged attack.", max_stack=100, weight=1, alpha="ammunition", beta=1.0)
    c_items["Crossbow Bolts (20)"] = Inanimate("Crossbow Bolts (20)", item_code=3, cost=100, details="Crossbow bolts are used with a weapon that has the ammunition property to make a ranged attack.", max_stack=100, weight=1.5, alpha="ammunition", beta=1.0)
    c_items["Sling Bullets (20)"] = Inanimate("Sling Bullets (20)", item_code=3, cost=4, details="Sling bullets are used with a weapon that has the ammunition property to make a ranged attack.", max_stack=100, weight=1.5, alpha="ammunition", beta=1.0)
    c_items["Antitoxin (Vial)"] = Inanimate("Antitoxin (Vial)", item_code=3, cost=5000, details="A creature that drinks this vial of liquid gains advantage on saving throws against poison for 1 hour. It confers no benefit to undead or constructs.", max_stack=100, weight=0, alpha="medicine", beta=1.0)
    c_items["Ball Bearings (Bag of 1,000)"] = Inanimate("Ball Bearings (Bag of 1,000)", item_code=3, cost=100, details="As an action, you can spill these tiny metal balls from their pouch to cover a level area 10 feet square. A creature moving across the covered area must succeed on a DC 10 Dexterity saving throw or fall prone. A creature moving through the area at half speed doesn’t need to make the saving throw.", max_stack=100, weight=2, alpha="weapon", beta=1.0)
    c_items["Caltrops (Bag of 20)"] = Inanimate("Caltrops (Bag of 20)", item_code=3, cost=100, details="As an action, you can spread a single bag of caltrops to cover a 5-foot-square area. Any creature that enters the area must succeed on a DC 15 Dexterity saving throw or stop moving and take 1 piercing damage. Until the creature regains at least 1 hit point, its walking speed is reduced by 10 feet. A creature moving through the area at half speed doesn’t need to make the saving throw.", max_stack=100, weight=2, alpha="weapon", beta=1.0)
    c_items["Candle"] = Inanimate("Candle", item_code=3, cost=1, details="For 1 hour, a candle sheds bright light in a 5-foot radius and dim light for an additional 5 feet.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    c_items["Chalk (1 piece)"] = Inanimate("Chalk (1 piece)", item_code=3, cost=1, details="A piece of chalk used for writing and marking on various surfaces.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    c_items["Healer's Kit"] = Inanimate("Healer's Kit", item_code=3, cost=500, details="This kit is a leather pouch containing bandages, salves, and splints. The kit has ten uses. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check.", max_stack=100, weight=3, alpha="medicine", beta=1.0)
    c_items["Holy Water (Flask)"] = Inanimate("Holy Water (Flask)", item_code=3, cost=2500, details="As an action, you can splash the contents of this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. In either case, make a ranged attack against a target creature, treating the holy water as an improvised weapon. If the target is a fiend or undead, it takes 2d6 radiant damage.", max_stack=100, weight=1, alpha="weapon", beta=1.0)
    c_items["Ink (1 ounce bottle)"] = Inanimate("Ink (1 ounce bottle)", item_code=3, cost=1000, details="Ink is typically used with an ink pen to write.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    c_items["Oil (Flask)"] = Inanimate("Oil (Flask)", item_code=3, cost=10, details="Oil usually comes in a clay flask that holds 1 pint. As an action, you can splash the oil in this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. Make a ranged attack against a target creature or object, treating the oil as an improvised weapon. On a hit, the target is covered in oil. If the target takes any fire damage before the oil dries (after 1 minute), the target takes an additional 5 fire damage from the burning oil. You can also pour a flask of oil on the ground to cover a 5-foot-square area, provided that the surface is level. If lit, the oil burns for 2 rounds and deals 5 fire damage to any creature that enters the area or ends its turn in the area. A creature can take this damage only once per turn.", max_stack=100, weight=1, alpha="utility", beta=1.0)
    c_items["Perfume (Vial)"] = Inanimate("Perfume (Vial)", item_code=3, cost=500, details="A fragrant commodity typically used by the wealthy.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    c_items["Basic Poison (Vial)"] = Inanimate("Basic Poison (Vial)", item_code=3, cost=10000, details="You can use the poison in this vial to coat one slashing or piercing weapon or up to three pieces o f ammunition. Applying the poison takes an action. A creature hit by the poisoned weapon or ammunition must make a DC 10 Constitution saving throw or take 1d4 poison damage. Once applied, the poison retains potency for 1 minute before drying.", max_stack=100, weight=0, alpha="weapon", beta=1.0)
    c_items["Potion of Healing"] = Inanimate("Potion of Healing", item_code=3, cost=5000, details="A character who drinks the magical red fluid in this vial regains 2d4 + 2 hit points. Drinking or administering a potion takes an action.", max_stack=100, weight=0.5, alpha="medicine", beta=1.0)
    c_items["Rations (1 day)"] = Inanimate("Rations (1 day)", item_code=3, cost=50, details="Rations consist of dry foods suitable for extended travel, including jerky, dried fruit, hardtack, and nuts.", max_stack=100, weight=2, alpha="utility", beta=1.0)
    c_items["Sealing Wax"] = Inanimate("Sealing Wax", item_code=3, cost=50, details="Wax melted to seal letters. When you press a signet ring into warm sealing wax, you leave an identifying mark.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    c_items["Soap"] = Inanimate("Soap", item_code=3, cost=2, details="A commodity used for bathing.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    c_items["Iron Spikes (10)"] = Inanimate("Iron Spikes (10)", item_code=3, cost=100, details="Standard iron spikes typically used with a hammer.", max_stack=100, weight=5, alpha="aid", beta=1.0)
    c_items["Torch"] = Inanimate("Torch", item_code=3, cost=1, details="A torch burns for 1 hour, providing bright light in a 20-foot radius and dim light for an additional 20 feet. If you make a melee attack with a burning torch and hit, it deals 1 fire damage.", max_stack=100, weight=1, alpha="utility", beta=1.0)

    c_items["Mana Potion"] = Inanimate("Mana Potion", item_code=3, cost=5000, details="Restores Mana", max_stack=6, weight=0.5, alpha="medicine", beta=1.0)

    # c_items[""] = Inanimate("", item_code=4, cost=, details="", max_stack=100, weight=)
    # # Non-Consumable
    c_items["Abacus"] = Inanimate("Abacus", item_code=4, cost=200, details="A calculating tool", max_stack=100, weight=2)
    c_items["Arcane Focus - Crystal"] = Inanimate("Arcane Focus Crystal", item_code=4, cost=1000, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=1)
    c_items["Arcane Focus - Orb"] = Inanimate("Arcane Focus Orb", item_code=4, cost=2000, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=3)
    c_items["Arcane Focus - Rod"] = Inanimate("Arcane Focus Rod", item_code=4, cost=1000, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=2)
    c_items["Arcane Focus - Staff"] = Inanimate("Arcane Focus Staff", item_code=4, cost=500, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=4)
    c_items["Arcane Focus - Wand"] = Inanimate("Arcane Focus Wand", item_code=4, cost=1000, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=1)
    c_items["Backpack"] = Inanimate("Backpack", item_code=4, cost=200, details="A backpack is a leather pack carried on the back, typically with straps to secure it. A backpack can hold 1 cubic foot/  30 pounds of gear. You can also strap items, such as a bedroll or a coil of rope, to the outside of a backpack", max_stack=100, weight=5)
    c_items["Barrel"] = Inanimate("Barrel", item_code=4, cost=200, details="A barrel can hold 40 gallons of liquid or 4 cubic feet of solid material.", max_stack=100, weight=70)
    c_items["Basket"] = Inanimate("Basket", item_code=4, cost=40, details="A basket can hold 2 cubic feet / 40 pounds of gear.", max_stack=100, weight=2)
    c_items["Bedroll"] = Inanimate("Bedroll", item_code=4, cost=100, details="You never know where you’re going to sleep, and a bedroll helps you get better sleep in a hayloft or on the cold ground. A bedroll consists of bedding and a blanket thin enough to be rolled up and tied. In an emergency, it can double as a stretcher.", max_stack=100, weight=7)
    c_items["Bell"] = Inanimate("Bell", item_code=4, cost=100, details="A standard bell that rings, typically used for signaling.", max_stack=100, weight=0)
    c_items["Blanket"] = Inanimate("Blanket", item_code=4, cost=50, details="A thick, quilted, blanket made to keep you warm in cold weather.", max_stack=100, weight=3)
    c_items["Block and Tackle"] = Inanimate("Block and Tackle", item_code=4, cost=100, details="A set of pulleys with a cable threaded through them and a hook to attach to objects, a block and tackle allows you to hoist up to four times the weight you can normally lift.", max_stack=100, weight=5)
    c_items["Book"] = Inanimate("Book", item_code=4, cost=2500, details="A book might contain poetry, historical accounts, information pertaining to a particular field of lore, diagrams and notes on gnomish contraptions, or just about anything else that can be represented using text or pictures. ", max_stack=100, weight=5)
    c_items["Bottle (Glass)"] = Inanimate("Bottle (Glass)", item_code=4, cost=200, details="A bottle can hold 1 1/2 pints of liquid.", max_stack=100, weight=2)
    c_items["Bucket"] = Inanimate("Bucket", item_code=4, cost=5, details="A bucket can hold 3 gallons of liquid, or 1/2 cubic foot of solid material.", max_stack=100, weight=2)
    c_items["Crossbow Bold Case"] = Inanimate("Crossbow Bolt Case", item_code=4, cost=100, details="This wooden case can hold up to twenty crossbow bolts.", max_stack=100, weight=1)
    c_items["Map or Scroll Case"] = Inanimate("Map or Scroll Case", item_code=4, cost=100, details="This cylindrical leather case can hold up to ten rolled-up sheets of paper or five rolled-up sheets of parchment.", max_stack=100, weight=1)
    c_items["Chain (10 feet)"] = Inanimate("Chain (10 Feet)", item_code=4, cost=500, details="A chain has 10 hit points. It can be burst with a successful DC 20 Strength check.", max_stack=100, weight=10)
    c_items["Chest"] = Inanimate("Chest", item_code=4, cost=500, details="A chest can hold 12 cubic feet / 300 pounds of gear.", max_stack=100, weight=25)
    c_items["Climber's Kit"] = Inanimate("Climber's Kit", item_code=4, cost=2500, details="A climber's kit includes special pitons, boot tips, gloves, and a harness. You can use the climber's kit as an action to anchor yourself; when you do, you can't fall more than 25 feet from the point where you anchored yourself, and you can't climb more than 25 feet away from that point without undoing the anchor.", max_stack=100, weight=12)
    c_items["Clothes (Common)"] = Inanimate("Clothes (Common)", item_code=4, cost=50, details="This set of clothes could consist of a loose shirt and baggy breeches, or a loose shirt and skirt or overdress. Cloth wrappings are used for shoes.", max_stack=100, weight=3)
    c_items["Clothes (Costume)"] = Inanimate("Clothes (Costume)", item_code=4, cost=500, details="This set of clothes is fashioned after a particular costume, typically meant for entertaining.", max_stack=100, weight=4)
    c_items["Clothes (Fine)"] = Inanimate("Clothes (Fine)", item_code=4, cost=1500, details="This set of clothes is designed specifically to be expensive and to show it, including fancy, tailored clothes in whatever fashion happens to be the current style in the courts of the nobles. Precious metals and gems could be worked into the clothing.", max_stack=100, weight=6)
    c_items["Clothes (Traveler's)"] = Inanimate("Clothes (Traveler's)", item_code=4, cost=200, details="This set of clothes could consist of boots, a wool skirt or breeches, a sturdy belt, a shirt (perhaps with a vest or jacket), and an ample cloak with a hood.", max_stack=100, weight=4)
    c_items["Component Pouch"] = Inanimate("Component Pouch", item_code=4, cost=2500, details="A component pouch is a small, watertight leather belt pouch that has compartments to hold all the material components and other special items you need to cast your spells, except for those components that have a specific cost.", max_stack=100, weight=2)
    c_items["Crowbar"] = Inanimate("Crowbar", item_code=4, cost=200, details="Using a crowbar grants advantage to Strength checks where the crowbar's leverage can be applied.", max_stack=100, weight=5)
    c_items["Druidic Focus - Sprig of Mistletoe"] = Inanimate("Druidic Focus - Sprig of Mistletoe", item_code=4, cost=100, details="A druidic focus might be a sprig of mistletoe or holly, a wand or scepter made of yew or another special wood, a staff drawn whole out of a living tree, or a totem object incorporating feathers, fur, bones, and teeth from sacred animals. A druid can use such an object as a spellcasting focus.", max_stack=100, weight=0)
    c_items["Druidic Focus - Totem"] = Inanimate("Druidic Focus - Totem", item_code=4, cost=100, details="A druidic focus might be a sprig of mistletoe or holly, a wand or scepter made of yew or another special wood, a staff drawn whole out of a living tree, or a totem object incorporating feathers, fur, bones, and teeth from sacred animals. A druid can use such an object as a spellcasting focus.", max_stack=100, weight=0)
    c_items["Druidic Focus - Wooden Staff"] = Inanimate("Druidic Focus - Wooden Staff", item_code=4, cost=500, details="A druidic focus might be a sprig of mistletoe or holly, a wand or scepter made of yew or another special wood, a staff drawn whole out of a living tree, or a totem object incorporating feathers, fur, bones, and teeth from sacred animals. A druid can use such an object as a spellcasting focus.", max_stack=100, weight=4)
    c_items["Druidic Focus - Yew Wand"] = Inanimate("Druidic Focus - Yew Wand", item_code=4, cost=1000, details="A druidic focus might be a sprig of mistletoe or holly, a wand or scepter made of yew or another special wood, a staff drawn whole out of a living tree, or a totem object incorporating feathers, fur, bones, and teeth from sacred animals. A druid can use such an object as a spellcasting focus.", max_stack=100, weight=1)
    c_items["Fishing Tackle"] = Inanimate("Fishing Tackle", item_code=4, cost=100, details="This kit includes a wooden rod, silken line, corkwood bobbers, steel hooks, lead sinkers, velvet lures, and narrow netting.", max_stack=100, weight=4)
    c_items["Flask"] = Inanimate("Flask", item_code=4, cost=2, details="Can hold 1 pint of liquid.", max_stack=100, weight=1)
    c_items["Tankard"] = Inanimate("Tankard", item_code=4, cost=2, details="Can hold 1 pint of liquid.", max_stack=100, weight=1)
    c_items["Grappling Hook"] = Inanimate("Grappling Hook", item_code=4, cost=200, details="When tied to the end of a rope, a grappling hook can secure the rope to a battlement, window ledge, tree limb, or other protrusion.", max_stack=100, weight=4)
    c_items["Hammer"] = Inanimate("Hammer", item_code=4, cost=100, details="A one-handed hammer with an iron head.", max_stack=100, weight=3)
    c_items["Sledgehammer"] = Inanimate("Sledgehammer", item_code=4, cost=200, details="A two-handed, iron-headed hammer.", max_stack=100, weight=10)
    c_items["Holy Symbol - Amulet"] = Inanimate("Holy Symbol - Amulet", item_code=4, cost=500, details="A representation of a god or pantheon. A cleric or paladin can use a holy symbol as a spellcasting focus. To use the symbol in this way, the caster must hold it in hand, wear it visibly, or bear it on a shield.", max_stack=100, weight=1)
    c_items["Holy Symbol - Emblem"] = Inanimate(" Holy Symbol - Emblem", item_code=4, cost=500, details="A representation of a god or pantheon. A cleric or paladin can use a holy symbol as a spellcasting focus. To use the symbol in this way, the caster must hold it in hand, wear it visibly, or bear it on a shield.", max_stack=100, weight=0)
    c_items["Holy Symbol - Reliquary"] = Inanimate("Holy Symbol - Reliquary", item_code=4, cost=500, details="A representation of a god or pantheon. A cleric or paladin can use a holy symbol as a spellcasting focus. To use the symbol in this way, the caster must hold it in hand, wear it visibly, or bear it on a shield.", max_stack=100, weight=2)
    c_items["Hourglass"] = Inanimate("Hourglass", item_code=4, cost=2500, details="A standard hourglass used to measure the passage of time.", max_stack=100, weight=1)
    c_items["Hunting Trap"] = Inanimate("Hunting Trap", item_code=4, cost=500, details="When you use your action to set it, this trap forms a saw-toothed steel ring that snaps shut when a creature steps on a pressure plate in the center. The trap is affixed by a heavy chain to an immobile object, such as a tree or a spike driven into the ground. A creature that steps on the plate must succeed on a DC 13 Dexterity saving throw or take 1d4 piercing damage and stop moving. Thereafter, until the creature breaks free of the trap, its movement is limited by the length of the chain (typically 3 feet long). A creature can use its action to make a DC 13 Strength check, freeing itself or another creature within its reach on a success. Each failed check deals 1 piercing damage to the trapped creature.", max_stack=100, weight=25)
    c_items["Ink Pen"] = Inanimate("Ink Pen", item_code=4, cost=2, details="A wooden stick with a special tip on the end. The tip draws ink in when dipped in a vial and leaves an ink trail when drawn across a surface.", max_stack=100, weight=0)
    c_items["Jug"] = Inanimate("Jug", item_code=4, cost=2, details="Can hold 1 gallon of liquid.", max_stack=100, weight=4)
    c_items["Pitcher"] = Inanimate("Pitcher", item_code=4, cost=2, details="Can hold 1 gallon of liquid.", max_stack=100, weight=4)
    c_items["Ladder (10-foot)"] = Inanimate("Ladder (10-foot)", item_code=4, cost=10, details="A straight, simple wooden ladder.", max_stack=100, weight=25)
    c_items["Lamp"] = Inanimate("Lamp", item_code=4, cost=50, details="A lamp casts bright light in a 15-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil.", max_stack=100, weight=1)
    c_items["Lantern (Bullseye)"] = Inanimate("Lantern (Bullseye)", item_code=4, cost=1000, details="Casts bright light in a 60-foot cone and dim light for an additional 60 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil.", max_stack=100, weight=2)
    c_items["Lantern (Hooded)"] = Inanimate("Lantern (Hooded)", item_code=4, cost=500, details="A hooded lantern casts bright light in a 30-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil. As an action, you can lower the hood, reducing the light to dim light in a 5-foot radius.", max_stack=100, weight=2)
    c_items["Lock"] = Inanimate("Lock", item_code=4, cost=1000, details="A key is provided with the lock. Without the key, a creature proficient with thieves' tools can pick this lock with a successful DC 15 Dexterity check.", max_stack=100, weight=1)
    c_items["Magnifying Glass"] = Inanimate("Magnifying Glass", item_code=4, cost=10000, details="This lens allows a closer look at small objects. It is also useful as a substitute for flint and steel when starting fires. Lighting a fire with a magnifying glass requires light as bright as sunlight to focus, tinder to ignite, and about 5 minutes for the fire to ignite. A magnifying glass grants advantage on any ability check made to appraise or inspect an item that is small or highly detailed.", max_stack=100, weight=0)
    c_items["Manacles"] = Inanimate("Manacles", item_code=4, cost=200, details="These metal restraints can bind a Small or Medium creature. Escaping the manacles requires a successful DC 20 Dexterity check. Breaking them requires a successful DC 20 Strength check. Each set of manacles comes with one key. Without the key, a creature proficient with thieves' tools can pick the manacles' lock with a successful DC 15 Dexterity check. Manacles have 15 hit points.", max_stack=100, weight=6)
    c_items["Mess Kit"] = Inanimate("Mess Kit", item_code=4, cost=20, details="This tin box contains a cup and simple cutlery. The box clamps together, and one side can be used as a cooking pan and the other as a plate or shallow bowl.", max_stack=100, weight=1)
    c_items["Mirror (Steel)"] = Inanimate("Mirror (Steel)", item_code=4, cost=500, details="A reflective surface.", max_stack=100, weight=.5)
    c_items["Paper (One sheet)"] = Inanimate("Paper (One sheet)", item_code=4, cost=20, details="A sheet of standard paper. Made from cloth fibers.", max_stack=100, weight=0)
    c_items["Parchment (One sheet)"] = Inanimate("Parchment (One sheet)", item_code=4, cost=10, details="A piece of goat hide or sheepskin that has been prepared for writing on.", max_stack=100, weight=10)
    c_items["Miner's Pick"] = Inanimate("Miner's Pick", item_code=4, cost=200, details="A miner's pick is designed to concentrate the force of its blow on a small area.", max_stack=100, weight=10)
    c_items["Piton"] = Inanimate("Piton", item_code=4, cost=5, details="A piton is a steel spike with an eye through which you can loop a rope.", max_stack=100, weight=.25)
    c_items["Pole (10-foot)"] = Inanimate("Pole (10-foot)", item_code=4, cost=5, details="A long, slender, rounded piece of wood or metal,", max_stack=100, weight=7)
    c_items["Iron Pot"] = Inanimate("Iron Pot", item_code=4, cost=200, details="An iron pot can hold 1 gallon of liquid.", max_stack=100, weight=10)
    c_items["Pouch"] = Inanimate("Pouch", item_code=4, cost=50, details="A cloth or leather pouch can hold up to 20 sling bullets or 50 blowgun needles, among other things.", max_stack=100, weight=1)
    c_items["Quiver"] = Inanimate("Quiver", item_code=4, cost=100, details="A quiver can hold up to 20 arrows.", max_stack=100, weight=1)
    c_items["Portable Ram"] = Inanimate("Portable Ram", item_code=4, cost=400, details="You can use a portable ram to break down doors. When doing so, you gain a +4 bonus on the Strength check. One other character can help you use the ram, giving you advantage on this check.", max_stack=100, weight=35)
    c_items["Robes"] = Inanimate("Robes", item_code=4, cost=100, details="A standard set of robes.", max_stack=100, weight=4)
    c_items["Hempen Rope (50 Feet)"] = Inanimate("Hempen Rope (50 Feet)", item_code=4, cost=100, details="Rope has 2 hit points and can be burst with a DC 17 Strength check.", max_stack=100, weight=10)
    c_items["Silk Rope (50 Feet)"] = Inanimate("Silk Rope (50 Feet)", item_code=4, cost=1000, details="Rope has 2 hit points and can be burst with a DC 17 Strength check.", max_stack=100, weight=5)
    c_items["Sack"] = Inanimate("Sack", item_code=4, cost=1, details="A sack can hold 1 cubic foot / 30 pounds of gear.", max_stack=100, weight=.5)
    c_items["Merchant's Scale"] = Inanimate("Merchant's Scale", item_code=4, cost=500, details="A scale includes a small balance, pans, and a suitable assortment of weights up to 2 pounds. With it, you can measure the exact weight of small objects, such as raw precious metals or trade goods, to help determine their worth.", max_stack=100, weight=3)
    c_items["Shovel"] = Inanimate("Shovel", item_code=4, cost=200, details="A standard shovel used for digging.", max_stack=100, weight=5)
    c_items["Signal Whistle"] = Inanimate("Signal Whistle", item_code=4, cost=5, details="A small whistle used for signaling.", max_stack=100, weight=0)
    c_items["Signet Ring"] = Inanimate("Signet Ring", item_code=4, cost=500, details="Each signet ring has a distinctive design carved into it. When you press this ring into warm sealing wax, you leave an identifying mark.", max_stack=100, weight=0)
    c_items["Spellbook"] = Inanimate("Spellbook", item_code=4, cost=5000, details="Essential for wizards, a spellbook is a leather-bound tome with 100 blank vellum pages suitable for recording spells.", max_stack=100, weight=3)
    c_items["Spyglass"] = Inanimate("Spyglass", item_code=4, cost=100000, details="Objects viewed through a spyglass are magnified to twice their size.", max_stack=100, weight=1)
    c_items["Tent (Two-Person)"] = Inanimate("Tent (Two-Person)", item_code=4, cost=200, details="A simple and portable canvas shelter, a tent sleeps two.", max_stack=100, weight=20)
    c_items["Tinderbox"] = Inanimate("Tinderbox", item_code=4, cost=50, details="This small container holds flint, fire steel, and tinder (usually dry cloth soaked in light oil) used to kindle a fire. Using it to light a torch -- or anything else with abundant, exposed fuel -- takes an action. Lighting any other fire takes 1 minute.", max_stack=100, weight=1)
    c_items["Vial"] = Inanimate("Vial", item_code=4, cost=100, details="A small glass container. Can hold 4 ounces of liquid.", max_stack=100, weight=0)
    c_items["Waterskin"] = Inanimate("Waterskin", item_code=4, cost=20, details="Can hold 4 pints of liquid. Weighs 5 lbs. when full.", max_stack=100, weight=5)
    c_items["Whetstone"] = Inanimate("Whetstone", item_code=4, cost=1, details="A standard whetstone used to sharpen blades.", max_stack=100, weight=1)

    # Tools ============================================================================================================
    # # Artisan's Tools
    c_items["Alchemist's Supplies"] = Inanimate("Alchemist's Supplies", item_code=4, cost=5000, details="Special tools needed to pursue alchemy. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=8)
    c_items["Brewer's Supplies"] = Inanimate("Brewer's Supplies", item_code=4, cost=2000, details="Special tools needed to pursue brewing. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=9)
    c_items["Calligrapher's Supplies"] = Inanimate("Calligrapher's Supplies", item_code=4, cost=1000, details="Special tools needed to pursue calligraphy. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=5)
    c_items["Carpenter's Tools"] = Inanimate("Carpenter's Tools", item_code=4, cost=500, details="Special tools needed to pursue carpentry. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=6)
    c_items["Cartographer's Tools"] = Inanimate("Cartographer's Tools", item_code=4, cost=1500, details="Special tools needed to pursue cartography. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=6)
    c_items["Cobbler's Tools"] = Inanimate("Cobbler's Tools", item_code=4, cost=500, details="Special tools needed to pursue cobbling. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=5)
    c_items["Cook's Utensils"] = Inanimate("Cook's Utensils", item_code=4, cost=100, details="Special tools needed to pursue cooking. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=8)
    c_items["Glassblower's Tools"] = Inanimate("Glassblower's Tools", item_code=4, cost=3000, details="Special tools needed to pursue glassblowing. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=5)
    c_items["Jeweler's Tools"] = Inanimate("Jeweler's Tools", item_code=4, cost=2500, details="Special tools needed to pursue jeweling. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=2)
    c_items["Leatherworker's Tools"] = Inanimate("Leatherworker's Tools", item_code=4, cost=500, details="Special tools needed to pursue leatherworking. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=5)
    c_items["Mason's Tools"] = Inanimate("Mason's Tools", item_code=4, cost=1000, details="Special tools needed to pursue masonry. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=8)
    c_items["Painter's Supplies"] = Inanimate("Painter's Supplies", item_code=4, cost=1000, details="Special tools needed to pursue painting. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=5)
    c_items["Potter's Tools"] = Inanimate("Potter's Tools", item_code=4, cost=1000, details="Special tools needed to pursue pottery. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=3)
    c_items["Smith's Tools"] = Inanimate("Smith's Tools", item_code=4, cost=2000, details="Special tools needed to pursue smithing. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=8)
    c_items["Tinker's Tools"] = Inanimate("Tinker's Tools", item_code=4, cost=5000, details="Special tools needed to pursue tinkering. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=10)
    c_items["Weaver's Tools"] = Inanimate("Weaver's Tools", item_code=4, cost=100, details="Special tools needed to pursue weaving. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=5)
    c_items["Woodcarver's Tools"] = Inanimate("Woodcarver's Tools", item_code=4, cost=100, details="Special tools needed to pursue woodcarving. Proficiency with this set of tools lets you add your proficiency bonus to any ability checks you make using the tools in your craft.", max_stack=100, weight=5)

    # # Gaming Set
    c_items["Dice Set"] = Inanimate("Dice Set", item_code=4, cost=10, details="A set of dice. If you are proficient with a gaming set, you can add your proficiency bonus to ability checks you make to play a game with that set.", max_stack=100, weight=0)
    c_items["Dragonchess Set"] = Inanimate("Dragonchess Set", item_code=4, cost=100, details="A set of pieces needed for dragonchess. If you are proficient with a gaming set, you can add your proficiency bonus to ability checks you make to play a game with that set.", max_stack=100, weight=0.5)
    c_items["Playing Card Set"] = Inanimate("Playing Card Set", item_code=4, cost=50, details="A full deck of playing cards. If you are proficient with a gaming set, you can add your proficiency bonus to ability checks you make to play a game with that set.", max_stack=100, weight=0)
    c_items["Three-Dragon Ante Set"] = Inanimate("Three-Dragon Ante Set", item_code=4, cost=100, details="All the stuff you need for a game of three-dragon ante, a card game of luck and skill. If you are proficient with a gaming set, you can add your proficiency bonus to ability checks you make to play a game with that set.", max_stack=100, weight=0)

    # # Musical Instruments
    c_items["Bagpipes"] = Inanimate("Bagpipes", item_code=4, cost=3000, details="A woodwind instrument using enclosed reeds fed from a constant reservoir of air in the form of a bag. If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus.", max_stack=100, weight=6)
    c_items["Drum"] = Inanimate("Drum", item_code=4, cost=600, details="A percussion instrument sounded by being struck with sticks or the hands. If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus.", max_stack=100, weight=3)
    c_items["Dulcimer"] = Inanimate("Dulcimer", item_code=4, cost=2500, details="A musical instrument with a long rounded body and a fretted fingerboard, played by bowing, plucking, and strumming. If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus.", max_stack=100, weight=10)
    c_items["Flute"] = Inanimate("Flute", item_code=4, cost=200, details="A wind instrument made from a tube with holes along it that are stopped by the fingers or keys. If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus.", max_stack=100, weight=1)
    c_items["Lute"] = Inanimate("Lute", item_code=4, cost=3500, details="A plucked stringed instrument with a long neck bearing frets and a rounded body with a flat front that is shaped like a halved egg. If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus.", max_stack=100, weight=2)
    c_items["Lyre"] = Inanimate("Lyre", item_code=4, cost=3000, details="A stringed instrument like a small U-shaped harp with strings fixed to a crossbar. If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus. ", max_stack=100, weight=2)
    c_items["Horn"] = Inanimate("Horn", item_code=4, cost=300, details="A wind instrument, conical in shape or wound into a spiral. If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus.", max_stack=100, weight=2)
    c_items["Pan Flute"] = Inanimate("Pan Flute", item_code=4, cost=1200, details="A wind instrument consisting of multiple pipes of gradually increasing length and occasionally girth. If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus.", max_stack=100, weight=2)
    c_items["Shawm"] = Inanimate("Shawm", item_code=4, cost=200, details="A wind instrument with a double reed enclosed in a wooden mouthpiece, and having a penetrating tone.  If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus.", max_stack=100, weight=1)
    c_items["Viol"] = Inanimate("Viol", item_code=4, cost=3000, details="A musical instrument, typically six-stringed, held vertically and played with a bow.  If you have proficiency with a given musical instrument, you can add your proficiency bonus to any ability checks you make to play music with the instrument. A bard can use a musical instrument as a spellcasting focus.", max_stack=100, weight=1)

    # # Other kits + tools
    c_items["Disguise Kit"] = Inanimate("Disguise Kit", item_code=4, cost=2500, details="This pouch of cosmetics, hair dye, and small props lets you create disguises that change your physical appearance. Proficiency with this kit lets you add your proficiency bonus to any ability checks you make to create a visual disguise.", max_stack=100, weight=3)
    c_items["Forgery Kit"] = Inanimate("Forgery Kit", item_code=4, cost=1500, details="This small box contains a variety of papers and parchments, pens and inks, seals and sealing wax, gold and silver leaf, and other supplies necessary to create convincing forgeries of physical documents. Proficiency with this kit lets you add your proficiency bonus to any ability checks you make to create a physical forgery of a document.", max_stack=100, weight=5)
    c_items["Herbalism Kit"] = Inanimate("Herbalism Kit", item_code=4, cost=500, details="This kit contains a variety of instruments such as clippers, mortar and pestle, and pouches and vials used by herbalists to create remedies and potions. Proficiency with this kit lets you add your proficiency bonus to any ability checks you make to identify or apply herbs. Also, proficiency with this kit is required to create antitoxin and potions of healing.", max_stack=100, weight=3)
    c_items["Navigator's Tools"] = Inanimate("Navigator's Tools", item_code=4, cost=2500, details="This set of instruments is used for navigation at sea. Proficiency with navigator's tools lets you chart a ship's course and follow navigation charts. In addition, these tools allow you to add your proficiency bonus to any ability check you make to avoid getting lost at sea.", max_stack=100, weight=2)
    c_items["Poisoner's Kit"] = Inanimate("Poisoner's Kit", item_code=4, cost=5000, details="A poisoner’s kit includes the vials, chemicals, and other equipment necessary for the creation of poisons. Proficiency with this kit lets you add your proficiency bonus to any ability checks you make to craft or use poisons.", max_stack=100, weight=2)
    c_items["Thieves' Tools"] = Inanimate("Thieves' Tools", item_code=4, cost=2500, details="This set of tools includes a small file, a set of lock picks, a small mirror mounted on a metal handle, a set of narrow-bladed scissors, and a pair of pliers. Proficiency with these tools lets you add your proficiency bonus to any ability checks you make to disarm traps or open locks.", max_stack=100, weight=1)

    # Food & Drink =====================================================================================================
    c_items["Ale (Gallon)"] = Inanimate("Ale (Gallon)", item_code=3, cost=20, details="A type of beer with a bitter flavor and higher alcoholic content. Now served by the gallon.", max_stack=100, alpha="drink", beta=1.0)
    c_items["Ale (Mug)"] = Inanimate("Ale (Mug)", item_code=3, cost=4, details="A type of beer with a bitter flavor and higher alcoholic content. Now served by the mug.", max_stack=100, alpha="drink", beta=1.0)
    c_items["Banquet (per person)"] = Inanimate("Banquet (per person)", item_code=3, cost=1000, details="An elaborate and formal meal", max_stack=100, alpha="food", beta=1.0)
    c_items["Bread (Loaf)"] = Inanimate("Bread (Loaf)", item_code=3, cost=2, details="A standard loaf of white bread.", max_stack=100, alpha="food", beta=1.0)
    c_items["Cheese (Hunk)"] = Inanimate("Cheese (Hunk)", item_code=3, cost=10, details="A dairy product, derived from milk.", max_stack=100, alpha="food", beta=1.0)
    c_items["Meat (Chunk)"] = Inanimate("Meat (Chunk)", item_code=3, cost=30, details="A chunk of roasted animal flesh.", max_stack=100, alpha="food", beta=1.0)
    c_items["Common Wine (Pitcher)"] = Inanimate("Common Wine (Pitcher)", item_code=3, cost=20, details="An alcoholic drink made from fermented grape juice. Cheap but it gets the job done.", max_stack=100, alpha="food", beta=1.0)
    c_items["Fine Wine (Bottle)"] = Inanimate("Fine Wine (Bottle)", item_code=3, cost=1000, details="An alcoholic drink made from fermented grape juice. The bottle looks quite luxurious.", max_stack=100, alpha="food", beta=1.0)

    # Packs ============================================================================================================
    # # Pack Exclusive
    c_items["String (10 feet)"] = Inanimate("String", item_code=4, cost=0, details="A 10-foot length of string, typically found in a burglar's pack.", max_stack=100, weight=0)
    c_items["Little Bag of Sand"] = Inanimate("Little Bag of Sand", item_code=4, cost=0, details="A small bag of sand, typically found in a scholar's pack.", max_stack=100, weight=0)
    c_items["Small Knife"] = Inanimate("Small Knife", item_code=4, cost=0, details="A small knife, typically found in a scholar's pack.", max_stack=100, weight=0)
    c_items["Alms Box"] = Inanimate("Alms Box", item_code=4, cost=0, details="A small box for alms, typically found in a priest's pack.", max_stack=100, weight=0)
    c_items["Censer"] = Inanimate("Censer", item_code=4, cost=0, details="A censer, typically found in a priest's pack.", max_stack=100, weight=0)
    c_items["Block of Incense"] = Inanimate("Block of Incense", item_code=3, cost=0, details="A block of incense, typically found in a priest's pack.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    c_items["Vestments"] = Inanimate("Vestments", item_code=4, cost=0, details="Religious clothing, typically found in a priest's pack.", max_stack=100, weight=0)

    # # The Packs
    c_items["Burglar's Pack"] = Inanimate("Burglar's Pack", item_code=5, cost=1600, details={"Backpack": 1, "Ball Bearings (Bag of 1,000)": 1, "String (10 feet)": 1, "Bell": 1, "Candle": 5, "Crowbar": 1, "Hammer": 1, "Piton": 10, "Lantern (Hooded)": 1, "Oil (Flask)": 2, "Rations (1 day)": 5, "Tinderbox": 1, "Waterskin": 1, "Hempen Rope (50 Feet)": 1})
    c_items["Diplomat's Pack"] = Inanimate("Diplomat's Pack", item_code=5, cost=3900, details={"Chest": 1, "Map or Scroll Case": 2, "Clothes (Fine)": 1, "Ink (1 ounce bottle)": 1, "Ink Pen": 1, "Lamp": 1, "Oil (Flask)": 2, "Paper (One Sheet)": 5, "Perfume (Vial)": 1, "Sealing Wax": 1, "Soap": 1})
    c_items["Dungeoneer's Pack"] = Inanimate("Dungeoneer's Pack", item_code=5, cost=1200, details={"Backpack": 1, "Crowbar": 1, "Hammer": 1, "Piton": 10, "Torch": 10, "Tinderbox": 1, "Rations (1 day)": 10, "Waterskin": 1, "Hempen Rope (50 Feet)": 1})
    c_items["Entertainer's Pack"] = Inanimate("Entertainer's Pack", item_code=5, cost=4000, details={"Backpack": 1, "Bedroll": 1, "Clothes (Costume)": 2, "Candle": 5, "Rations (1 day)": 5, "Waterskin": 1, "Disguise Kit": 1})
    c_items["Explorer's Pack"] = Inanimate("Explorer's Pack", item_code=5, cost=1000, details={"Backpack": 1, "Bedroll": 1, "Mess Kit": 1, "Tinderbox": 1, "Torch": 10, "Rations (1 day)": 10, "Waterskin": 1, "Hempen Rope (50 Feet)": 1})
    c_items["Priest's Pack"] = Inanimate("Priest's Pack", item_code=5, cost=1900, details={"Backpack": 1, "Blanket": 1, "Candle": 10, "Tinderbox": 1, "Alms Box": 1, "Block of Incense": 2, "Censer": 1, "Vestments": 1, "Rations (1 day)": 2, "Waterskin": 1})
    c_items["Scholar's Pack"] = Inanimate("Scholar's Pack", item_code=5, cost=4000, details={"Backpack": 1, "Book": 1, "Ink (1 ounce bottle)": 1, "Ink Pen": 1, "Parchment (One sheet)": 10, "Little Bag of Sand": 1, "Small Knife": 1})

    pickle.dump(c_items, open("items_main.camp", "wb"))

try:
    custom = pickle.load(open("items_custom.camp", "rb"))
except: pass


def get_item(self, name, is_custom=False):
    if is_custom:
        return custom.get(name)
    else:
        return c_items.get(name)


def add_item(self, item_type, is_custom=False):

    if is_custom:
        pickle.dump(custom, open("items_custom.camp", "wb"))
    else:
        pickle.dump(c_items, open("items_main.camp", "wb"))
