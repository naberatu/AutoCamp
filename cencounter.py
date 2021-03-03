from encounter import Encounter
from enemy import Enemy
from player import Player
from inanimate import Inanimate
from map import Map
# from random import randint
# from math import floor


class CEncounter(Encounter):
    def __init__(self, name, is_shop=False, is_combat=True, anim=None, inanim=None, bkgd="./assets/rivermouth.jpg",
                 max_inventory="slot", max_x=15, max_y=15):
        super().__init__(name, is_shop, is_combat, anim)
        self.is_combat = is_combat
        if inanim:
            self.inanimateList = inanim
        else:
            self.inanimateList = list()
        self.background = bkgd
        self.map = Map(max_x, max_y, self.animateList, self.inanimateList)
        self.gamerule_inv_max = max_inventory   # Gamerule that determines if there will be max inventory size.
        self.turnCounter = 0
        self.live = False
        self.map_max_x = max_x
        self.map_max_y = max_y
        self.death_saves = 0

    def no_enemies(self):
        for ent in self.animateList:
            if type(ent) == Enemy:
                return False
        return True

    def get_bkgd(self):
        return self.background

    def get_inanim(self):
        return self.inanimateList

    def get_tiles(self):
        return self.map.get_tile_list()

    def get_background(self):
        return self.background

    def get_entity(self, is_animate, index):
        if is_animate:
            return self.animateList[index]
        else:
            return self.inanimateList[index]

    def get_actor(self):
        return self.currentEntity

    def get_al_size(self):
        return len(self.animateList)

    def add_entity(self, ent):
        if isinstance(ent, Inanimate):
            self.inanimateList.append(ent)
        else:
            self.animateList.append(ent)
            if self.live:
                self.turnCounter = self.turnCounter % (len(self.animateList) - 1)
                self.determineInitiative()

    def start_encounter(self):
        self.determineInitiative()
        self.currentEntity = self.animateList[0]
        self.live = True
        self.map = Map(self.map_max_x, self.map_max_y, self.animateList, self.inanimateList)

    def enemyInRange(self):
        location = self.currentEntity.get_coors()
        x, y, z = location[0], location[1], location[2]
        nearbyCoors = []
        inRange = []

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

        if not self.currentEntity.get_iff():  # if attacker is a player
            for ent in self.animateList:
                if ent.get_iff():
                    otherCoors = ent.get_coors()
                    if otherCoors in nearbyCoors:
                        inRange.append(ent)

        else:  # if attacker is an enemy
            for ent in self.animateList:
                if not ent.get_iff():
                    otherCoors = ent.get_coors()
                    if otherCoors in nearbyCoors:
                        inRange.append(ent)

        return inRange

    # ===============================================================================
    # Map, Movement, and Hint Methods
    # ===============================================================================
    def enc_move(self, actor, speed_remaining, new_x_coord, new_y_coord, new_z_coord=1):
        source = (actor.get_coors()[0], actor.get_coors()[1])
        destination = (new_x_coord, new_y_coord)

        if new_x_coord > self.map_max_x or new_y_coord > self.map_max_y:
            return [0, "[ER] Out of bounds!"]

        obstacles = self.animateList + self.inanimateList
        for ent in obstacles:
            if ent.get_coors() == [new_x_coord, new_y_coord, new_z_coord] and ent != actor:
                return False   # In the case of failure

        paths = self.map.dijkstras(source)
        distance = paths[0][destination]

        if distance <= speed_remaining:
            actor.set_coors(x=new_x_coord, y=new_y_coord, z=new_z_coord)
            return True

        return False

    def get_hint(self):
        response = ""
        actor = self.currentEntity
        enemies_in_attack_range = list()
        enemies_in_range = list()
        if type(actor) == Enemy:
            response = "No hints for DM controlled entities."
            return response
        elif type(actor) == Player:
            for i in range(0, len(self.animateList)):
                if (type(self.animateList[i]) == Enemy) and self.distance_between(actor, self.animateList[i]) <= 5:
                    enemies_in_attack_range.append(self.animateList[i])
                if (type(self.animateList[i]) == Enemy) and self.distance_between(actor,
                                                                                  self.animateList[
                                                                                      i]) <= actor.get_stat(
                    "Speed"):
                    enemies_in_range.append(self.animateList[i])
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
        for ent in self.animateList:
            if ent.is_stealthy:
                stealth = self.performCheck("Stealth", ent)
                for ent2 in self.animateList:
                    if type(ent) != type(ent2) and stealth > self.passiveCheck("Perception", ent2, False, False, False):
                        ent2.is_surprised = True

    def resetSurprise(self):
        for ent in self.animateList:
            if ent.is_surprised:
                ent.set_surprise(False)

    # ===============================================================================
    # Combat Methods
    # ===============================================================================

    def determineInitiative(self):
        order = []
        index = 0
        for ent in self.animateList:
            order.append((index, self.performCheck("Dexterity", None, ent, print_results=False)))
            index += 1
        order = sorted(order, key=lambda x: - x[1])

        self.animateList[:] = [self.animateList[i[0]] for i in order]

    def next_turn(self):
        self.turnCounter += 1
        self.currentEntity = self.animateList[self.turnCounter % len(self.animateList)]

    def dealDMG(self, damage, target):
        targetHealth = target.get_stat("Current HP")
        targetHealth -= damage

        print(self.currentEntity.get_name(), "attacked", target.get_name(), "!!")
        print(target.get_name(), "took", damage, "damage!!")

        if type(target) == Enemy and targetHealth <= 0:  # HP is -/0, enemy -> INSTANT DEATH
            target.set_stats("Current HP", 0)
            print(target.get_name(), "has died!!")
            self.mapList[target.get_coors()[1] - 1][(target.get_coors()[0] + ((1 * target.get_coors()[0]) - 1))] = ' '
            self.animateList.remove(target)

        elif targetHealth >= 0:  # HP is +/0, player -> DMG
            target.set_stats("Current HP", targetHealth)
            print(target.get_name(), "is now at", target.get_stat("Current HP"), "/",
                  target.get_stat("Max HP"), "HP.")

        elif (targetHealth * -1) >= target.get_stat("Max HP"):  # HP is -, exceeds max HP-> INSTANT DEATH
            target.set_stats("Current HP", 0)
            print(target.get_name(), "has died!!")
            self.mapList[target.get_coors()[1] - 1][(target.get_coors()[0] + ((1 * target.get_coors()[0]) - 1))] = ' '
            self.animateList.remove(target)
            self.enc_update_map()

        elif (targetHealth * -1) <= target.get_stat("Max HP"):  # HP is negative, doesn't exceed max HP -> UNCONSCIOUS
            target.set_stats("Current HP", 0)
            if type(target) == Player:
                target.set_stability(False)
            if "unconscious" in target.get_conditions():  # if already unconscious when hit
                target.set_death_strikes(target.get_death_strikes() + 1)
            print(target.get_name(), "is unconscious!!")
            target.mod_conditions(True, "Unconscious")

    def attack(self, target, adv, disadv) -> None:
        toHit = target.get_stat("Armor Class")
        attempt = 0

        # if "melee" in self.currentEntity.get_weapon().get_use():
        attempt = self.performCheck("Strength", None, self.currentEntity, adv, disadv)
        # elif "ranged" in self.currentEntity.get_weapon().get_use():
        #     attempt = self.performCheck("Dexterity", self.currentEntity, adv, disadv)

        if attempt >= toHit:
            damage = self.rollDice(1, 20, False)
            self.dealDMG(damage, target)
        else:
            print("Attack failed!")
