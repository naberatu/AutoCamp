
from inanimate import Inanimate
import pickle


catalog = dict()
custom = dict()

try:
    catalog = pickle.load(open("items_main.camp", "rb"))
except:

    # Weapons ==========================================================================================================
    # # Simple Melee Weapons
    catalog["Club"] = Inanimate("Club", item_code=1, cost=10, details="A wooden club. {Light}", weight=2, alpha=1, beta=4, gamma="bludgeoning")
    catalog["Dagger"] = Inanimate("Dagger", item_code=1, cost=200, details="An iron dagger. {Finesse, light, thrown (range 20/60)}", weight=1, alpha=1, beta=4, gamma="piercing")
    catalog["Greatclub"] = Inanimate("Greatclub", item_code=1, cost=20, details="A massive club. {Two-handed}", weight=10, alpha=1, beta=8, gamma="bludgeoning")
    catalog["Handaxe"] = Inanimate("Handaxe", item_code=1, cost=500, details="A simple handaxe. {Light, thrown (range 20/60)}", weight=2, alpha=1, beta=6, gamma="slashing")
    catalog["Javelin"] = Inanimate("Javelin", item_code=1, cost=50, details="A sturdy javelin. {Thrown (range 30/120)}", weight=2, alpha=1, beta=6, gamma="slashing")
    catalog["Light Hammer"] = Inanimate("Light Hammer", item_code=1, cost=200, details="A smaller, lighter hammer. {Light, thrown (range 20/60)}", weight=2, alpha=1, beta=4, gamma="bludgeoning")
    catalog["Mace"] = Inanimate("Mace", item_code=1, cost=5, details="A weapon with a bladed head.", weight=4, alpha=1, beta=6, gamma="bludgeoning")
    catalog["Quarterstaff"] = Inanimate("Quarterstaff", item_code=1, cost=200, details="A light and powerful staff. {Versatile (1d8)}", weight=4, alpha=1, beta=6, gamma="bludgeoning")
    catalog["Sickle"] = Inanimate("Sickle", item_code=1, cost=100, details="A sharp sickle. {Light}", weight=2, alpha=1, beta=6, gamma="slashing")
    catalog["Spear"] = Inanimate("Spear", item_code=1, cost=100, details="A sharpened spear. {Thrown (range 20/60), versatile (1d8)}", weight=3, alpha=1, beta=6, gamma="piercing")

    # # Simple Ranged Weapons
    catalog["Crossbow (Light)"] = Inanimate("Crossbow (Light)", item_code=1, cost=2500, details="A light-weight crossbow. {Ammunition (range 80/320), loading, two-handed}", weight=5, alpha=1, beta=8, gamma="piercing")
    catalog["Dart"] = Inanimate("Dart", item_code=1, cost=5, details="A small, pointed projectile. {Finesse, thrown (range 20/60)}", weight=.25, alpha=1, beta=4, gamma="piercing")
    catalog["Shortbow"] = Inanimate("Shortbow", item_code=1, cost=2500, details="A smaller arrow-shooter. {Ammunition (range 80/320), two-handed}", weight=2, alpha=1, beta=6, gamma="piercing")
    catalog["Sling"] = Inanimate("Sling", item_code=1, cost=10, details="A forked stick with a leather strap. {Ammunition (range 30/120)}", weight=0, alpha=1, beta=4, gamma="bludgeoning")

    # # Martial Melee Weapons
    catalog["Battleaxe"] = Inanimate("Battleaxe", item_code=1, cost=1000, details="An axe, ready for battle. {Versatile (1d10)}", weight=4, alpha=1, beta=8, gamma="slashing")
    catalog["Flail"] = Inanimate("Flail", item_code=1, cost=1000, details="A wooden staff with a short heavy stick swinging from it.", weight=2, alpha=1, beta=8, gamma="bludgeoning")
    catalog["Glaive"] = Inanimate("Glaive", item_code=1, cost=2000, details="A sword. {Heavy, reach, two-handed}", weight=6, alpha=1, beta=10, gamma="slashing")
    catalog["Greataxe"] = Inanimate("Greataxe", item_code=1, cost=3000, details="A large, heavy battleaxe with a double-bladed head. {Heavy, two-handed}", weight=7, alpha=1, beta=12, gamma="slashing")
    catalog["Greatsword"] = Inanimate("Greatsword", item_code=1, cost=5000, details="A massive, two-handed Medieval sword. {Heavy, two-handed}", weight=6, alpha=2, beta=6, gamma="slashing")
    catalog["Halberd"] = Inanimate("Halberd", item_code=1, cost=2000, details="A combined spear and battleaxe. {Heavy, reach, two-handed}", weight=6, alpha=1, beta=10, gamma="slashing")
    catalog["Lance"] = Inanimate("Lance", item_code=1, cost=1000, details="A long weapon for thrusting, having a wooden shaft and a pointed steel head. {Reach, special}", weight=6, alpha=1, beta=12, gamma="piercing")
    catalog["Longsword"] = Inanimate("Longsword", item_code=1, cost=1500, details="A straight double-edged blade. {Versatile (1d10)}", weight=3, alpha=1, beta=8, gamma="slashing")
    catalog["Maul"] = Inanimate("Maul", item_code=1, cost=1000, details="A heavy wooden-headed hammer. {Heavy, two-handed}", weight=10, alpha=2, beta=6, gamma="bludgeoning")
    catalog["Morningstar"] = Inanimate("Morningstar", item_code=1, cost=1500, details="A club with a heavy spiked head.", weight=4, alpha=1, beta=8, gamma="piercing")
    catalog["Pike"] = Inanimate("Pike", item_code=1, cost=500, details="A long wooden shaft with a pointed metal head. {Heavy, reach, two-handed}", weight=18, alpha=1, beta=10, gamma="piercing")
    catalog["Rapier"] = Inanimate("Rapier", item_code=1, cost=2500, details="A thin, light sharp-pointed sword used for thrusting. {Finesse}", weight=2, alpha=1, beta=8, gamma="piercing")
    catalog["Scimitar"] = Inanimate("Scimitar", item_code=1, cost=2500, details="A short sword with a curved blade that broadens toward the point. {Finesse, light}", weight=3, alpha=1, beta=6, gamma="slashing")
    catalog["Shortsword"] = Inanimate("Shortsword", item_code=1, cost=1000, details="A steel shortsword. {Finesse, light}", weight=2, alpha=1, beta=6, gamma="piercing")
    catalog["Trident"] = Inanimate("Trident", item_code=1, cost=500, details="A three-pronged spear. {Thrown (range 20/60), versatile (1d8)}", weight=4, alpha=1, beta=6, gamma="piercing")
    catalog["War Pick"] = Inanimate("War Pick", item_code=1, cost=500, details="A war hammer with a very long spike on the reverse of the hammer head.", weight=2, alpha=1, beta=8, gamma="piercing")
    catalog["Warhammer"] = Inanimate("Warhammer", item_code=1, cost=1500, details="A long-handled metal hammer. {Versatile (1d10)}", weight=2, alpha=1, beta=8, gamma="bludgeoning")
    catalog["Whip"] = Inanimate("Whip", item_code=1, cost=200, details="A strip of leather fastened to a handle. {Finesse, reach}", weight=3, alpha=1, beta=4, gamma="slashing")

    # # Martial Ranged Weapons
    catalog["Blowgun"] = Inanimate("Blowgun", item_code=1, cost=1000, details="A long tube. {Ammunition (range 25/100), loading}", weight=1, alpha=1, beta=1, gamma="piercing")
    catalog["Crossbow (Hand)"] = Inanimate("Crossbow (Hand)", item_code=1, cost=7500, details="A smaller crossbow. {Ammunition (range 30/120), light, loading}", weight=3, alpha=1, beta=6, gamma="piercing")
    catalog["Crossbow (Heavy)"] = Inanimate("Crossbow (Heavy)", item_code=1, cost=5000, details="A heavy-weight crossbow. {Ammunition (range 100/400), heavy, loading, two-handed}", weight=18, alpha=1, beta=10, gamma="piercing")
    catalog["Longbow"] = Inanimate("Longbow", item_code=1, cost=5000, details="A large bow drawn by hand. {Ammunition (range 150/600), heavy, two-handed}", weight=2, alpha=1, beta=8, gamma="piercing")
    catalog["Net"] = Inanimate("Net", item_code=1, cost=100, details="An open-meshed fabric woven together at regular intervals. {Special, thrown (range 5/15)}", weight=3)

    # Armor ============================================================================================================
    # # Light Armor
    catalog["Padded Armor"] = Inanimate("Padded Armor", item_code=2, cost=500, details="Provides +11 AC", weight=8, alpha=11, beta="dexterity", gamma=True)
    catalog["Leather Armor"] = Inanimate("Leather Armor", item_code=2, cost=1000, details="Provides +11 AC", weight=10, alpha=11, beta="dexterity")
    catalog["Studded Leather Armor"] = Inanimate("Studded Leather Armor", item_code=2, cost=4500, details="Provides +12 AC", weight=13,alpha=12, beta="dexterity")

    # # Medium Armor
    catalog["Hide Armor"] = Inanimate("Hide Armor", item_code=2, cost=1000, details="Provides +12 AC", weight=12, alpha=12, beta="dexterity")
    catalog["Chain Shirt"] = Inanimate("Chain Shirt", item_code=2, cost=5000, details="Provides +13 AC", weight=20, alpha=13, beta="dexterity")
    catalog["Scale Mail"] = Inanimate("Scale Mail", item_code=2, cost=5000, details="Provides +14 AC", weight=45, alpha=14, beta="dexterity", gamma=True)
    catalog["Breastplate"] = Inanimate("Breastplate", item_code=2, cost=40000, details="Provides +14 AC", weight=20, alpha=14, beta="dexterity")
    catalog["Half Plate"] = Inanimate("Half Plate", item_code=2, cost=75000, details="Provides +15 AC", weight=40, alpha=15, beta="dexterity", gamma=True)

    # # Heavy Armor
    catalog["Ring Mail"] = Inanimate("Ring Mail", item_code=2, cost=3000, details="Provides +14 AC", weight=40, alpha=14, beta=None, gamma=True)
    catalog["Chain Mail"] = Inanimate("Chain Mail", item_code=2, cost=7500, details="Provides +16 AC", weight=55, alpha=16, beta=None, gamma=True)
    catalog["Splint Armor"] = Inanimate("Splint Armor", item_code=2, cost=20000, details="Provides +17 AC", weight=60, alpha=17, beta=None, gamma=True)
    catalog["Plate Armor"] = Inanimate("Plate Armor", item_code=2, cost=150000, details="Provides +18 AC", weight=65, alpha=18, beta=None, gamma=True)

    # # Shield
    catalog["Shield"] = Inanimate("Shield", item_code=2, cost=1000, details="Provides +2 AC", weight=6, alpha=2, beta=None, gamma=False)

    # catalog[""] = Inanimate("", item_code=3, cost=, details="", max_stack=100, weight=, alpha="", beta=1.0)
    # Adventuring Gear =================================================================================================
    # TYPES LISTED: weapon, medicine, ammunition, utility
    # # Consumable
    catalog["Acid (Vial)"] = Inanimate("Acid (Vial)", item_code=3, cost=2500, details="Can be thrown 5-20 feet away, shattering on impact. Counts as a ranged attack against a creature/object. If it hits, target takes 2d6 acid damage.", max_stack=100, weight=1, alpha="weapon", beta=1.0)
    catalog["Alchemist's Fire (Flask)"] = Inanimate("Alchemist's Fire (Flask)", item_code=3, cost=5000, details="A sticky adhesive fluid that ignites when exposed to air. Can be thrown up to 20 feet, shatters on impact. Counts as a ranged attack against a creature/object. If it hits, target takes 1d4 fire damage at the start of each turn.", max_stack=100, weight=1, alpha="weapon", beta=1.0)
    catalog["Arrows (20)"] = Inanimate("Arrows (20)", item_code=3, cost=100, details="Arrows are used with a weapon that has the ammunition property to make a ranged attack.", max_stack=100, weight=1, alpha="ammunition", beta=1.0)
    catalog["Blowgun Needles (50)"] = Inanimate("Blowgun Needles (50)", item_code=3, cost=100, details="Blowgun needles are used with a weapon that has the ammunition property to make a ranged attack.", max_stack=100, weight=1, alpha="ammunition", beta=1.0)
    catalog["Crossbow Bolts (20)"] = Inanimate("Crossbow Bolts (20)", item_code=3, cost=100, details="Crossbow bolts are used with a weapon that has the ammunition property to make a ranged attack.", max_stack=100, weight=1.5, alpha="ammunition", beta=1.0)
    catalog["Sling Bullets (20)"] = Inanimate("Sling Bullets (20)", item_code=3, cost=4, details="Sling bullets are used with a weapon that has the ammunition property to make a ranged attack.", max_stack=100, weight=1.5, alpha="ammunition", beta=1.0)
    catalog["Antitoxin (Vial)"] = Inanimate("Antitoxin (Vial)", item_code=3, cost=5000, details="A creature that drinks this vial of liquid gains advantage on saving throws against poison for 1 hour. It confers no benefit to undead or constructs.", max_stack=100, weight=0, alpha="medicine", beta=1.0)
    catalog["Ball Bearings (Bag of 1,000)"] = Inanimate("Ball Bearings (Bag of 1,000)", item_code=3, cost=100, details="As an action, you can spill these tiny metal balls from their pouch to cover a level area 10 feet square. A creature moving across the covered area must succeed on a DC 10 Dexterity saving throw or fall prone. A creature moving through the area at half speed doesn’t need to make the saving throw.", max_stack=100, weight=2, alpha="weapon", beta=1.0)
    catalog["Caltrops (Bag of 20)"] = Inanimate("Caltrops (Bag of 20)", item_code=3, cost=100, details="As an action, you can spread a single bag of caltrops to cover a 5-foot-square area. Any creature that enters the area must succeed on a DC 15 Dexterity saving throw or stop moving and take 1 piercing damage. Until the creature regains at least 1 hit point, its walking speed is reduced by 10 feet. A creature moving through the area at half speed doesn’t need to make the saving throw.", max_stack=100, weight=2, alpha="weapon", beta=1.0)
    catalog["Candle"] = Inanimate("Candle", item_code=3, cost=1, details="For 1 hour, a candle sheds bright light in a 5-foot radius and dim light for an additional 5 feet.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    catalog["Chalk (1 piece)"] = Inanimate("Chalk (1 piece)", item_code=3, cost=1, details="A piece of chalk used for writing and marking on various surfaces.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    catalog["Healer's Kit"] = Inanimate("Healer's Kit", item_code=3, cost=500, details="This kit is a leather pouch containing bandages, salves, and splints. The kit has ten uses. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check.", max_stack=100, weight=3, alpha="medicine", beta=1.0)
    catalog["Holy Water (Flask)"] = Inanimate("Holy Water (Flask)", item_code=3, cost=2500, details="As an action, you can splash the contents of this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. In either case, make a ranged attack against a target creature, treating the holy water as an improvised weapon. If the target is a fiend or undead, it takes 2d6 radiant damage.", max_stack=100, weight=1, alpha="weapon", beta=1.0)
    catalog["Ink (1 ounce bottle)"] = Inanimate("Ink (1 ounce bottle)", item_code=3, cost=1000, details="Ink is typically used with an ink pen to write.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    catalog["Oil (Flask)"] = Inanimate("Oil (Flask)", item_code=3, cost=10, details="Oil usually comes in a clay flask that holds 1 pint. As an action, you can splash the oil in this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. Make a ranged attack against a target creature or object, treating the oil as an improvised weapon. On a hit, the target is covered in oil. If the target takes any fire damage before the oil dries (after 1 minute), the target takes an additional 5 fire damage from the burning oil. You can also pour a flask of oil on the ground to cover a 5-foot-square area, provided that the surface is level. If lit, the oil burns for 2 rounds and deals 5 fire damage to any creature that enters the area or ends its turn in the area. A creature can take this damage only once per turn.", max_stack=100, weight=1, alpha="utility", beta=1.0)
    catalog["Perfume (Vial)"] = Inanimate("Perfume (Vial)", item_code=3, cost=500, details="A fragrant commodity typically used by the wealthy.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    catalog["Basic Poison (Vial)"] = Inanimate("Basic Poison (Vial)", item_code=3, cost=10000, details="You can use the poison in this vial to coat one slashing or piercing weapon or up to three pieces o f ammunition. Applying the poison takes an action. A creature hit by the poisoned weapon or ammunition must make a DC 10 Constitution saving throw or take 1d4 poison damage. Once applied, the poison retains potency for 1 minute before drying.", max_stack=100, weight=0, alpha="weapon", beta=1.0)
    catalog["Potion of Healing"] = Inanimate("Potion of Healing", item_code=3, cost=5000, details="A character who drinks the magical red fluid in this vial regains 2d4 + 2 hit points. Drinking or administering a potion takes an action.", max_stack=100, weight=0.5, alpha="medicine", beta=1.0)
    catalog["Rations (1 day)"] = Inanimate("Rations (1 day)", item_code=3, cost=50, details="Rations consist of dry foods suitable for extended travel, including jerky, dried fruit, hardtack, and nuts.", max_stack=100, weight=2, alpha="utility", beta=1.0)
    catalog["Sealing Wax"] = Inanimate("Sealing Wax", item_code=3, cost=50, details="Wax melted to seal letters. When you press a signet ring into warm sealing wax, you leave an identifying mark.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    catalog["Soap"] = Inanimate("Soap", item_code=3, cost=2, details="A commodity used for bathing.", max_stack=100, weight=0, alpha="utility", beta=1.0)
    catalog["Iron Spikes (10)"] = Inanimate("Iron Spikes (10)", item_code=3, cost=100, details="Standard iron spikes typically used with a hammer.", max_stack=100, weight=5, alpha="aid", beta=1.0)
    catalog["Torch"] = Inanimate("Torch", item_code=3, cost=1, details="A torch burns for 1 hour, providing bright light in a 20-foot radius and dim light for an additional 20 feet. If you make a melee attack with a burning torch and hit, it deals 1 fire damage.", max_stack=100, weight=1, alpha="utility", beta=1.0)

    catalog["Mana Potion"] = Inanimate("Mana Potion", item_code=3, cost=5000, details="Restores Mana", max_stack=6, weight=0.5, alpha="medicine", beta=1.0)

    # catalog[""] = Inanimate("", item_code=4, cost=, details="", max_stack=100, weight=)
    # # Non-Consumable
    catalog["Abacus"] = Inanimate("Abacus", item_code=4, cost=200, details="A calculating tool", max_stack=100, weight=2)
    catalog["Arcane Focus - Crystal"] = Inanimate("Arcane Focus Crystal", item_code=4, cost=1000, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=1)
    catalog["Arcane Focus - Orb"] = Inanimate("Arcane Focus Orb", item_code=4, cost=2000, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=3)
    catalog["Arcane Focus - Rod"] = Inanimate("Arcane Focus Rod", item_code=4, cost=1000, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=2)
    catalog["Arcane Focus - Staff"] = Inanimate("Arcane Focus Staff", item_code=4, cost=500, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=4)
    catalog["Arcane Focus - Wand"] = Inanimate("Arcane Focus Wand", item_code=4, cost=1000, details="A special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spellcasting focus.", max_stack=100, weight=1)
    catalog["Backpack"] = Inanimate("Backpack", item_code=4, cost=200, details="A backpack is a leather pack carried on the back, typically with straps to secure it. A backpack can hold 1 cubic foot/  30 pounds of gear. You can also strap items, such as a bedroll or a coil of rope, to the outside of a backpack", max_stack=100, weight=5)
    catalog["Barrel"] = Inanimate("Barrel", item_code=4, cost=200, details="A barrel can hold 40 gallons of liquid or 4 cubic feet of solid material.", max_stack=100, weight=70)
    catalog["Basket"] = Inanimate("Basket", item_code=4, cost=40, details="A basket can hold 2 cubic feet / 40 pounds of gear.", max_stack=100, weight=2)
    catalog["Bedroll"] = Inanimate("Bedroll", item_code=4, cost=100, details="You never know where you’re going to sleep, and a bedroll helps you get better sleep in a hayloft or on the cold ground. A bedroll consists of bedding and a blanket thin enough to be rolled up and tied. In an emergency, it can double as a stretcher.", max_stack=100, weight=7)
    catalog["Bell"] = Inanimate("Bell", item_code=4, cost=100, details="A standard bell that rings, typically used for signaling.", max_stack=100, weight=0)
    catalog["Blanket"] = Inanimate("Blanket", item_code=4, cost=50, details="A thick, quilted, blanket made to keep you warm in cold weather.", max_stack=100, weight=3)
    catalog["Block and Tackle"] = Inanimate("Block and Tackle", item_code=4, cost=100, details="A set of pulleys with a cable threaded through them and a hook to attach to objects, a block and tackle allows you to hoist up to four times the weight you can normally lift.", max_stack=100, weight=5)
    catalog["Book"] = Inanimate("Book", item_code=4, cost=2500, details="A book might contain poetry, historical accounts, information pertaining to a particular field of lore, diagrams and notes on gnomish contraptions, or just about anything else that can be represented using text or pictures. ", max_stack=100, weight=5)
    catalog["Bottle (Glass)"] = Inanimate("Bottle (Glass)", item_code=4, cost=200, details="A bottle can hold 1 1/2 pints of liquid.", max_stack=100, weight=2)
    catalog["Bucket"] = Inanimate("Bucket", item_code=4, cost=5, details="A bucket can hold 3 gallons of liquid, or 1/2 cubic foot of solid material.", max_stack=100, weight=2)
    catalog["Crossbow Bold Case"] = Inanimate("Crossbow Bolt Case", item_code=4, cost=100, details="This wooden case can hold up to twenty crossbow bolts.", max_stack=100, weight=1)
    catalog["Map or Scroll Case"] = Inanimate("Map or Scroll Case", item_code=4, cost=100, details="This cylindrical leather case can hold up to ten rolled-up sheets of paper or five rolled-up sheets of parchment.", max_stack=100, weight=1)
    catalog["Chain (10 feet)"] = Inanimate("Chain (10 Feet)", item_code=4, cost=500, details="A chain has 10 hit points. It can be burst with a successful DC 20 Strength check.", max_stack=100, weight=10)
    catalog["Chest"] = Inanimate("Chest", item_code=4, cost=500, details="A chest can hold 12 cubic feet / 300 pounds of gear.", max_stack=100, weight=25)
    catalog["Climber's Kit"] = Inanimate("Climber's Kit", item_code=4, cost=2500, details="A climber's kit includes special pitons, boot tips, gloves, and a harness. You can use the climber's kit as an action to anchor yourself; when you do, you can't fall more than 25 feet from the point where you anchored yourself, and you can't climb more than 25 feet away from that point without undoing the anchor.", max_stack=100, weight=12)
    catalog["Clothes (Common)"] = Inanimate("Clothes (Common)", item_code=4, cost=50, details="This set of clothes could consist of a loose shirt and baggy breeches, or a loose shirt and skirt or overdress. Cloth wrappings are used for shoes.", max_stack=100, weight=3)
    catalog["Clothes (Costume)"] = Inanimate("Clothes (Costume)", item_code=4, cost=500, details="This set of clothes is fashioned after a particular costume, typically meant for entertaining.", max_stack=100, weight=4)
    catalog["Clothes (Fine)"] = Inanimate("Clothes (Fine)", item_code=4, cost=1500, details="This set of clothes is designed specifically to be expensive and to show it, including fancy, tailored clothes in whatever fashion happens to be the current style in the courts of the nobles. Precious metals and gems could be worked into the clothing.", max_stack=100, weight=6)
    catalog["Clothes (Traveler's)"] = Inanimate("Clothes (Traveler's)", item_code=4, cost=200, details="This set of clothes could consist of boots, a wool skirt or breeches, a sturdy belt, a shirt (perhaps with a vest or jacket), and an ample cloak with a hood.", max_stack=100, weight=4)
    catalog["Component Pouch"] = Inanimate("Component Pouch", item_code=4, cost=2500, details="A component pouch is a small, watertight leather belt pouch that has compartments to hold all the material components and other special items you need to cast your spells, except for those components that have a specific cost.", max_stack=100, weight=2)
    catalog["Crowbar"] = Inanimate("Crowbar", item_code=4, cost=200, details="Using a crowbar grants advantage to Strength checks where the crowbar's leverage can be applied.", max_stack=100, weight=5)
    catalog["Druidic Focus - Sprig of Mistletoe"] = Inanimate("Druidic Focus - Sprig of Mistletoe", item_code=4, cost=100, details="A druidic focus might be a sprig of mistletoe or holly, a wand or scepter made of yew or another special wood, a staff drawn whole out of a living tree, or a totem object incorporating feathers, fur, bones, and teeth from sacred animals. A druid can use such an object as a spellcasting focus.", max_stack=100, weight=0)
    catalog["Druidic Focus - Totem"] = Inanimate("Druidic Focus - Totem", item_code=4, cost=100, details="A druidic focus might be a sprig of mistletoe or holly, a wand or scepter made of yew or another special wood, a staff drawn whole out of a living tree, or a totem object incorporating feathers, fur, bones, and teeth from sacred animals. A druid can use such an object as a spellcasting focus.", max_stack=100, weight=0)
    catalog["Druidic Focus - Wooden Staff"] = Inanimate("Druidic Focus - Wooden Staff", item_code=4, cost=500, details="A druidic focus might be a sprig of mistletoe or holly, a wand or scepter made of yew or another special wood, a staff drawn whole out of a living tree, or a totem object incorporating feathers, fur, bones, and teeth from sacred animals. A druid can use such an object as a spellcasting focus.", max_stack=100, weight=4)
    catalog["Druidic Focus - Yew Wand"] = Inanimate("Druidic Focus - Yew Wand", item_code=4, cost=1000, details="A druidic focus might be a sprig of mistletoe or holly, a wand or scepter made of yew or another special wood, a staff drawn whole out of a living tree, or a totem object incorporating feathers, fur, bones, and teeth from sacred animals. A druid can use such an object as a spellcasting focus.", max_stack=100, weight=1)
    catalog["Fishing Tackle"] = Inanimate("Fishing Tackle", item_code=4, cost=100, details="This kit includes a wooden rod, silken line, corkwood bobbers, steel hooks, lead sinkers, velvet lures, and narrow netting.", max_stack=100, weight=4)
    catalog["Flask"] = Inanimate("Flask", item_code=4, cost=2, details="Can hold 1 pint of liquid.", max_stack=100, weight=1)
    catalog["Tankard"] = Inanimate("Tankard", item_code=4, cost=2, details="Can hold 1 pint of liquid.", max_stack=100, weight=1)
    catalog["Grappling Hook"] = Inanimate("Grappling Hook", item_code=4, cost=200, details="When tied to the end of a rope, a grappling hook can secure the rope to a battlement, window ledge, tree limb, or other protrusion.", max_stack=100, weight=4)
    catalog["Hammer"] = Inanimate("Hammer", item_code=4, cost=100, details="A one-handed hammer with an iron head.", max_stack=100, weight=3)
    catalog["Sledgehammer"] = Inanimate("Sledgehammer", item_code=4, cost=200, details="A two-handed, iron-headed hammer.", max_stack=100, weight=10)
    catalog["Holy Symbol - Amulet"] = Inanimate("Holy Symbol - Amulet", item_code=4, cost=500, details="A representation of a god or pantheon. A cleric or paladin can use a holy symbol as a spellcasting focus. To use the symbol in this way, the caster must hold it in hand, wear it visibly, or bear it on a shield.", max_stack=100, weight=1)
    catalog["Holy Symbol - Emblem"] = Inanimate(" Holy Symbol - Emblem", item_code=4, cost=500, details="A representation of a god or pantheon. A cleric or paladin can use a holy symbol as a spellcasting focus. To use the symbol in this way, the caster must hold it in hand, wear it visibly, or bear it on a shield.", max_stack=100, weight=0)
    catalog["Holy Symbol - Reliquary"] = Inanimate("Holy Symbol - Reliquary", item_code=4, cost=500, details="A representation of a god or pantheon. A cleric or paladin can use a holy symbol as a spellcasting focus. To use the symbol in this way, the caster must hold it in hand, wear it visibly, or bear it on a shield.", max_stack=100, weight=2)
    catalog["Hourglass"] = Inanimate("Hourglass", item_code=4, cost=2500, details="A standard hourglass used to measure the passage of time.", max_stack=100, weight=1)
    catalog["Hunting Trap"] = Inanimate("Hunting Trap", item_code=4, cost=500, details="When you use your action to set it, this trap forms a saw-toothed steel ring that snaps shut when a creature steps on a pressure plate in the center. The trap is affixed by a heavy chain to an immobile object, such as a tree or a spike driven into the ground. A creature that steps on the plate must succeed on a DC 13 Dexterity saving throw or take 1d4 piercing damage and stop moving. Thereafter, until the creature breaks free of the trap, its movement is limited by the length of the chain (typically 3 feet long). A creature can use its action to make a DC 13 Strength check, freeing itself or another creature within its reach on a success. Each failed check deals 1 piercing damage to the trapped creature.", max_stack=100, weight=25)
    catalog["Ink Pen"] = Inanimate("Ink Pen", item_code=4, cost=2, details="A wooden stick with a special tip on the end. The tip draws ink in when dipped in a vial and leaves an ink trail when drawn across a surface.", max_stack=100, weight=0)
    catalog["Jug"] = Inanimate("Jug", item_code=4, cost=2, details="Can hold 1 gallon of liquid.", max_stack=100, weight=4)
    catalog["Pitcher"] = Inanimate("Pitcher", item_code=4, cost=2, details="Can hold 1 gallon of liquid.", max_stack=100, weight=4)
    catalog["Ladder (10-foot)"] = Inanimate("Ladder (10-foot)", item_code=4, cost=10, details="A straight, simple wooden ladder.", max_stack=100, weight=25)
    catalog["Lamp"] = Inanimate("Lamp", item_code=4, cost=50, details="A lamp casts bright light in a 15-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil.", max_stack=100, weight=1)
    catalog["Lantern (Bullseye)"] = Inanimate("Lantern (Bullseye)", item_code=4, cost=1000, details="Casts bright light in a 60-foot cone and dim light for an additional 60 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil.", max_stack=100, weight=2)
    catalog["Lantern (Hooded)"] = Inanimate("Lantern (Hooded)", item_code=4, cost=500, details="A hooded lantern casts bright light in a 30-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil. As an action, you can lower the hood, reducing the light to dim light in a 5-foot radius.", max_stack=100, weight=2)
    catalog["Lock"] = Inanimate("Lock", item_code=4, cost=1000, details="A key is provided with the lock. Without the key, a creature proficient with thieves' tools can pick this lock with a successful DC 15 Dexterity check.", max_stack=100, weight=1)
    catalog["Magnifying Glass"] = Inanimate("Magnifying Glass", item_code=4, cost=10000, details="This lens allows a closer look at small objects. It is also useful as a substitute for flint and steel when starting fires. Lighting a fire with a magnifying glass requires light as bright as sunlight to focus, tinder to ignite, and about 5 minutes for the fire to ignite. A magnifying glass grants advantage on any ability check made to appraise or inspect an item that is small or highly detailed.", max_stack=100, weight=0)
    catalog["Manacles"] = Inanimate("Manacles", item_code=4, cost=200, details="These metal restraints can bind a Small or Medium creature. Escaping the manacles requires a successful DC 20 Dexterity check. Breaking them requires a successful DC 20 Strength check. Each set of manacles comes with one key. Without the key, a creature proficient with thieves' tools can pick the manacles' lock with a successful DC 15 Dexterity check. Manacles have 15 hit points.", max_stack=100, weight=6)
    catalog["Mess Kit"] = Inanimate("Mess Kit", item_code=4, cost=20, details="This tin box contains a cup and simple cutlery. The box clamps together, and one side can be used as a cooking pan and the other as a plate or shallow bowl.", max_stack=100, weight=1)
    catalog["Mirror (Steel)"] = Inanimate("Mirror (Steel)", item_code=4, cost=500, details="A reflective surface.", max_stack=100, weight=.5)
    catalog["Paper (One sheet)"] = Inanimate("Paper (One sheet)", item_code=4, cost=20, details="A sheet of standard paper. Made from cloth fibers.", max_stack=100, weight=0)
    catalog["Parchment (One sheet)"] = Inanimate("Parchment (One sheet)", item_code=4, cost=10, details="A piece of goat hide or sheepskin that has been prepared for writing on.", max_stack=100, weight=10)
    catalog["Miner's Pick"] = Inanimate("Miner's Pick", item_code=4, cost=200, details="A miner's pick is designed to concentrate the force of its blow on a small area.", max_stack=100, weight=10)
    catalog["Piton"] = Inanimate("Piton", item_code=4, cost=5, details="A piton is a steel spike with an eye through which you can loop a rope.", max_stack=100, weight=.25)
    catalog["Pole (10-foot)"] = Inanimate("Pole (10-foot)", item_code=4, cost=5, details="A long, slender, rounded piece of wood or metal,", max_stack=100, weight=7)
    catalog["Iron Pot"] = Inanimate("Iron Pot", item_code=4, cost=200, details="An iron pot can hold 1 gallon of liquid.", max_stack=100, weight=10)
    catalog["Pouch"] = Inanimate("Pouch", item_code=4, cost=50, details="A cloth or leather pouch can hold up to 20 sling bullets or 50 blowgun needles, among other things.", max_stack=100, weight=1)
    catalog["Quiver"] = Inanimate("Quiver", item_code=4, cost=100, details="A quiver can hold up to 20 arrows.", max_stack=100, weight=1)
    catalog["Portable Ram"] = Inanimate("Portable Ram", item_code=4, cost=400, details="You can use a portable ram to break down doors. When doing so, you gain a +4 bonus on the Strength check. One other character can help you use the ram, giving you advantage on this check.", max_stack=100, weight=35)
    catalog["Robes"] = Inanimate("Robes", item_code=4, cost=100, details="A standard set of robes.", max_stack=100, weight=4)
    catalog["Hempen Rope (50 Feet)"] = Inanimate("Hempen Rope (50 Feet)", item_code=4, cost=100, details="Rope has 2 hit points and can be burst with a DC 17 Strength check.", max_stack=100, weight=10)
    catalog["Silk Rope (50 Feet)"] = Inanimate("Silk Rope (50 Feet)", item_code=4, cost=1000, details="Rope has 2 hit points and can be burst with a DC 17 Strength check.", max_stack=100, weight=5)
    catalog["Sack"] = Inanimate("Sack", item_code=4, cost=1, details="A sack can hold 1 cubic foot / 30 pounds of gear.", max_stack=100, weight=.5)
    catalog["Merchant's Scale"] = Inanimate("Merchant's Scale", item_code=4, cost=500, details="A scale includes a small balance, pans, and a suitable assortment of weights up to 2 pounds. With it, you can measure the exact weight of small objects, such as raw precious metals or trade goods, to help determine their worth.", max_stack=100, weight=3)
    catalog["Shovel"] = Inanimate("Shovel", item_code=4, cost=200, details="A standard shovel used for digging.", max_stack=100, weight=5)
    catalog["Signal Whistle"] = Inanimate("Signal Whistle", item_code=4, cost=5, details="A small whistle used for signaling.", max_stack=100, weight=0)
    catalog["Signet Ring"] = Inanimate("Signet Ring", item_code=4, cost=500, details="Each signet ring has a distinctive design carved into it. When you press this ring into warm sealing wax, you leave an identifying mark.", max_stack=100, weight=0)
    catalog["Spellbook"] = Inanimate("Spellbook", item_code=4, cost=5000, details="Essential for wizards, a spellbook is a leather-bound tome with 100 blank vellum pages suitable for recording spells.", max_stack=100, weight=3)
    catalog["Spyglass"] = Inanimate("Spyglass", item_code=4, cost=100000, details="Objects viewed through a spyglass are magnified to twice their size.", max_stack=100, weight=1)
    catalog["Tent (Two-Person)"] = Inanimate("Tent (Two-Person)", item_code=4, cost=200, details="A simple and portable canvas shelter, a tent sleeps two.", max_stack=100, weight=20)
    catalog["Tinderbox"] = Inanimate("Tinderbox", item_code=4, cost=50, details="This small container holds flint, fire steel, and tinder (usually dry cloth soaked in light oil) used to kindle a fire. Using it to light a torch -- or anything else with abundant, exposed fuel -- takes an action. Lighting any other fire takes 1 minute.", max_stack=100, weight=1)
    catalog["Vial"] = Inanimate("Vial", item_code=4, cost=100, details="A small glass container. Can hold 4 ounces of liquid.", max_stack=100, weight=0)
    catalog["Waterskin"] = Inanimate("Waterskin", item_code=4, cost=20, details="Can hold 4 pints of liquid. Weighs 5 lbs. when full.", max_stack=100, weight=5)
    catalog["Whetstone"] = Inanimate("Whetstone", item_code=4, cost=1, details="A standard whetstone used to sharpen blades.", max_stack=100, weight=1)

    # Tools ============================================================================================================
    # # Consumable

    # Mounts & Vehicles ================================================================================================

    # Trade Goods ======================================================================================================


    # Food & Drink =====================================================================================================
    catalog["Ale (Gallon)"] = Inanimate("Ale (Gallon)", item_code=3, cost=20, details="A type of beer with a bitter flavor and higher alcoholic content. Now served by the gallon.", max_stack=100, alpha="drink", beta=1.0)
    catalog["Ale (Mug)"] = Inanimate("Ale (Mug)", item_code=3, cost=4, details="A type of beer with a bitter flavor and higher alcoholic content. Now served by the mug.", max_stack=100, alpha="drink", beta=1.0)
    catalog["Banquet (per person)"] = Inanimate("Banquet (per person)", item_code=3, cost=1000, details="An elaborate and formal meal", max_stack=100,alpha="food", beta=1.0)
    catalog["Bread (Loaf)"] = Inanimate("Bread (Loaf)", item_code=3, cost=2, details="A standard loaf of white bread.", max_stack=100, alpha="food", beta=1.0)
    catalog["Cheese (Hunk)"] = Inanimate("Cheese (Hunk)", item_code=3, cost=10, details="A dairy product, derived from milk.", max_stack=100, alpha="food", beta=1.0)
    catalog["Meat (Chunk)"] = Inanimate("Meat (Chunk)", item_code=3, cost=30, details="A chunk of roasted animal flesh.", max_stack=100, alpha="food", beta=1.0)
    catalog["Common Wine (Pitcher)"] = Inanimate("Common Wine (Pitcher)", item_code=3, cost=20, details="An alcoholic drink made from fermented grape juice. Cheap but it gets the job done.", max_stack=100, alpha="food", beta=1.0)
    catalog["Fine Wine (Bottle)"] = Inanimate("Fine Wine (Bottle)", item_code=3, cost=1000, details="An alcoholic drink made from fermented grape juice. The bottle looks quite luxurious.", max_stack=100, alpha="food", beta=1.0)

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
