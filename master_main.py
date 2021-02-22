# /etc/init.d/sample.py
### BEGIN INIT INFO
# Provides:          master_main.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO


from statblock import StatBlock
from random import randint
from campaign import Campaign
from enemy import Enemy
from display import Display
import player
import cencounter
import copy

# Parameters & CEncounter init.
# disp = Display()
# disp.page_startup()
# exit()

# ===============================================================================
# NCE Setup
# ===============================================================================
merchant = player.Animate("Willy", "Human", "Vendor")
merchant.inventory["Spear"] = 3
merchant.inventory["Padded Armor"] = 3
merchant.inventory["Mana Potion"] = 10
merchant.inventory["Scale Mail"] = 2

encounters = [cencounter.Encounter("Town"),
              cencounter.Encounter("Tavern"),
              cencounter.Encounter("Willy's Weapons", is_shop=True, vendor=merchant),
              cencounter.CEncounter("Haunted Forest")]

sBlocks = [StatBlock(), StatBlock(), StatBlock(), StatBlock(), StatBlock()]

players = [
    player.Player("Fjord", "Orc", "Warlock", stat_block=sBlocks[0]),
    player.Player("Jester Lavorre", "Tiefling", "Cleric", stat_block=sBlocks[1]),
    player.Player("Caleb Widowgast", "Human", "Wizard", stat_block=sBlocks[2]),
    player.Player("Yasha Nyoodrin", "Aasimar", "Barbarian", stat_block=sBlocks[3]),
    player.Player("Veth Brenatto", "Goblin", "Rogue", stat_block=sBlocks[4])]

for p in players:
    p.inv_add("Shortsword")
    p.inv_add("Dagger")
    p.inv_add("Chain Mail")
    p.inv_add("Padded Armor")
    p.inv_add("Mana Potion", randint(1, 6))
    p.inv_equip("Chain Mail")
    p.level_up()
    p.level_up()
    p.level_up()
    p.set_stats("Current HP", 1)
    p.set_stats("Constitution", randint(1, 17))
    p.money_add(5, 7, 300)

for e in encounters:
    e.animateList = copy.deepcopy(players)

# ===============================================================================
# CE Setup
# ===============================================================================
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

player_list = list()
MAP_MAX_X = 15
MAP_MAX_Y = 10

combat_enc = encounters[3]
combat_enc.enc_fill_map()

# Example Entities
combat_enc.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
combat_enc.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
combat_enc.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
for player in player_list:
    combat_enc.add_entity(player)
combat_enc.start_encounter()

# Creator Loop
for index in range(combat_enc.get_al_size()):
    actor = combat_enc.get_entity(True, index)

    while combat_enc.enc_move(actor, max(MAP_MAX_X, MAP_MAX_Y) * 5,
                       randint(1, MAP_MAX_X), randint(1, MAP_MAX_Y))[1]:
        pass

combat_enc.enc_update_map()
#combat_enc.enc_print_map()
actor = combat_enc.get_actor()
speed_remaining = actor.get_stat("Speed")
can_act = True
action = True

# ===============================================================================
# Run the campaign
# ===============================================================================
camp1 = Campaign("The Beginning of the End", encounters)
camp1.run_campaign()
