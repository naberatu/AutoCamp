#!/usr/bin/python

import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from display import Display
from encounter import Encounter
from player import Player
from statblock import StatBlock
from enemy import Enemy
import items
import random
import pickle


commands = {
            "act": "Opens ACTION menu.",
            "end": "Ends the current turn",
            "exit": "Ends the program.",
            "help": "Displays list of commands.",
            "hero": "Displays your stats.",
            "hint": "Provides a hint if possible.",
            "handbook": "Display the Basic Rules",
            "inv": "Displays inventory.",
            "stats": "Displays stats",
            "cond": "Displays conditions",
            "map": "Displays map once again.",
            "move": "Change current position (or \'move x y\').",
            "use": "Uses an item from inventory."
}

# Parameters & Encounter init.
disp = Display()
player_list = list()
MAP_MAX_X = 15
MAP_MAX_Y = 10
RELOAD_ENC = False
EMPTY_LIST = []


try:
    player_list = pickle.load(open("players.camp", "rb"))
    # player_list[1].mod_conditions(condition="Paralyzed", duration=2, adding=True)
    # RELOAD_ENC = True
except:

    player_list.append(Player("Fjord", "Orc", "Warlock"))
    player_list.append(Player("Jester Lavorre", "Tiefling", "Cleric"))
    player_list.append(Player("Caleb Widowgast", "Human", "Wizard"))
    player_list.append(Player("Yasha Nyoodrin", "Aasimar", "Barbarian"))
    player_list.append(Player("Veth Brenatto", "Goblin", "Rogue"))

    for hero in player_list:
        hero.set_weapon("Shortsword")
        hero.set_armor("Chain Mail")
        hero.inv_add("Mana Potion", random.randint(1, 6))

    pickle.dump(EMPTY_LIST, open("players.camp", "wb"))
    pickle.dump(player_list, open("players.camp", "wb"))
    RELOAD_ENC = True


try:
    if RELOAD_ENC:
        RELOAD_ENC = False
        raise KeyError
    ENC = pickle.load(open("savegame.camp", "rb"))
except:
    ENC = Encounter()
    ENC.enc_fill_map()

    # Example Entities
    ENC.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
    ENC.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
    ENC.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
    for player in player_list:
        ENC.add_entity(player)
    ENC.start_encounter()

    # Creator Loop
    for index in range(ENC.get_al_size()):
        entity = ENC.get_entity(True, index)

        while ENC.enc_move(entity, max(MAP_MAX_X, MAP_MAX_Y) * 5,
                           random.randint(1, MAP_MAX_X), random.randint(1, MAP_MAX_Y))[1]:
            pass

    pickle.dump(EMPTY_LIST, open("savegame.camp", "wb"))
    pickle.dump(ENC, open("savegame.camp", "wb"))

# End Except statement


print("\nWelcome to the AutoCamp Demonstration v1.3")
disp.page_startup()

ENC.enc_update_map()
ENC.enc_print_map()
ACTOR = ENC.get_actor()
SPEED_REM = ACTOR.get_stat("Speed")
CAN_ACT = True
ACTION = True
ADVANTAGE = False
DISADVANTAGE = False


