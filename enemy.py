
from animate import Animate
from statblock import StatBlock


class Enemy(Animate):
    def __init__(self, name, race=None, role=None, level=1, stat_block=StatBlock(), AC=0, HP=0, speed=(0,0,0),
                 abs=(0,0,0,0,0,0), saving_throws=dict(), skills=dict(), dmg_resist=[], dmg_immune=[], dmg_vuln=[], cond_immune=[], exp=0):
        super().__init__(name, race, role, level, stat_block)      # should inherit everything this way
        self.exp = exp
        #self.companion = None
        self.is_enemy = True
        self.maxInvSize = 10            # Arbitrary value
        self.weapon = None
        self.stat_block = stat_block

        self.stat_block.modify_stat("Armor Class", AC)
        # Speed tuple values -> (Regular Speed, Flying Speed, Swimming Speed, Burrow Speed, Climbing Speed)
        self.stat_block.modify_stat("Speed", speed)

        self.stat_block.modify_stat("Max HP", HP)
        self.stat_block.modify_stat("Current HP", HP)

        # abs tuple values -> (STR, DEX, CON, INT, WIS, CHA)
        self.stat_block.modify_stat("Strength", abs[0])
        self.stat_block.modify_stat("Dexterity", abs[1])
        self.stat_block.modify_stat("Constitution", abs[2])
        self.stat_block.modify_stat("Intellect", abs[3])
        self.stat_block.modify_stat("Wisdom", abs[4])
        self.stat_block.modify_stat("Charisma", abs[5])

        self.saving_throws = saving_throws

        for k, v in skills.items():
            self.stat_block.modify_stat(k, self.stat_block.stats[k] + v)

        self.dmg_resistances = dmg_resist
        self.dmg_immunities = dmg_immune
        self.dmg_vulnerabilities = dmg_vuln
        self.cond_immunities = cond_immune

    # Accessors
    # ==================================
    def get_exp_yield(self):
        return self.exp

    def inv_print(self):
        print("[ER] Enemies have no inventory!")
        return False

    # Mutators
    # ==================================
    def mod_exp_yield(self, amount):
        self.exp = amount

