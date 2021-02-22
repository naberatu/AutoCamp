
import pickle
from enemy import Enemy


c_monsters = dict()

try:
    c_monsters = pickle.load(open("monsters.camp", "rb"))
except:
    #c_items[""] = Enemy("", AC=, HP=, speed=(, , , , ), abs=(, , , , , ), saving_throws={}, skills={}, dmg_resist=[], dmg_immune=[], dmg_vuln=[], cond_immune=[], exp=)

    # ================================================ A ===================================================================
    c_monsters["Aarakocra"] = Enemy("Aarakocra", AC=12, HP=13, speed=(20, 50, 0, 0, 0), abs=(10, 14, 10, 11, 12, 11), skills={"Perception": 5}, exp=50)
    c_monsters["Aboleth"] = Enemy("Aboleth", AC=17, HP=135, speed=(10, 0, 40, 0, 0), abs=(21, 9, 15, 18, 15, 18), saving_throws={"Constitution": 6, "Intellect": 8, "Wisdom": 6}, skills={"History": 12, "Perception": 10}, exp=5900)

    # # Angels
    c_monsters["Deva"] = Enemy("Deva", AC=17, HP=136, speed=(30, 90, 0, 0, 0), abs=(18, 18, 18, 17, 20, 20), saving_throws={"Wisdom": 9, "Charisma": 9}, skills={"Insight": 7, "Perception": 9}, dmg_resist=["radiant", "bludgeoning", "piercing", "slashing (nonmagical weapons)"], cond_immune=["Charmed", "Exhausted", "Frightened"], exp=5900)
    c_monsters["Planetar"] = Enemy("Planetar", AC=19, HP=200, speed=(40, 120, 0, 0, 0), abs=(24, 20, 24, 19, 22, 25), saving_throws={"Constitution": 12, "Wisdom": 11, "Charisma": 12}, skills={"Perception": 11}, dmg_resist=["radiant", "bludgeoning", "piercing", "slashing (nonmagical weapons)"], cond_immune=["Charmed", "Exhausted", "Frightened"], exp=15000)
    c_monsters["Solar"] = Enemy("Solar", AC=21, HP=243, speed=(50, 150, 0, 0, 0), abs=(26, 22, 26, 25, 25, 30), saving_throws={"Intelligence": 14, "Wisdom": 14, "Charisma": 17}, skills={"Perception": 14}, dmg_resist=["radiant", "bludgeoning", "piercing", "slashing (nonmagical weapons)"], dmg_immune=["necrotic", "poison"], cond_immune=["Charmed", "Exhausted", "Frightened", "Poisoned"], exp=33000)

    # # Animated Objects
    c_monsters["Animated Armor"] = Enemy("Animated Armor", AC=18, HP=33, speed=(25, 0, 0, 0, 0), abs=(14, 11, 13, 1, 3, 1), dmg_immune=["poison", "psychic"], cond_immune=["Blinded", "Charmed", "Deafened", "Exhausted", "Frightened", "Paralyzed", "Petrified", "Poisoned"], exp=200)
    c_monsters["Flying Sword"] = Enemy("Flying Sword", AC=17, HP=17, speed=(0, 50, 0, 0, 0), abs=(12, 15, 11, 1, 5, 1), saving_throws={"Dexterity": 4}, dmg_immune=["poison", "psychic"], cond_immune=["Blinded", "Charmed", "Deafened", "Frightened", "Paralyzed", "Petrified", "Poisoned"], exp=50)
    c_monsters["Rug of Smothering"] = Enemy("Rug of Smothering", AC=12, HP=33, speed=(10, 0, 0, 0, 0), abs=(17, 14, 10, 1, 3, 1), dmg_immune=["poison", "psychic"], cond_immune=["Blinded", "Charmed", "Deafened", "Frightened", "Paralyzed", "Petrified", "Poisoned"], exp=450)

    c_monsters["Ankheg"] = Enemy("Ankheg", AC=14, HP=39, speed=(30, 0, 0, 10, 0), abs=(17, 11, 13, 1, 13, 6), exp=450)
    c_monsters["Azer"] = Enemy("Azer", AC=17, HP=39, speed=(30, 0, 0, 0, 0), abs=(17, 12, 15, 12, 13, 10), saving_throws={"Constitution": 4}, dmg_immune=["fire", "poison"], cond_immune=["Poisoned"], exp=450)

    # ================================================ B ===================================================================
    c_monsters["Banshee"] = Enemy("Banshee", AC=12, HP=58, speed=(0, 40, 0, 0, 0), abs=(0, 14, 10, 12, 11, 17), saving_throws={"Wisdom": 2, "Charisma": 4}, dmg_resist=["acid", "fire", "lightning", "thunder", "bludgeoning", "piercing", "slashing (nonmagical weapons)"], dmg_immune=["cold", "necrotic", "poison"], cond_immune=["Charmed", "Exhausted", "Frightened", "Grappled", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained"], exp=1100)
    c_monsters["Basilisk"] = Enemy("Basilisk", AC=15, HP=52, speed=(20, 0, 0, 0, 0), abs=(16, 8, 15, 2, 8, 7), exp=700)
    c_monsters["Behir"] = Enemy("Behir", AC=17, HP=168, speed=(50, 0, 0, 0, 40), abs=(23, 16, 18, 7, 14, 12), skills={"Perception": 6, "Stealth": 7}, dmg_immune=["lightning"], exp=7200)

    # # Beholders
    c_monsters["Beholder"] = Enemy("Beholder", AC=18, HP=180, speed=(0, 20, 0, 0, 0), abs=(10, 14, 18, 17, 15, 17), saving_throws={"Intellect": 8, "Wisdom": 7, "Charisma": 8}, skills={"Perception": 12}, cond_immune=["Prone"], exp=10000)
    c_monsters["Death Tyrant"] = Enemy("Death Tyrant", AC=19, HP=187, speed=(0, 20, 0, 0, 0), abs=(10, 14, 14, 19, 15, 19), saving_throws={"Strength": 5, "Constitution": 7, "Intellect": 9, "Wisdom": 7, "Charisma": 9}, skills={"Perception": 12}, dmg_immune=["poison"], cond_immune=["Charmed", "Exhausted", "Paralyzed", "Petrified", "Poisoned", "Prone"], exp=11500)
    c_monsters["Spectator"] = Enemy("Spectator", AC=14, HP=39, speed=(0, 30, 0, 0, 0), abs=(8, 14, 14, 13, 14, 11), skills={"Perception": 6}, cond_immune=["Prone"], exp=700)

    # # Blights
    c_monsters["Needle Blight"] = Enemy("Needle Blight", AC=12, HP=11, speed=(30, 0, 0, 0, 0), abs=(12, 12, 13, 4, 8, 3), cond_immune=["Blinded", "Deafened"], exp=50)
    c_monsters["Twig Blight"] = Enemy("Twig Blight", AC=13, HP=4, speed=(20, 0, 0, 0, 0), abs=(6, 13, 12, 4, 8, 3), skills={"Stealth": 3}, dmg_vuln=["fire"], cond_immune=["Blinded", "Deafened"], exp=25)
    c_monsters["Vine Blight"] = Enemy("Vine Blight", AC=12, HP=26, speed=(10, 0, 0, 0, 0), abs=(15, 8, 14, 5, 10, 3), skills={"Stealth": 1}, cond_immune=["Blinded", "Deafened"], exp=100)

    # # Bugbears
    c_monsters["Bugbear"] = Enemy("Bugbear", AC=16, HP=27, speed=(30, 0, 0, 0, 0), abs=(15, 14, 13, 8, 11, 9), skills={"Stealth": 6, "Survival": 2}, exp=200)
    c_monsters["Bugbear Chief"] = Enemy("Bugbear Chief", AC=17, HP=65, speed=(30, 0, 0, 0, 0), abs=(17, 14, 14, 11, 12, 11), skills={"Intimidation": 2, "Stealth": 6, "Survival": 3}, exp=700)

    c_monsters["Bulette"] = Enemy("Bulette", AC=17, HP=94, speed=(40, 0, 0, 40, 0), abs=(19, 11, 21, 2, 10, 5), skills={"Perception": 6}, exp=1800)
    c_monsters["Bullywug"] = Enemy("Bullywug", AC=15, HP=11, speed=(20, 0, 40, 0, 0), abs=(12, 12, 13, 7, 10, 7), skills={"Stealth": 3}, exp=50)

    # ================================================ C ===================================================================
    c_monsters["Cambion"] = Enemy("Cambion", AC=19, HP=82, speed=(30, 60, 0, 0, 0), abs=(18, 18, 16, 14, 12, 16), saving_throws={"Strength": 7, "Constitution": 6, "Intellect": 5, "Charisma": 6}, skills={"Deception": 6, "Intimidation": 6, "Perception": 4, "Stealth": 7}, dmg_resist=["cold", "fire", "lightning", "poison", "bludgeoning", "piercing", " slashing (nonmagical weapons)"], exp=1800)
    c_monsters["Carrion Crawler"] = Enemy("Carrion Crawler", AC=13, HP=51, speed=(30, 0, 0, 0, 30), abs=(14, 13, 16, 1, 12, 5), skills={"Perception": 3}, exp=450)
    c_monsters["Centaur"] = Enemy("Centaur", AC=12, HP=45, speed=(50, 0, 0, 0, 0), abs=(18, 14, 14, 9, 13, 11), skills={"Athletics": 6, "Perception": 3, "Survival": 3}, exp=450)
    c_monsters["Chimera"] = Enemy("Chimera", AC=14, HP=114, speed=(30, 60, 0, 0, 0), abs=(19, 11, 19, 3, 14, 10), skills={"Perception": 8}, exp=2300)
    c_monsters["Chuul"] = Enemy("Chuul", AC=16, HP=93, speed=(30, 0, 30, 0, 0), abs=(19, 10, 16, 5, 11, 5), skills={"Perception": 4}, dmg_immune=["poison"], cond_immune=["Poisoned"], exp=1100)
    c_monsters["Cloaker"] = Enemy("Cloaker", AC=14, HP=78, speed=(10, 40, 0, 0, 0), abs=(17, 15, 12, 13, 12, 14), skills={"Stealth": 5}, exp=3900)
    c_monsters["Cockatrice"] = Enemy("Cockatrice", AC=11, HP=27, speed=(20, 40, 0, 0, 0), abs=(6, 12, 12, 2, 13, 5), exp=100)
    c_monsters["Couatl"] = Enemy("Couatl", AC=19, HP=97, speed=(30, 90, 0, 0, 0), abs=(16, 20, 17, 18, 20, 18), saving_throws={"Constitution": 5, "Wisdom": 7, "Charisma": 6}, dmg_resist=["radiant"], dmg_immune=["psychic", "bludgeoning", "piercing", "slashing (nonmagical weapons)"], exp=1100)
    c_monsters["Crawling Claw"] = Enemy("Crawling Claw", AC=12, HP=2, speed=(20, 0, 0, 0, 20), abs=(13, 14, 11, 5, 10, 4), dmg_immune=["poison"], cond_immune=["Charmed", "Exhausted", "Poisoned"], exp=10)
    c_monsters["Cyclops"] = Enemy("Cyclops", AC=14, HP=138, speed=(30, 0, 0, 0, 0), abs=(22, 11, 20, 8, 6, 10), exp=2300)

    # ================================================ D ===================================================================
    c_monsters["Darkmantle"] = Enemy("Darkmantle", AC=11, HP=22, speed=(10, 30, 0, 0, 0), abs=(16, 12, 13, 2, 10, 5), skills={"Stealth": 3}, exp=100)
    c_monsters["Death Knight"] = Enemy("Death Knight", AC=20, HP=180, speed=(30, 0, 0, 0, 0), abs=(20, 11, 20, 12, 16, 18), saving_throws={"Dexterity": 6, "Wisdom": 9, "Charisma": 10}, dmg_immune=["necrotic", "poison"], cond_immune=["Exhausted", "Frightened", "Poisoned"], exp=18000)
    c_monsters["Demilich"] = Enemy("Demilich", AC=20, HP=80, speed=(0, 30, 0, 0, 0), abs=(1, 20, 10, 20, 17, 20), saving_throws={"Constitution": 6, "Intellect": 11, "Wisdom": 9, "Charisma": 11}, dmg_resist=["bludgeoning", "piercing", " slashing (nonmagical weapons)"], cond_immune=["Charmed", "Deafened", "Exhausted", "Frightened", "Paralyzed", "Petrified", "Poisoned", "Prone", "Stunned"], exp=20000)

    # # Demons
    c_monsters["Balor"] = Enemy("Balor", AC=19, HP=262, speed=(40, 80, 0, 0, 0), abs=(26, 15, 22, 20, 16, 22), saving_throws={"Strength": 14, "Constitution": 12, "Wisdom": 9, "Charisma": 12}, dmg_resist=["cold", "lightning", "bludgeoning", "piercing", "slashing (nonmagical weapons)"], dmg_immune=["fire", "poison"], cond_immune=["Poisoned"], exp=22000)
    c_monsters["Barlgura"] = Enemy("Barlgura", AC=15, HP=68, speed=(30, 0, 0, 0, 30), abs=(18, 15, 16, 7, 14, 9), saving_throws={"Dexterity": 5, "Constitution": 6}, skills={"Perception": 5, "Stealth": 5}, dmg_resist=["cold", "fire", "lightning"], dmg_immune=["poison"], cond_immune=["Poisoned"], exp=1800)
    c_monsters["Chasme"] = Enemy("Chasme", AC=15, HP=84, speed=(20, 60, 0, 0, 0), abs=(15, 15, 12, 11, 14, 10), saving_throws={"Dexterity": 5, "Wisdom": 5}, skills={"Perception": 5}, dmg_resist=["cold", "fire", "lightning"], dmg_immune=["poison"], cond_immune=["Poisoned"], exp=2300)
    c_monsters["Dretch"] = Enemy("Dretch", AC=11, HP=18, speed=(20, 0, 0, 0, 0), abs=(11, 11, 12, 5, 8, 3), dmg_resist=["cold", "fire", "lightning"], dmg_immune=["poison"], cond_immune=["Poisoned"], exp=50)

    pickle.dump(c_monsters, open("monsters.camp", "wb"))