def cond_ok(try_move=False, try_act=False, try_poison=False, try_unstable=False):
    global CAN_ACT
    global SPEED_REM
    global ACTOR

    if try_poison and "Poisoned" in ACTOR.get_conditions().keys():
        return True         # Say that we are poisoned.

    if try_act:
        cond_list = {"Petrified", "Paralyzed", "Stunned", "Incapacitated"}
        for cond in cond_list:
            if cond in ACTOR.get_conditions().keys():
                CAN_ACT = False
                return cond
        return False

    if try_move:
        cond_list = {"Petrified", "Paralyzed", "Stunned", "Incapacitated", "Restrained", "Grappled"}
        for cond in cond_list:
            if cond in ACTOR.get_conditions().keys():
                SPEED_REM = 0
                return cond
        return False

    if try_unstable and "Unconscious" in ACTOR.get_conditions():
        if not ACTOR.is_stable and ENC.death_saves == 0:
            death_save = ENC.rollDice(1, 20, False)
            ENC.death_saves += 1
            if death_save >= 10:
                ACTOR.set_death_evasions(ACTOR.get_death_evasions() + 1)
                print("Death save succeeded!")

            else:
                if death_save == 1:  # +2 strikes if 1
                    ACTOR.set_death_strikes(ACTOR.get_death_strikes() + 1)
                ACTOR.set_death_strikes(ACTOR.get_death_strikes() + 1)
                print("Death save failed")

            if ACTOR.get_death_evasions() >= 3 or death_save == 20:
                ACTOR.mod_conditions("Unconscious", adding=False)
                print(ACTOR.get_name(), "is no longer unconscious!!")
                ACTOR.set_stability(True)
                ACTOR.set_death_evasions(0)
                ACTOR.set_death_strikes(0)
                if death_save == 20:
                    ACTOR.set_stats("Current HP", 1)
                return True

            elif ACTOR.get_death_strikes() >= 3:
                print(ACTOR.get_name(), "has died!!")
                ACTOR.set_death_evasions(0)
                ACTOR.set_death_strikes(0)
                ENC.animateList.remove(ACTOR)
                print("Your turn has ended.")
                ENC.enc_print_map()
                ENC.next_turn()
                return False
    elif not try_poison:
        return True


