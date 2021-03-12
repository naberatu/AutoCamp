
from math import floor

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
            "Hit Dice Quantity": 0,     # For current remaining HD. Total is still level.

            # Misc Stats
            "Inspiration": 0,
            "Proficiency Bonus": 2,

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
        if stat == "Current HP" and num > self.stats["Max HP"]:
            self.stats[stat] = self.stats["Max HP"]
        elif stat in self.stats.keys():
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
            if stat == "Speed" and type(self.stats["Speed"]) is tuple:
                return max(self.stats["Speed"])
            return self.stats[stat]
        else:
            print("[ER] That stat is unavailable!")

    def get_mod(self, stat):
        if stat in list(self.stats.keys())[8:14]:
            return int(floor((self.stats[stat] - 10) / 2))
        else:
            return None

    def get_dict(self):
        return self.stats

    def autofill_scores(self, stre, dext, cons, wisd, intl, cha):
        self.modify_stat("Strength", stre)
        self.modify_stat("Dexterity", dext)
        self.modify_stat("Constitution", cons)
        self.modify_stat("Wisdom", wisd)
        self.modify_stat("Intellect", intl)
        self.modify_stat("Charisma", cha)

        self.modify_stat("Charisma", cha)

        str_list = [17]
        dex_list = [14, 29, 30]
        int_list = [16, 19, 22, 24, 28]
        wis_list = [15, 20, 23, 25, 31]
        cha_list = [18, 21, 26, 27]

        names = list(self.stats)
        names = names[14:32]

        for num, name in enumerate(names, 14):
            if num in str_list:
                self.modify_stat(name, self.get_mod("Strength"))
            elif num in dex_list:
                self.modify_stat(name, self.get_mod("Dexterity"))
            elif num in int_list:
                self.modify_stat(name, self.get_mod("Intellect"))
            elif num in wis_list:
                self.modify_stat(name, self.get_mod("Wisdom"))
            elif num in cha_list:
                self.modify_stat(name, self.get_mod("Charisma"))


