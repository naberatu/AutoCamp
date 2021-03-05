from encounter import Encounter
from enemy import Enemy
from player import Player
from inanimate import Inanimate
from map import Map
from math import floor
from items import c_items

class CEncounter(Encounter):
    def __init__(self, name, is_shop=False, is_combat=True, anim=None, inanim=None, bkgd="./assets/rivermouth.jpg",
                 max_inventory="slot", max_x=15, max_y=15):
        super().__init__(name, is_shop, is_combat, anim)

        if anim is None:
            anim = list()
        if inanim is None:
            inanim = list()

        self.inanimate_list = inanim
        self.animate_list = anim
        self.is_combat = is_combat

        self.background = bkgd
        self.map = Map(max_x, max_y, self.animate_list, self.inanimate_list)
        self.gamerule_inv_max = max_inventory   # Gamerule that determines if there will be max inventory size.
        self.turnCounter = 0
        # self.current_turn = 0
        self.live = False
        self.map_max_x = max_x
        self.map_max_y = max_y
        self.death_saves = 0

    def no_enemies(self):
        for ent in self.animate_list:
            if type(ent) == Enemy:
                return False
        return True

    def get_bkgd(self):
        return self.background

    def get_inanim(self):
        return self.inanimate_list

    def get_tiles(self):
        return self.map.get_tile_list()

    def get_background(self):
        return self.background

    def get_turn(self):
        return self.turnCounter

    def get_entity(self, is_animate, index):
        if is_animate:
            return self.animate_list[index]
        else:
            return self.inanimate_list[index]

    def get_actor(self):
        return self.currentEntity

    def get_al_size(self):
        return len(self.animate_list)

    def add_entity(self, ent):
        if isinstance(ent, Inanimate):
            self.inanimate_list.append(ent)
        else:
            self.animate_list.append(ent)
            if self.live:
                self.turnCounter = self.turnCounter % (len(self.animate_list) - 1)
                self.determineInitiative()

    def start_encounter(self, reset_init=True):
        if reset_init:
            self.determineInitiative()
        self.live = True
        self.map = Map(self.map_max_x, self.map_max_y, self.animate_list, self.inanimate_list)

    def enemyInRange(self):
        object_list = self.animate_list + self.inanimate_list
        location = object_list[self.turnCounter].get_coors()
        x, y, z = location[0], location[1], location[2]
        nearbyCoors = []
        enemy_attacker = False
        player_attacker = False
        # inRange = []

        if y > 1:  # N
            nearbyCoors.append([x, y - 1, z])
        if y > 1 and x < self.map_max_x:  # NE
            nearbyCoors.append([x + 1, y - 1, z])
        if x < self.map_max_x:  # E
            nearbyCoors.append([x + 1, y, z])
        if y < self.map_max_y and x < self.map_max_x:  # SE
            nearbyCoors.append([x + 1, y + 1, z])
        if y < self.map_max_y:  # S
            nearbyCoors.append([x, y + 1, z])
        if y < self.map_max_y and x > 1:  # SW
            nearbyCoors.append([x - 1, y + 1, z])
        if x > 1:  # W
            nearbyCoors.append([x - 1, y, z])
        if x > 1 and y > 1:  # NW
            nearbyCoors.append([x - 1, y - 1, z])

        if type(self.get_entity(self.turnCounter)) is Enemy:
            enemy_attacker = True
        elif type(self.get_entity(self.turnCounter)) is Player:
            player_attacker = True

        for coors in nearbyCoors:
            index = self.entity_at(coors[0], coors[1])
            if index is not None and player_attacker and type(self.get_entity(index)) is Enemy:
                return [True, index]
            if index is not None and enemy_attacker and type(self.get_entity(index)) is Player:
                return [True, index]
        return [False, -1]

    # ===============================================================================
    # Map, Movement, and Hint Methods
    # ===============================================================================
    def entity_at(self, x_coor, y_coor):
        entity_list = self.animate_list + self.inanimate_list
        for index, ent in enumerate(entity_list):
            coors = (ent.get_coors()[0], ent.get_coors()[1])
            if coors == (x_coor, y_coor):
                return index
        return None

    def get_entity(self, index):
        entity_list = self.animate_list + self.inanimate_list
        try:
            if 0 <= index < len(entity_list):
                return entity_list[index]
        except: pass
        return None

    def enc_move(self, x_src, y_src, z_src, speed, x_dest, y_dest, z_dest=0):
        source = (x_src, y_src)
        destination = (x_dest, y_dest)

        if x_dest > self.map_max_x or y_dest > self.map_max_y:
            return [False, 0]

        actor = None
        for ent in self.animate_list:
            if ent.get_coors() == [x_src, y_src, z_src]:
                actor = ent
                break

        obstacles = self.animate_list + self.inanimate_list
        obstacles.remove(actor)

        for ent in obstacles:
            if ent.get_coors() == [x_dest, y_dest, z_dest]:
                return [False, 0]   # In the case of failure

        paths = self.map.dijkstras(source)
        distance = paths[0][destination]

        if distance <= speed:
            actor.set_coors(x=x_dest, y=y_dest, z=z_dest)
            return [True, distance]

        return [False, 0]

    def get_hint(self):
        response = ""
        actor = self.currentEntity
        enemies_in_attack_range = list()
        enemies_in_range = list()
        if type(actor) == Enemy:
            response = "No hints for DM controlled entities."
            return response
        elif type(actor) == Player:
            for i in range(0, len(self.animate_list)):
                if (type(self.animate_list[i]) == Enemy) and self.distance_between(actor, self.animate_list[i]) <= 5:
                    enemies_in_attack_range.append(self.animate_list[i])
                if (type(self.animate_list[i]) == Enemy) and self.distance_between(actor,
                                                                                   self.animate_list[
                                                                                      i]) <= actor.get_stat(
                    "Speed"):
                    enemies_in_range.append(self.animate_list[i])
            if len(enemies_in_attack_range) != 0:
                min_health_remaining = float('inf')
                min_health_remaining_index = -1
                for i in range(0, len(enemies_in_attack_range)):
                    if enemies_in_attack_range[i].get_stat("Current HP") < min_health_remaining:
                        min_health_remaining = enemies_in_attack_range[i].get_stat("Current HP")
                        min_health_remaining_index = i
                response = "Attack " + str(
                    enemies_in_attack_range[min_health_remaining_index].get_name()) + " at (" + str(
                    enemies_in_attack_range[min_health_remaining_index].get_coors()[0]) + ", " + str(
                    enemies_in_attack_range[min_health_remaining_index].get_coors()[1]) + ")"
                return response

    def distance_between(self, actor_one, actor_two):
        if (abs(actor_one.get_coors()[0] - actor_two.get_coors()[0]) == 1 and abs(
                actor_one.get_coors()[1] - actor_two.get_coors()[1]) == 1):
            return 5
        return ((abs(actor_one.get_coors()[0] - actor_two.get_coors()[0]) * 5) + (
                abs(actor_one.get_coors()[1] - actor_two.get_coors()[1]) * 5))

    # ===============================================================================
    # Inventory Methods
    # ===============================================================================
    def inv_pickup(self, item, amount=1, hot_swap=False):
        try:
            if self.currentEntity.inv_add(item, amount):
                if hot_swap and self.currentEntity.inv_equip(item):
                    print("[OK] Picked up and equipped " + item + "!")
                else:
                    print("[OK] Picked up " + item + "!")
                return True
            raise ValueError
        except:
            print("[ER] Could not pick up " + item + "!")
            return False

    # ===============================================================================
    # Dice & Check Methods
    # ===============================================================================
    def passiveCheck(self, stat, ent, advantage=False, disadvantage=False, print_results=True):
        mod = self.modifier(stat, ent)
        roll = 10 + mod
        if advantage:
            roll += 5
        if disadvantage:
            roll -= 5
        if print_results:
            print("Passive Check result w/", stat, "modifier of", mod, ":", roll)
        return roll

    def determineSurprise(self):
        for ent in self.animate_list:
            if ent.is_stealthy:
                stealth = self.performCheck("Stealth", None, ent)
                for ent2 in self.animate_list:
                    if type(ent) != type(ent2) and stealth > self.passiveCheck("Perception", ent2, False, False, False):
                        ent2.is_surprised = True

    def resetSurprise(self):
        for ent in self.animate_list:
            if ent.is_surprised:
                ent.set_surprise(False)

    # ===============================================================================
    # Combat Methods
    # ===============================================================================

    def determineInitiative(self):
        order = []
        index = 0
        for ent in self.animate_list:
            order.append((index, self.performCheck("Dexterity", None, ent, print_results=False)))
            index += 1
        order = sorted(order, key=lambda x: - x[1])

        self.animate_list[:] = [self.animate_list[i[0]] for i in order]

    def next_turn(self):
        self.turnCounter = (self.turnCounter + 1) % len(self.animate_list + self.inanimate_list)

    def dealDMG(self, damage, target):
        object_list = self.animate_list + self.inanimate_list
        currentEntity = object_list[self.turnCounter]

        targetHealth = target.get_stat("Current HP")
        targetHealth -= damage

        print(currentEntity.get_name(), "attacked", target.get_name(), "!!")
        print(target.get_name(), "took", damage, "damage!!")

        if type(target) == Enemy and targetHealth <= 0:  # HP is -/0, enemy -> INSTANT DEATH
            target.set_stats("Current HP", 0)
            print(target.get_name(), "has died!!")
            self.animate_list.remove(target)

        elif targetHealth >= 0:  # HP is +/0, player -> DMG
            target.set_stats("Current HP", targetHealth)
            print(target.get_name(), "is now at", target.get_stat("Current HP"), "/",
                  target.get_stat("Max HP"), "HP.")

        elif (targetHealth * -1) >= target.get_stat("Max HP"):  # HP is -, exceeds max HP-> INSTANT DEATH
            target.set_stats("Current HP", 0)
            print(target.get_name(), "has died!!")
            self.animate_list.remove(target)

        elif (targetHealth * -1) <= target.get_stat("Max HP"):  # HP is negative, doesn't exceed max HP -> UNCONSCIOUS
            target.set_stats("Current HP", 0)
            if type(target) == Player:
                target.set_stability(False)
            if "unconscious" in target.get_conditions():  # if already unconscious when hit
                target.set_death_strikes(target.get_death_strikes() + 1)
            print(target.get_name(), "is unconscious!!")
            target.mod_conditions(True, "Unconscious")

    def parse_finesse(self, weapon):
        desc = weapon.details
        stripped_desc = ""
        for c in desc:
            if c.isalnum() or c.isspace():
                stripped_desc+= c
        if "Finesse" in stripped_desc:
            return True
        return False

    def attack(self, target, adv, disadv) -> None:
        object_list = self.animate_list + self.inanimate_list
        currentEntity = object_list[self.turnCounter]

        toHit = target.get_stat("Armor Class")
        attempt = 0
        weapon = None
        atk_mod = None
        dmg_type = None
        str_attempt = self.performCheck("Strength", None, currentEntity, adv, disadv)
        dex_attempt = self.performCheck("Dexterity", None, currentEntity, adv, disadv)
        # This will print two rolls to the console, but only the appropriate one will be used based on weapon

        if type(currentEntity) is Player and currentEntity.get_weapon() is not None:
            weapon = c_items[currentEntity.get_weapon()]  # Weapon is object
            dmg_type = weapon.properties["dmg_type"]

        if weapon is None or weapon.properties["range_melee"] == 0:  # Melee attack
            attempt = str_attempt
            atk_mod = "Strength"

        elif weapon.properties["range_melee"] == 1:  # Ranged Attack
            attempt = dex_attempt
            atk_mod = "Dexterity"

        if weapon is not None and self.parse_finesse(weapon):  # FINESSE, picks better of STR & DEX
            str_mod = self.modifier("Strength", currentEntity)
            dex_mod = self.modifier("Dexterity", currentEntity)
            if str_mod > dex_mod:
                attempt = str_attempt
                atk_mod = "Strength"
                print("Strength chosen!")
            else:
                attempt = dex_attempt
                atk_mod = "Dexterity"
                print("Dexterity chosen!")

        if type(currentEntity) is Player and weapon.get_name() in currentEntity.weapon_prof:  # checks for proficiency
            attempt += currentEntity.get_stat("Proficiency Bonus")
            print("You are proficient with this weapon! +{} to attempt against AC!".format(
                currentEntity.get_stat("Proficiency Bonus")))

        if attempt >= toHit:
            if weapon is None:  # Unarmed
                damage = self.rollDice(1, 20, print_results=False) + self.modifier("Strength", currentEntity)
            else:
                damage = self.rollDice(weapon.properties["dmg_dice"], weapon.properties["dmg_sides"],
                                       print_results=False) + self.modifier(atk_mod, currentEntity)

            damage = max(0, damage)

            if type(target) is Enemy:
                if dmg_type in target.dmg_immunities:
                    damage = 0
                    # print("{} is immune to {}!".format(target.get_name(), dmg_type))
                elif dmg_type in target.dmg_resistances:
                    # print("Damage before: ", damage)
                    damage = floor(damage / 2)
                    # print("Damage after: ", damage)
                    # print("{} is resistant to {}!".format(target.get_name(), dmg_type))
                elif dmg_type in target.dmg_vulnerabilities:
                    damage = damage * 2
                    # print("{} is vulnerable to {}!".format(target.get_name(), dmg_type))

            self.dealDMG(damage, target)
        else:
            print("Attack failed!")
