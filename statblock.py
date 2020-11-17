
class StatBlock:
    def __init__(self):
        # dictionary of all stats
        self.stats = {
            # Character Stats
            "Armor Class": 0,
            "Speed": 0,
            "Current HP": 0,
            "Max HP": 0,
            "Hit Dice": 0,

            # Misc Stats
            "Inspiration": 0,
            "Proficiency Bonus": 0,

            # Ability Scores
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Wisdom": 0,
            "Intellect": 0,
            "Charisma": 0,

            # Skills
            "Acrobatics": 0,
            "Animal Handling": 0,
            "Arcana": 0,
            "Athletics": 0,
            "Deception": 0,
            "History": 0,
            "Insight": 0,
            "Intimidation": 0,
            "Investigation": 0,
            "Medicine": 0,
            "Nature": 0,
            "Perception": 0,
            "Performance": 0,
            "Persuasion": 0,
            "Religion": 0,
            "Sleight Of Hand": 0,
            "Stealth": 0,
            "Survival": 0
        }

    def modify_stat(self, stat, num):
        if stat in self.stats.keys():
            try:
                self.stats[stat] = num
                if stat == "Max HP":
                    self.stats["Current HP"] = num
            except:
                print("[ER] Cannot modify ", stat, "...")
        else:
            print("[ER] ", stat, " does not exist!")

    def get_stat(self, stat):
        if self.stats.keys().__contains__(stat):
            return self.stats[stat]
        else:
            print("[ER] That stat is unavailable!")

    def get_dict(self):
        return self.stats
