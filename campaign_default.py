
from encounter import Encounter
from cencounter import CEncounter
from monsters import c_monsters
import copy


def load_default_camp():
    # Encounter List Init
    DEFAULT_ENC = list()
    DEFAULT_ENC.append(1)

    foe_lists = list()
    foe_lists.append(list())
    foe_lists.append(list())
    foe_lists.append(list())

    foe_lists[0].append(copy.deepcopy(c_monsters["Needle Blight"]))
    foe_lists[0].append(copy.deepcopy(c_monsters["Needle Blight"]))
    foe_lists[0].append(copy.deepcopy(c_monsters["Twig Blight"]))
    foe_lists[0].append(copy.deepcopy(c_monsters["Twig Blight"]))
    foe_lists[0].append(copy.deepcopy(c_monsters["Twig Blight"]))
    foe_lists[1].append(copy.deepcopy(c_monsters["Basilisk"]))
    for num in range(5):
        foe_lists[2].append(copy.deepcopy(c_monsters["Aarakocra"]))

    # Non-combat Encounters
    DEFAULT_ENC.append(Encounter("[Zinnia] The Leaky Tap", bkgd="./assets/tavern.jpg"))
    DEFAULT_ENC.append(Encounter("[Zinnia] Al's Apothecary", bkgd="./assets/apothecary.jpg"))
    DEFAULT_ENC.append(Encounter("[Zinnia] The Bazaar", bkgd="./assets/bazaar.jpg"))

    DEFAULT_ENC.append(Encounter("[Adgard] Coral Inn", bkgd="./assets/coralinn.jpg"))
    DEFAULT_ENC.append(Encounter("[Adgard] Bard's Den", bkgd="./assets/tavern2.jpg"))
    DEFAULT_ENC.append(Encounter("[Adgard] Crownguard HQ", bkgd="./assets/guardhq.jpg"))

    # Combat Encounters
    DEFAULT_ENC.append(CEncounter("Verdant Wilds", anim=foe_lists[0], bkgd="./assets/verdantwilds.jpg"))
    DEFAULT_ENC.append(CEncounter("Jagged Pass", anim=foe_lists[1], bkgd="./assets/jaggedpass.jpg"))
    DEFAULT_ENC.append(CEncounter("Rivermouth", anim=foe_lists[2], bkgd="./assets/rivermouth.jpg"))

    return DEFAULT_ENC
