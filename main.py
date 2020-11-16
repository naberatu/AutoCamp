from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from encounter import Encounter
from player import Player
from statblock import StatBlock
from inanimate import Inanimate
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
enc.add_entity(Player("Fjord", random.randint(1, 10000), "Orc", "Warlock", 1, StatBlock()))
enc.add_entity(Player("Jester Lavorre", random.randint(1, 10000), "Tiefling", "Cleric", 1, StatBlock()))
enc.add_entity(Player("Caleb Widowgast", random.randint(1, 10000), "Human", "Wizard", 1, StatBlock()))
enc.add_entity(Player("Yasha Nyoodrin", random.randint(1, 10000), "Aasimar", "Barbarian", 1, StatBlock()))
enc.add_entity(Player("Veth Brenatto", random.randint(1, 10000), "Goblin", "Rogue", 1, StatBlock()))

sword = Inanimate("Iron Sword", 00000, 1, 20, "Deals +2 Damage", 1, 4)
armor = Inanimate("Chainmail", 00000, 2, 20, "Provides +10 AC", 1, 6)
potion = Inanimate("Mana Potion", 00000, 3, 30, "Restores Mana", 10, 0.5)

enc.start_encounter()

for i in range(5):
    hero = enc.get_entity(True, i)
    hero.set_coors(1, 1, 0)
    hero.set_stats("Animal Handling", -3)
    enc.inv_pickup(sword, 1, True, False, False)
    enc.inv_pickup(armor, 1, True, True, False)
    enc.inv_pickup(potion, 1, False, False, False)
enc.determineInitiative()

print("\nWelcome to the AutoCamp Demonstration v0.1")

while True:
    can_act = True
    action = True
    actor = enc.get_actor()
    speed = actor.get_stat("Speed")

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
        if speed <= 0:
            print("You've exhausted all your movement!")
            continue
        else:
            print("You are currently at x = ", actor.get_coors()[0], ", y = ", actor.get_coors()[1])
            print("Where would you like to go?")
            x = y = 0
            cancel = False
            while True:
                if x == 0:
                    x = int(input("X: "))
                    if x == "cancel":
                        cancel = True
                        break
                    elif type(x) != int:
                        print("[ER] Invalid input. Please try again.")
                        continue
                if y == 0:
                    y = int(input("Y: "))
                    if y == "cancel":
                        cancel = True
                        break
                    elif type(y) != int:
                        print("[ER] Invalid input. Please try again.")
                        continue
                if x != 0 and y != 0: break

            if not cancel:
                enc.enc_move(actor, x, y, 0)
                print(actor.get_coors())

    elif ans.lower() == "profile":
        enc.showStats()

    elif ans.lower() == "inventory":
        print_inv(True, enc.inv_get())

    elif ans.lower() == "end":
        print("Your turn has ended.")
        enc.next_turn()
        continue

    elif ans.lower() == "exit":
        print("Game Over! Thanks for playing!")
        break

    # Action Menus:
    # ===============================================================================
    if action:
        if ans.lower() == "attack":
            print("Attack!")

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



