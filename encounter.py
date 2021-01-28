
from enemy import Enemy
from player import Player
from inanimate import Inanimate
from random import randint
from math import floor


class Encounter:
    def __init__(self, max_inventory="slot"):
        self.currentEntity = None
        self.animateList = list()
        self.inanimateList = list()
        self.mapList = list()
        self.gamerule_inv_max = max_inventory   # Gamerule that determines if there will be max inventory size.
        self.turnCounter = 0
        self.live = False
        self.map_max_x = 0
        self.map_max_y = 0
        self.death_saves = 0

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
        x_coord = actor.get_coors()[0]
        y_coord = actor.get_coors()[1]
        testing = [new_x_coord, new_y_coord, new_z_coord]

        if new_x_coord > self.map_max_x or new_y_coord > self.map_max_y:
            return [0, "[ER] Out of bounds!"]

        for ent in self.animateList:
            if ent.get_coors() == testing and ent != actor:
                return [0, "[ER] That space is occupied!"]

        requested_distance = 0
        # vertical
        if actor.get_coors()[0] == new_x_coord:
            requested_distance = abs(actor.get_coors()[1] - new_y_coord) * 5
        # horizontal
        elif actor.get_coors()[1] == new_y_coord:
            requested_distance = abs(actor.get_coors()[0] - new_x_coord) * 5
        else:
            requested_distance = (abs(actor.get_coors()[0] - new_x_coord) * 5) + (
                    abs(actor.get_coors()[1] - new_y_coord) * 5)
        if requested_distance > speed_remaining:
            return [0, "[ER] You're not fast enough! (Speed {})".format(actor.get_stat("Speed"))]

        self.mapList[y_coord - 1][(x_coord + ((1 * x_coord) - 1))] = ' '
        actor.set_coors(new_x_coord, new_y_coord, new_z_coord)
        return [requested_distance, False]

    def enc_fill_map(self, width=15, height=10):
        self.map_max_x = width
        self.map_max_y = height
        for i in range(0, height):
            newRow = list()
            newRow.append('|')
            for i in range(0, width):
                newRow.append(' ')
                newRow.append('|')
            self.mapList.append(newRow)

    def enc_update_map(self):
        for i in range(0, len(self.animateList)):
            xCoord = self.animateList[i].get_coors()[0]
            yCoord = self.animateList[i].get_coors()[1]
            self.mapList[yCoord - 1][(xCoord + ((1 * xCoord) - 1))] = self.animateList[i].get_name()[0]

    def enc_print_map(self):
        print()
        for i in range(0, len(self.mapList)):
            for j in range(0, len(self.mapList[i])):
                print(self.mapList[i][j], end='')
            print("")

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

    def inv_give(self, recipient, item_name, amount=1):
        if not recipient.get_iff() and self.currentEntity.inv_remove(item_name, amount=amount, discarding=True, notify=False) \
                and recipient.inv_add(item_name, amount=amount):
            print("[OK] You gave", recipient.get_name(), amount, item_name, "!")
        else:
            print("[ER] Cannot give", item_name, "to", recipient.get_name(), "!")

    # ===============================================================================
    # Dice & Check Methods
    # ===============================================================================
    @staticmethod
    def rollDice(rolls, number_of_faces, print_results=True) -> int:
        total = 0

        if (rolls < 1) or (type(rolls) != int):
            print("Rolls must be whole numbers > 1!!")
            return total

        valid_faces = [4, 6, 8, 10, 12, 20]
        if number_of_faces not in valid_faces:
            print(str(number_of_faces) + " is not a valid number of faces!!")
            print("Valid dice are: d4, d6, d8, d10, d12, and d20.")
            return total

        for roll in range(rolls):
            result = randint(1, number_of_faces)
            total += result

            if print_results:
                print("Rolling D{} {} of {}... Result is {}".format(number_of_faces, roll + 1, rolls, result))
        if print_results:
            print("Final total is... {}!!".format(total))
        return total

    def modifier(self, stat, ent):
        return floor(((ent.get_stat(stat)) - 10) / 2)

    def performCheck(self, stat, ent, advantage=False, disadvantage=False, print_results=True):
        roll = 0
        roll1 = self.rollDice(1, 20, False)
        roll2 = self.rollDice(1, 20, False)
        if (advantage and disadvantage) or (not advantage and not disadvantage):
            roll = roll1
        elif advantage:
            roll = max(roll1, roll2)
        elif disadvantage:
            roll = min(roll1, roll2)

        mod = self.modifier(stat, ent)
        if print_results:
            print("{} rolled {} with {} modifier {}".format(ent.get_name(), roll, stat, mod))
        roll += mod
        if print_results:
            print("Result is... {}!!".format(roll))
        return roll

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
            order.append((index, self.performCheck("Dexterity", ent, False, False, False)))
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
        attempt = self.performCheck("Strength", self.currentEntity, adv, disadv)
        # elif "ranged" in self.currentEntity.get_weapon().get_use():
        #     attempt = self.performCheck("Dexterity", self.currentEntity, adv, disadv)

        if attempt >= toHit:
            damage = self.rollDice(1, 20, False)
            self.dealDMG(damage, target)
        else:
            print("Attack failed!")
