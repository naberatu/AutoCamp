#!/usr/bin/python

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
# from display import Display
from encounter import Encounter
from player import Player
from statblock import StatBlock
from enemy import Enemy
import items
import random
import pickle


commands = {
            "act": "Opens action menu.",
            "end": "Ends the current turn",
            "exit": "Ends the program.",
            "help": "Displays list of commands.",
            "hero": "Displays your stats.",
            "hint": "Provides a hint if possible.",
            "inv": "Displays inventory.",
            "map": "Displays map once again.",
            "move": "Change current position (or \'move x y\').",
            "use": "Uses an item from inventory."
}

# Parameters & Encounter init.
# disp = Display()

try:
    enc = pickle.load(open("savegame.camp", "rb"))
except:
    enc = Encounter()
    MAP_MAX_X = 15
    MAP_MAX_Y = 10
    enc.enc_fill_map(MAP_MAX_X, MAP_MAX_Y)

    # Example Entities
    enc.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
    enc.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
    enc.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
    enc.add_entity(Player("Fjord", "Orc", "Warlock"))
    enc.add_entity(Player("Jester Lavorre", "Tiefling", "Cleric"))
    enc.add_entity(Player("Caleb Widowgast", "Human", "Wizard"))
    enc.add_entity(Player("Yasha Nyoodrin", "Aasimar", "Barbarian"))
    enc.add_entity(Player("Veth Brenatto", "Goblin", "Rogue"))
    enc.start_encounter()

    # Done to ensure the item actually exists.
    sword = items.catalog["Shortsword"].get_name()
    armor = items.catalog["Chain Mail"].get_name()
    potion = items.catalog["Mana Potion"].get_name()

    # Creator Loop
    for index in range(enc.get_al_size()):
        actor = enc.get_entity(True, index)

        if type(actor) == Enemy:
            actor.set_stats("Max HP", 25)

        if type(actor) == Player:
            actor.set_weapon(sword)
            actor.set_armor(armor)
            actor.inv_add(potion, random.randint(1, 6))

        while enc.enc_move(actor, max(MAP_MAX_X, MAP_MAX_Y) * 5,
                           random.randint(1, MAP_MAX_X), random.randint(1, MAP_MAX_Y))[1]:
            pass

    # Saving Loop
    player_list = list()
    for index in range(enc.get_al_size()):
        entity = enc.get_entity(True, index)
        if type(entity) == Player:
            player_list.append(entity)

    pickle.dump(player_list, open("players.camp", "wb"))
    pickle.dump(enc, open("savegame.camp", "wb"))

# End Except statement


print("\nWelcome to the AutoCamp Demonstration v1.3")
# disp.game_intro()

enc.enc_update_map()
enc.enc_print_map()
actor = enc.get_actor()
speed_remaining = actor.get_stat("Speed")
can_act = True
action = True