# AutoCamp Mainloop
while True:
    if not cond_ok(try_unstable=True):
        continue
    cond_ok(try_act=True)
    DISADVANTAGE = cond_ok(try_poison=True)

    print("\n[", ACTOR.get_name(), "] what would you like to do?")
    ans = input("> ")

    if ans.lower().strip() == "stats":
        ACTOR.showStats()

    elif ans.lower().strip() == "handbook":
        os.system('C:/Users/elite/PycharmProjects/autocamp32/docs/dnd_basicrules.pdf')

    elif ans.lower().strip() == "check":
        ENC.performCheck("Constitution", ACTOR, ADVANTAGE, DISADVANTAGE)

    elif ans.lower().strip() == "cond":
        print(ACTOR.get_conditions())

    elif ans.lower().strip() == "help":
        print("\nList of Commands:")
        for com, desc in commands.items():
            print("> ", com.ljust(7), "\t", desc)
        ans = input("> ")

    elif ans.lower().strip() == "act":
        condition = cond_ok(try_act=True)

        if condition:
            print("[ER] You cannot act, you are {}!".format(condition))
        elif not CAN_ACT:
            print("[ER] You already used your turn!")
        else:
            print("\nPlease select an ACTION to take:")
            print("> attack", "\n> use", "\n> end")
            ans = input("> ")

            if ans.lower() == "cancel":
                continue

            if ans.lower() == ("attack" or "use" or "end"):
                ACTION = True

    elif "move" in ans.lower().strip():
        condition = cond_ok(try_move=True)
        if condition:
            print("[ER] You cannot move, you are {}!".format(condition))
        elif SPEED_REM <= 0:
            print("[ER] Cannot move! Speed is", SPEED_REM)
        else:
            one_step = False
            if ans.lower().strip() == "move":
                print("\nWhere to?  (from {}, {}) (Speed {})".format(str(ACTOR.get_coors()[0]), str(ACTOR.get_coors()[1]), SPEED_REM))
            else:
                one_step = True
            try:
                if one_step:
                    move, x, y = ans.lower().split()
                else:
                    ans = input("> ")
                    if ans.lower().strip() == "cancel":
                        continue
                    x, y = ans.split()

                x = int(x)
                y = int(y)
                # if one_step and move.lower() != "move":
                if one_step and move != "move":
                    print("[ER1] Invalid input. Please try again.")
                    continue
                else:
                    response = ENC.enc_move(ACTOR, SPEED_REM, x, y)
                    if not response[1]:
                        ENC.enc_update_map()
                        ENC.enc_print_map()
                        print(ACTOR.get_name(), "moved to", ACTOR.get_coors())
                        SPEED_REM -= response[0]
                    else:
                        ENC.enc_print_map()
                        print(response[1])
            except:
                print("[ER] Invalid input. Please try again.")
                continue

    elif ans.lower().strip() == "hero":
        ENC.showStats()

    elif ans.lower().strip() == "inv":
        ACTOR.inv_print()

    elif ans.lower().strip() == "end":
        # For the Old Actor
        ACTOR.condition_tick()  # tick down 1 turn or 6 seconds.
        ADVANTAGE = False
        DISADVANTAGE = False
        print("Your turn has ended.")

        # For the New Actor
        ENC.enc_print_map()
        ENC.next_turn()
        ACTOR = ENC.get_actor()
        SPEED_REM = ACTOR.get_stat("Speed")
        CAN_ACT = True
        ACTION = True
        continue

    elif ans.lower().strip() == "exit":
        # Begin collecting players.
        entity_list = list()
        for index in range(ENC.get_al_size()):
            entity = ENC.get_entity(True, index)
            if type(entity) == Player:
                entity_list.append(entity)

        # Save all players to players.camp.
        entity_file = open("players.camp", "wb")
        pickle.dump(entity_list, entity_file)
        entity_file.close()

        # Save the current encounter.
        camp_file = open("savegame.camp", "wb")
        pickle.dump(ENC, camp_file)
        camp_file.close()

        # Exit game
        print("Game Over! Thanks for playing!")
        break

    elif ans.lower().strip() == "hint":
        print(ENC.get_hint())

    elif ans.lower().strip() == "map":
        ENC.enc_print_map()

    # Action Menus:
    # ===============================================================================
    elif ACTION:
        condition = cond_ok(try_act=True)
        success = False

        if condition:
            print("[ER] You cannot act, you are {}!".format(condition))
        elif ans.lower().strip() == "attack":
            if "unconscious" in ACTOR.get_conditions():
                print(ACTOR.get_name(), "can't attack! They're unconscious!")
            else:
                enemiesInRange = ENC.enemyInRange()
                if not enemiesInRange:
                    print("Sorry! No enemies in range of attack.")
                else:
                    print("Which enemy would you like to attack?")
                    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                    for e in range(len(enemiesInRange)):
                        print(alpha[e], "-", enemiesInRange[e].get_name(), "@", enemiesInRange[e].get_coors())

                    ans = input("> ")
                    if ans.lower() == "cancel":
                        continue

                    elif ans.lower() in alpha[:len(enemiesInRange)]:
                        ENC.attack(enemiesInRange[alpha.index(ans.lower())], ADVANTAGE, DISADVANTAGE)
                        success = True

        elif "use" in ans.lower().strip():
            if "unconscious" in ACTOR.get_conditions():
                print(ACTOR.get_name(), "can't use an item! They're unconscious!")
            else:
                if ans.lower().strip() == "use":
                    active = ACTOR.inv_print(False)
                    while active and not success:
                        item_name = input("Item: ")
                        if item_name.lower() == "":
                            break
                        success = ACTOR.inv_remove(item_name, using=True)
                else:
                    use, item_name = ans.split(' ', 1)
                    if use.lower() == "use":
                        ACTOR.inv_remove(item_name.lower(), using=True)
                    else:
                        print("[ER] Invalid input. Please try again.")
                        continue

        elif ans.lower().strip() == "end":
            print("Your turn has ended.")
            ENC.enc_print_map()
            ENC.next_turn()
            ACTOR = ENC.get_actor()
            SPEED_REM = ACTOR.get_stat("Speed")
            CAN_ACT = True
            ACTION = True
            continue

        if success:
            ACTION = False
            CAN_ACT = False

    elif not ACTION:
        print("You already acted this turn!")
    else:
        print("[ER] Invalid input, please try again.")

