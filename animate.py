
from entity import Entity
from statblock import StatBlock
import random
import conditions


class Animate(Entity):
    def __init__(self, name, icon="./assets/item_drop.png", race=None, role=None, level=1, stat_block=StatBlock()):
        super().__init__(name, icon)       # should inherit everything this way
        self.conditions = dict()

        self.stat_block = stat_block
        self.race = race
        self.role = role
        self.level = level
        self.companion = None
        self.exp = 0
        self.type_tag = None
        self.inventory = dict()                 # Key is Item, Value is quantity.
        self.inv_max = 20                       # maximum inventory capacity possible
        self.inv_scheme = "slot"                # whether the inventory stores by slot, item weight, or infinite
        self.is_enemy = False
        self.is_stealthy = False
        self.is_surprised = False

    def showStats(self) -> None:
        stat = self.stat_block.get_dict()

        print("\n==============================================================================")
        text = "{:20}".format(self.get_name())
        text += "{:^30}".format(self.get_race() + " " + self.get_role())

        if self.type_tag == "player" or self.type_tag == "enemy":
            text += "\t[Lv. {:<2}]".format(self.get_level())

        print(text, "\n------------------------------------------------------------------------------")
        text = "HP: " + "{:12}".format(("{:3} /{}".rjust(12).format(stat["Current HP"], stat["Max HP"])))
        text += "\t" + "{:^30}".format("[AC: {:<2}]".format(stat["Armor Class"]))
        text += "\tSpeed: {:<2}".format(stat["Speed"])
        print(text, "\n==============================================================================")

        if self.type_tag == "player" and self.companion:
            print("Companion:", self.companion)
        elif self.type_tag == "enemy":
            print("EXP Yield:", self.exp)

        text = "{:19}".format("Inspiration:") + " {:<2}".format(stat["Inspiration"])
        text += "\t\t{:19}".format("Proficiency Bonus:") + "{:<+2}".format(stat["Proficiency Bonus"])
        text += "\t\tHit Dice: d" + str(stat["Hit Dice"]) + " (" + str(stat["Hit Dice Quantity"]) + "/" + str(self.level) + ")" + "\n"
        print(text)

        tracer, text = 0, ""
        for name, value in list(stat.items())[8:31]:
            if tracer < 6:
                if tracer % 2 == 0:
                    text = "{:19}".format(name + ": ") + "{:2}".format(value)
                else:
                    text += "\t\t{:19}".format(name + ": ") + "{:2}".format(value)
                    print(text)
            elif tracer >= 6:
                if tracer == 6:
                    print()
                if tracer % 3 == 0:
                    text = "{:19}".format(name + ": ") + "{:+2}".format(value)
                else:
                    text += "\t\t{:19}".format(name + ": ") + "{:+2}".format(value)
                    if (tracer + 1) % 3 == 0:
                        print(text)
            tracer += 1

        print("==============================================================================")

    # ==================================
    # Accessors
    # ==================================
    def get_stat_block(self):
        return self.stat_block

    def get_level(self):
        return self.level

    def get_role(self):
        return self.role

    def get_race(self):
        return self.race

    def get_stat(self, stat):
        return self.stat_block.get_stat(stat)

    def get_conditions(self):
        return self.conditions

    def get_iff(self):
        return self.is_enemy

    # ==================================
    # Mutators
    # ==================================
    def level_up(self):
        if self.level < 20:
            self.level += 1
            new_hp = random.randint(1, self.stat_block.get_stat("Hit Dice"))
            old_hp = self.stat_block.get_stat("Max HP")
            self.stat_block.modify_stat("Max HP", old_hp + new_hp)
            self.stat_block.modify_stat("Current HP", old_hp + new_hp)
            self.stat_block.modify_stat("Hit Dice Quantity", self.stat_block.get_stat("Hit Dice Quantity") + 1)
            # Commented out for debug
            # print("[OK] Level Updated to ", self.level, "!")
        else:
            print("[ER] Already at max level!")

    def mod_level(self, value):
        if (value > 0) and (value < 21):
            self.level = value
            print("[OK] Level Updated to ", value, "!")
        else:
            print("[ER] Invalid Level!")

    def mod_role(self, role):
        self.role = role

    def mod_race(self, race):
        self.race = race

    def set_stats(self, stat, num):
        self.stat_block.modify_stat(stat, num)

    def mod_conditions(self, condition, duration=1, adding=True):
        try:
            if adding:
                self.conditions[condition] = duration
            else:
                del self.conditions[condition]
        except KeyError:
            print("[ER]", condition, "is not a valid condition!!")

    def condition_tick(self):
        del_list = list()
        for cond in self.conditions.keys():
            self.conditions[cond] -= 1
            if self.conditions[cond] <= 0:
                del_list.append(cond)

        for cond in del_list:
            del self.conditions[cond]

    def set_surprise(self, surprise_status):
        self.is_surprised = surprise_status

    def set_stealth(self, stealth_status):
        self.is_stealthy = stealth_status

    def set_iff(self, iff):
        self.is_enemy = iff