while True:
    if "unconscious" in actor.get_conditions() and type(actor) == Player:
        if not actor.is_stable and enc.death_saves == 0:
            death_save = enc.rollDice(1, 20, False)
            enc.death_saves += 1
            if death_save >= 10:
                actor.set_death_evasions(actor.get_death_evasions() + 1)
                print("Death save succeeded!")

            else:
                if death_save == 1:  # +2 strikes if 1
                    actor.set_death_strikes(actor.get_death_strikes() + 1)
                actor.set_death_strikes(actor.get_death_strikes() + 1)
                print("Death save failed")

            if actor.get_death_evasions() >= 3 or death_save == 20:
                actor.mod_conditions(False, "unconscious")
                print(actor.get_name(), "is no longer unconscious!!")
                actor.set_stability(True)
                actor.set_death_evasions(0)
                actor.set_death_strikes(0)
                if death_save == 20:
                    actor.set_stats("Current HP", 1)

            elif actor.get_death_strikes() >= 3:
                print(actor.get_name(), "has died!!")
                actor.set_death_evasions(0)
                actor.set_death_strikes(0)
                enc.animateList.remove(actor)
                print("Your turn has ended.")
                enc.enc_print_map()
                enc.next_turn()
                continue

    print("\n[", actor.get_name(), "] what would you like to do?")
    ans = input("> ")

    if ans.lower().strip() == "help":
        print("\nList of Commands:")
        for com, desc in commands.items():
            print("> ", com.ljust(7), "\t", desc)
        ans = input("> ")

    if ans.lower().strip() == "act" and can_act:
        print("\nPlease select an action to take:")
        print("> attack", "\n> use", "\n> end")
        ans = input("> ")

        if ans.lower() == "cancel":
            continue

        if ans.lower() == ("attack" or "use" or "end"):
            action = True

    elif ans.lower().strip() == "act" and not can_act:
        print("[ER] You cannot act this turn!")

    elif "move" in ans.lower().strip():
        if "unconscious" in actor.get_conditions():
            print(actor.get_name(), "can't move! They're unconscious!")
        else:
            one_step = False
            if ans.lower().strip() == "move":
                print("\nWhere to?  (from " + str(actor.get_coors()[0]) + ", " + str(actor.get_coors()[1]) + ")")
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
                    response = enc.enc_move(actor, speed_remaining, x, y)
                    if not response[1]:
                        enc.enc_update_map()
                        enc.enc_print_map()
                        print(actor.get_name(), "moved to", actor.get_coors())
                        speed_remaining -= response[0]
                    else:
                        enc.enc_print_map()
                        print(response[1])
            except:
                print("[ER] Invalid input. Please try again.")
                continue

    elif ans.lower().strip() == "hero":
        enc.showStats()

    elif ans.lower().strip() == "inv":
        actor.inv_print()

    elif ans.lower().strip() == "end":
        print("Your turn has ended.")
        enc.enc_print_map()
        enc.next_turn()
        actor = enc.get_actor()
        speed_remaining = actor.get_stat("Speed")
        can_act = True
        action = True
        continue

    elif ans.lower().strip() == "exit":
        # Begin collecting players.
        entity_list = list()
        for index in range(enc.get_al_size()):
            entity = enc.get_entity(True, index)
            if type(entity) == Player:
                entity_list.append(entity)

        # Save all players to players.camp.
        entity_file = open("players.camp", "wb")
        pickle.dump(entity_list, entity_file)
        entity_file.close()

        # Save the current encounter.
        camp_file = open("savegame.camp", "wb")
        pickle.dump(enc, camp_file)
        camp_file.close()

        # Exit game
        print("Game Over! Thanks for playing!")
        break

    elif ans.lower().strip() == "hint":
        print(enc.get_hint())

    elif ans.lower().strip() == "map":
        enc.enc_print_map()

    # Action Menus:
    # ===============================================================================
    elif action:
        success = False
        if ans.lower().strip() == "attack":
            if "unconscious" in actor.get_conditions():
                print(actor.get_name(), "can't attack! They're unconscious!")
            else:
                enemiesInRange = enc.enemyInRange()
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
                        enc.attack(enemiesInRange[alpha.index(ans.lower())], False, False)
                        success = True
                        # action = False
                        # can_act = False

        elif "use" in ans.lower().strip():
            if "unconscious" in actor.get_conditions():
                print(actor.get_name(), "can't use an item! They're unconscious!")
            else:
                if ans.lower().strip() == "use":
                    active = actor.inv_print(False)
                    while active and not success:
                        item_name = input("Item: ")
                        if item_name.lower() == "":
                            break
                        success = actor.inv_remove(item_name, using=True)
                else:
                    use, item_name = ans.split(' ', 1)
                    if use.lower() == "use":
                        actor.inv_remove(item_name, using=True)
                    else:
                        print("[ER] Invalid input. Please try again.")
                        continue

        elif ans.lower().strip() == "end":
            print("Your turn has ended.")
            enc.enc_print_map()
            enc.next_turn()
            actor = enc.get_actor()
            speed_remaining = actor.get_stat("Speed")
            can_act = True
            action = True
            continue

        if success:
            action = False
            can_act = False

    elif not action:
        print("You already acted this turn!")
    else:
        print("[ER] Invalid input, please try again.")

