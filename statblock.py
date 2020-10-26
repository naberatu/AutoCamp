
class StatBlock:

    def __init__(self):
        # dictionary of all stats
        self.stats = {
            # Misc Stats
            "initiative": 0,
            "inspiration": 0,
            "profBonus": 0,
            "weight": 0,
            "tileSize": 0,

            # Character Stats
            "armorClass": 0,
            "speed": 0,
            "currentHP": 0,
            "maxHP": 0,
            "hitDice": 0,

            # Ability Scores
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "wisdom": 0,
            "intellect": 0,
            "charisma": 0,

            # Skills
            "acrobatics": 0,
            "animalHandling": 0,
            "arcana": 0,
            "athletics": 0,
            "deception": 0,
            "history": 0,
            "insight": 0,
            "intimidation": 0,
            "investigation": 0,
            "medicine": 0,
            "nature": 0,
            "perception": 0,
            "performance": 0,
            "persuasion": 0,
            "religion": 0,
            "sleightOfHand": 0,
            "stealth": 0,
            "survival": 0
        }

    def modify_stat(self, stat, num):
        if stat in self.stats.keys():
            try:
                self.stats[stat] = num
            except:
                print("[ER] Cannot modify ", stat, "...")
        else:
            print("[ER] ", stat, " does not exist!")

    def get_stat(self, stat):
        return self.stats[stat]
