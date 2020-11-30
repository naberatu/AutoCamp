from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from encounter import Encounter
from player import Player
from statblock import StatBlock
from inanimate import Inanimate
from enemy import Enemy
import random

commands = {
            "act": "Opens action menu.",
            "end": "Ends the current turn",
            "exit": "Ends the program.",
            "help": "Displays list of commands.",
            "inventory": "Displays inventory.",
            "move": "Changes your current position.",
            "profile": "Displays your stats.",
            "use": "Uses an item from inventory."
}

# Parameters & Encounter init.
enc = Encounter("slot")
MAP_MAX_X = 15
MAP_MAX_Y = 10

# Example Entities
enc.add_entity(Enemy("Werewolf", random.randint(1, 10000), "Wolf", "Doggo", 1, StatBlock()))
enc.add_entity(Enemy("Werewolf", random.randint(1, 10000), "Wolf", "Doggo", 1, StatBlock()))
enc.add_entity(Enemy("Werewolf", random.randint(1, 10000), "Wolf", "Doggo", 1, StatBlock()))
enc.add_entity(Player("Fjord", random.randint(1, 10000), "Orc", "Warlock", 1, StatBlock()))
enc.add_entity(Player("Jester Lavorre", random.randint(1, 10000), "Tiefling", "Cleric", 1, StatBlock()))
enc.add_entity(Player("Caleb Widowgast", random.randint(1, 10000), "Human", "Wizard", 1, StatBlock()))
enc.add_entity(Player("Yasha Nyoodrin", random.randint(1, 10000), "Aasimar", "Barbarian", 1, StatBlock()))
enc.add_entity(Player("Veth Brenatto", random.randint(1, 10000), "Goblin", "Rogue", 1, StatBlock()))
enc.start_encounter()
enc.enc_fill_map(MAP_MAX_X, MAP_MAX_Y)

sword = Inanimate("Iron Sword", 0, 1, 20, "Deals +2 Damage", 1, 4)
armor = Inanimate("Chainmail", 1, 2, 20, "Provides +10 AC", 1, 6)
potion = Inanimate("Mana Potion", 2, 3, 30, "Restores Mana", 6, 0.5)

for index in range(enc.get_al_size()):
    actor = enc.get_entity(True, index)

    if type(actor) == Enemy:
        actor.set_stats("Max HP", 25)

    if type(actor) == Player:
        actor.inv_add(sword, 1)
        actor.inv_add(armor, 1)
        actor.inv_add(potion, random.randint(1, 6))
        actor.set_weapon(sword)
        actor.set_armor(armor)

    while enc.enc_move(actor, max(MAP_MAX_X, MAP_MAX_Y) * 5,
                       random.randint(1, MAP_MAX_X), random.randint(1, MAP_MAX_Y))[1]:
        pass

print("\nWelcome to the AutoCamp Demonstration v0.3")
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
        print("> attack", "\n> use item", "\n> hold action")
        ans = input("> ")

        if ans.lower() == "cancel":
            continue

        if ans.lower() == ("attack" or "use item" or "hold action"):
            action = True

    elif ans.lower().strip() == "act" and not can_act:
        print("[ER] You cannot act this turn!")

    elif ans.lower().strip() == "move":
        if "unconscious" in actor.get_conditions():
            print(actor.get_name(), "can't move! They're unconscious!")
        else:
            print("\nWhere to?  (from " + str(actor.get_coors()[0]) + ", " + str(actor.get_coors()[1]) + ")")
            cancel = False
            new_x = new_y = 0

            while True:
                if not new_x:
                    x = input("X: ")
                    if x == "cancel":
                        cancel = True
                        break
                    try:
                        new_x = int(x)
                    except:
                        print("[ER] Invalid input. Please try again.")
                        continue
                if not new_y:
                    y = input("Y: ")
                    if y == "cancel":
                        cancel = True
                        break
                    try:
                        new_y = int(y)
                    except:
                        print("[ER] Invalid input. Please try again.")
                        continue
                if new_x and new_y: break

            response = enc.enc_move(actor, speed_remaining, new_x, new_y)
            if not cancel and not response[1]:
                enc.enc_update_map()
                enc.enc_print_map()
                print(actor.get_name(), "moved to", actor.get_coors())
                speed_remaining -= response[0]
            else:
                enc.enc_print_map()
                print(response[1])

    elif ans.lower().strip() == "profile":
        enc.showStats()

    elif ans.lower().strip() == "inventory":
        actor.print_inv(True)

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
        print("Game Over! Thanks for playing!")
        break

    # Action Menus:
    # ===============================================================================
    if action:
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

        elif ans.lower().strip() == "use":
            if "unconscious" in actor.get_conditions():
                print(actor.get_name(), "can't use an item! They're unconscious!")
            else:
                success = False
                active = actor.print_inv(False)
                while active and not success:
                    item_name = input("Item: ")
                    if item_name.lower() == "cancel":
                        break
                    success = enc.inv_use(item_name, True)

        action = False
        can_act = False


