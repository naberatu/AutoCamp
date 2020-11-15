
from enemy import Enemy
from player import Player
from inanimate import Inanimate
from random import randint
from math import floor


class Encounter:
    def __init__(self, max_inventory):
        self.currentEntity = None
        self.animateList = list()
        self.inanimateList = list()
        self.mapList = list()
        self.gamerule_inv_max = max_inventory   # Gamerule that determines if there will be max inventory size.
        self.turnOrder = list()                 # The animateList put in order of initiative
        self.turnCounter = 0

    def get_entity(self, is_animate, index):
        if is_animate:
            return self.animateList[index]
        else:
            return self.inanimateList[index]

    def get_actor(self):
        return self.currentEntity

    def set_actor(self, ent):
        self.currentEntity = ent

    def add_entity(self, ent):
        if isinstance(ent, Inanimate):
            self.inanimateList.append(ent)
        else:
            self.animateList.append(ent)
            if len(self.animateList) == 1:
                self.currentEntity = self.animateList[0]


    # ===============================================================================
    # Map & Movement Methods
    # ===============================================================================
    def get_map_tile_z(self, x_coor, y_coor):
        return self.mapList[x_coor][y_coor].get_z_coor()

    def map_display(self):
        for i in range(0, len(self.entityList)):
            print(self.animateList[i].get_name() + " is taking up " + self.animateList[i].get_size() + " of tile (" +
                  self.animateList[i].get_coors()[0] + ", " + self.animateList[i].get_coors()[1] + ")")

    def enc_move(self, entityToMove, newXCoord, newYCoord, newZCoord):
        attempted_distance = 0
        possible_distance = 0

        if entityToMove in self.animateList:
            possible_distance = entityToMove.get_stat("speed")
            if entityToMove.get_coors()[0] == newXCoord:
                attempted_distance = abs(entityToMove.get_coors()[0] - newXCoord) * 5
            elif entityToMove.get_coors()[1] == newYCoord:
                attempted_distance = abs(entityToMove.get_coors()[1] - newYCoord) * 5

        if attempted_distance > possible_distance:
            print("[ER] Movement illegal, Not enough speed to achieve desired movment")

        for i in range(0, len(self.animateList)):
            if self.animateList[i].get_coors()[0] == newXCoord and self.animateList[i].get_coors()[2] == newYCoord and \
                    self.animateList[i].get_coors()[1] == newYCoord and \
                    self.animateList[i].get_tile_size() + entityToMove.get_tile_size() > 1:
                print("[ER] Movement illegal, another entity is at target position")
            else:
                entityToMove.set_coors(newXCoord, newYCoord, newZCoord)
                print("[OK] " + entityToMove.get_name() + " successfully moved")

    # ===============================================================================
    # Inventory Methods
    # ===============================================================================
    def inv_get(self):
        return self.currentEntity.get_inv()

    def inv_pickup(self, item_id, inv, amount, hot_swap, is_armor):
        if hot_swap:
            inv.inv_add(item_id, amount)
            self.inv_equip(is_armor, item_id, inv)
        else:
            inv.inv_add(item_id, amount)

    def inv_discard(self, item_id, inv, amount):
        inv.inv_remove(item_id, amount, True, False)

    def inv_sell(self, item_id, amount, inv):
        inv.inv_remove(item_id, amount, False, True)

    def inv_use(self, item_id, inv):        # pass in self.currentEntity.get_inv()
        item = inv.inv_remove(item_id, 1, False, False)
        if item is not None:
            # run the actual effect
            print("[OK] You used ", item.get_name(), "!")

    def inv_give(self, acceptor, item_id, amount, inv):
        if not acceptor.is_enemy():
            item = inv.inv_remove(item_id, amount, False, False)
            acceptor.inv_add(item)
            print("[OK] You gave", acceptor.get_name(), " ", item.get_name(), "!")
        else:
            print("[ER] You can’t give that to ", acceptor.get_name(), "!")

    def inv_equip(self, is_armor, item_id, inv):
        item = inv.inv_remove(item_id, 1, False, False)
        if is_armor:
            armor = self.currentEntity.get_armor()
            self.currentEntity.inv_add(armor)
            self.currentEntity.set_armor(item)
            print("[OK]: You have swapped your armor!")
        else:
            weapon = self.currentEntity.get_weapon()
            self.currentEntity.inv_add(weapon)
            self.currentEntity.set_armor(item)
            print("[OK]: You have swapped your weapon!")

    # ===============================================================================
    # Dice & Check Methods
    # ===============================================================================
    @staticmethod
    def rollDice(rolls, numOfFaces, print_results=True) -> int:
        total = 0

        validFaces = [4, 6, 8, 10, 12, 20]
        if numOfFaces not in validFaces:
            print(str(numOfFaces) + " is not a valid number of faces!!")
            print("Valid dice are: d4, d6, d8, d10, d12, and d20.")
            return total

        if (rolls < 1) or (type(rolls) != int):
            print("Rolls must be whole numbers > 1!!")
            return total

        for roll in range(rolls):
            result = randint(1, numOfFaces)
            total += result

            if print_results:
                print("Rolling D{} {} of {}... Result is {}".format(numOfFaces, roll + 1, rolls, result))
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

    def showStats(self) -> None:
        currEnt = self.currentEntity
        statKeys = list(self.currentEntity.stat_block.stats.keys())
        statValues = list(self.currentEntity.stat_block.stats.values())

        print("{:^60}".format("*~*~* " + currEnt.get_name() + "'s stats!! *~*~*"))

        if (type(currEnt) == Player) or (type(currEnt) == Enemy):
            print("Level & Class: Lvl.", currEnt.get_level(), currEnt.get_role())
        else:
            print("Class:", currEnt.get_role())

        print("Race:", currEnt.get_race())

        if type(currEnt) == Player:
            print("Max Inventory Weight:", currEnt.maxInvWeight)
            print("Companion:", currEnt.companion)
            print("EXP:", currEnt.get_exp())

        if type(currEnt) == Enemy:
            print("EXP Yield:", currEnt.get_exp_yield())

        print("\n > ABILITY SCORES")

        for x in range(3):
            print('{:20}{:20}'.format(statKeys[x * 2] + ": " + str(statValues[x * 2]),
                                      statKeys[(x * 2) + 1] + ": " + str(statValues[(x * 2) + 1])))

        print("\n > MISC STATS")
        print('Inspiration: {:<7}Proficiency Bonus: {}'.format(statValues[6], statValues[7]))

        print("\n > CHARACTER STATS")
        for x in range(2):
            print("{:17}{:17}{:17}".format(statKeys[8 + (x * 3)] + ': ' + str(statValues[8 + (x * 3)]),
                                           statKeys[9 + (x * 3)] + ': ' + str(statValues[9 + (x * 3)]),
                                           statKeys[10 + (x * 3)] + ': ' + str(statValues[10 + (x * 3)])))
        print("\n > SKILLS")
        for x in range(6):
            print("{:22}{:22}{:22}".format(statKeys[14 + (x * 3)] + ': ' + str(statValues[14 + (x * 3)]),
                                           statKeys[15 + (x * 3)] + ': ' + str(statValues[15 + (x * 3)]),
                                           statKeys[16 + (x * 3)] + ': ' + str(statValues[16 + (x * 3)])))

    # ===============================================================================
    # Combat Methods
    # ===============================================================================
    def determineInitiative(self):
        order = []
        index = 0
        for ent in self.animateList:
            # order.append((ent.get_name(), self.performCheck("Dexterity", ent)))
            order.append((index, self.performCheck("Dexterity", ent)))
            index += 1
        order = sorted(order, key=lambda x: - x[1])

        print("Determining initiative...")
        print("Turn Order Is: ")
        self.animateList[:] = [self.animateList[i[0]] for i in order]
        for ent in self.animateList:
            # print(ent[0])
            print(ent.get_name())
        # self.turnOrder = order

    def next_turn(self):
        self.turnCounter += 1
        self.currentEntity = self.animateList[self.turnCounter % len(self.animateList)]

    def dealDMG(self, damage, target):
        targetHealth = target.get_stat("Current HP")
        targetHealth -= damage
        if targetHealth >= 0:
            target.set_stats("Current HP", targetHealth)
        else:
            target.set_stats("Current HP", 0)

        print(self.currentEntity.get_name(), "attacked", target.get_name(), "!!")
        print(target.get_name(), "took", damage, "damage!!")
        print(target.get_name(), "is now at", target.get_stat("Current HP"), "/",
              target.get_stat("Max HP"), "HP.")

    def attack(self, target, adv, disadv) -> None:
        toHit = target.get_stat("Armor Class")
        attempt = 0

        if "melee" in self.currentEntity.get_weapon().get_use():
            attempt = self.performCheck("Strength", self.currentEntity, adv, disadv)
        elif "ranged" in self.currentEntity.get_weapon().get_use():
            attempt = self.performCheck("Dexterity", self.currentEntity, adv, disadv)

        if attempt >= toHit:
            damage = self.rollDice(1, 20, False)
            self.dealDMG(damage, target)
        else:
            print("Attack failed!")
