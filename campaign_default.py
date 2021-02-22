
from encounter import Encounter
from cencounter import CEncounter
from player import Player
from enemy import Enemy
from map import Map
from monsters import c_monsters
import pickle


def load_default_camp():
    # Encounter List Init
    DEFAULT_ENC = list()
    DEFAULT_ENC.append(1)

    foe_lists = list()
    foe_lists.append(list())
    foe_lists.append(list())
    foe_lists.append(list())

    foe_lists[0].append(c_monsters["Needle Blight"])
    foe_lists[0].append(c_monsters["Needle Blight"])
    foe_lists[0].append(c_monsters["Twig Blight"])
    foe_lists[0].append(c_monsters["Twig Blight"])
    foe_lists[0].append(c_monsters["Twig Blight"])
    foe_lists[1].append(c_monsters["Basilisk"])
    for num in range(5):
        foe_lists[2].append(c_monsters["Aarakocra"])

    # Non-combat Encounters
    DEFAULT_ENC.append(Encounter("[Zinnia] The Leaky Tap", bkgd="./assets/tavern.jpg"))
    DEFAULT_ENC.append(Encounter("[Zinnia] Al's Apothecary", bkgd="./assets/apothecary.jpg"))
    DEFAULT_ENC.append(Encounter("[Zinnia] The Bazaar", bkgd="./assets/bazaar.jpg"))

    DEFAULT_ENC.append(Encounter("[Adgard] Coral Inn", bkgd="./assets/coralinn.jpg"))
    DEFAULT_ENC.append(Encounter("[Adgard] Bard's Den", bkgd="./assets/tavern2.jpg"))
    DEFAULT_ENC.append(Encounter("[Adgard] Crownguard HQ", bkgd="./assets/guardhq.jpg"))

    # Combat Encounters
    DEFAULT_ENC.append(CEncounter("Verdant Wilds", inanim=foe_lists[0], tile="./assets/grasstile.png"))
    DEFAULT_ENC.append(CEncounter("Jagged Pass", inanim=foe_lists[1], tile="./assets/stonetile.png"))
    DEFAULT_ENC.append(CEncounter("Rivermouth", inanim=foe_lists[2], tile="./assets/grasstile2.png"))

    return DEFAULT_ENC
