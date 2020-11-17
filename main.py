from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
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
            "profile": "Displays your stats."
}


def print_inv(self, full_inv, inv=None):
    if inv is None:
        inv = enc.inv_get()
    if inv == {}:
        print("[ER] Your inventory is empty!")
        return

    print("=============================================================================")
    print(actor.get_name() + "\'s Inventory")
    print("-----------------------------------------------------------------------------")

    if full_inv:
        print("Weapon: " + "{:<20}".format(actor.get_weapon().get_name())
              + "\tArmor: " + "{:<20}".format(actor.get_armor().get_name()))
        print("=============================================================================")

    for item, quantity in inv.items():
        print("{:<20}".format(item.get_name()).ljust(20) + "\t\tx" + str(quantity))
    print("=============================================================================")


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

    while enc.enc_move(actor, random.randint(1, MAP_MAX_X), random.randint(1, MAP_MAX_Y)):
        pass

print("\nWelcome to the AutoCamp Demonstration v0.2")
enc.enc_update_map()
enc.enc_print_map()

while True:
    can_act = True
    action = True
    actor = enc.get_actor()

    print("\n[", actor.get_name(), "] what would you like to do?")
    ans = input("> ")

    if ans.lower() == "help":
        print("\nList of Commands:")
        for com, desc in commands.items():
            print("> ", com.ljust(7), "\t", desc)
        ans = input("> ")

    if ans.lower() == "act" and can_act:
        print("\nPlease select an action to take:")
        print("> attack", "\n> use item", "\n> hold action")
        ans = input("> ")

        if ans.lower() == "cancel":
            continue

        if ans.lower() == ("attack" or "use item" or "hold action"):
            action = True

    elif ans.lower() == "act" and not can_act:
        print("[ER] You cannot act this turn!")

    elif ans.lower() == "move":
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

        response = enc.enc_move(actor, new_x, new_y)
        if not cancel and not response:
            enc.enc_update_map()
            enc.enc_print_map()
            print(actor.get_name(), "moved to", actor.get_coors())
        else:
            enc.enc_print_map()
            print(response)

    elif ans.lower() == "profile":
        enc.showStats()

    elif ans.lower() == "inventory":
        print_inv(True, enc.inv_get())

    elif ans.lower() == "end":
        print("Your turn has ended.")
        enc.enc_print_map()
        enc.next_turn()
        continue

    elif ans.lower() == "exit":
        print("Game Over! Thanks for playing!")
        break

    # Action Menus:
    # ===============================================================================
    if action:
        if ans.lower() == "attack":
            enemiesInRange = enc.enemyInRange()  # max map x and y are 4's for testing purposes only
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

                elif ans.lower() in alpha:
                    enc.attack(enemiesInRange[alpha.index(ans.lower())], False, False)

        elif ans.lower() == "use item":
            inv = enc.inv_get()
            success = False
            print_inv(False, inv)
            while not success:
                item_name = input("Item: ")
                if item_name.lower() == "cancel":
                    break
                for i in list(inv.keys()):
                    if i.get_name() == item_name:
                        success = enc.inv_use(i, True)

        action = False
        can_act = False
