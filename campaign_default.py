
from encounter import Encounter
from cencounter import CEncounter
from monsters import c_monsters
from inanimate import Inanimate
from copy import deepcopy


def load_default_camp():
    # Encounter List Init
    DEFAULT_ENC = list()
    DEFAULT_ENC.append(1)

    foe_lists = list()
    prop_list = list()
    for i in range(3):
        foe_lists.append(list())
        prop_list.append(list())

    # Verdant Wilds: 0      Jagged Pass: 1      Rivermouth: 2
    foe_lists[0].append(deepcopy(c_monsters["Needle Blight"]))
    foe_lists[0].append(deepcopy(c_monsters["Needle Blight"]))
    foe_lists[0].append(deepcopy(c_monsters["Twig Blight"]))
    foe_lists[0].append(deepcopy(c_monsters["Twig Blight"]))
    foe_lists[0].append(deepcopy(c_monsters["Twig Blight"]))
    foe_lists[1].append(deepcopy(c_monsters["Basilisk"]))
    for num in range(5):
        foe_lists[2].append(deepcopy(c_monsters["Aarakocra"]))

    boulder = Inanimate("boulder", icon="./assets/boulder.png", item_code=0, details="A boulder to block paths")
    boulder.set_coors(2, 5)
    prop_list[0].append(deepcopy(boulder))
    boulder.set_coors(7, 4)
    prop_list[0].append(deepcopy(boulder))

    boulder.set_coors(5, 8)
    prop_list[1].append(deepcopy(boulder))
    boulder.set_coors(5, 7)
    prop_list[1].append(deepcopy(boulder))
    boulder.set_coors(6, 6)
    prop_list[1].append(deepcopy(boulder))
    boulder.set_coors(7, 5)
    prop_list[1].append(deepcopy(boulder))
    boulder.set_coors(8, 5)
    prop_list[1].append(deepcopy(boulder))

    for x_coors in range(15):
        boulder.set_coors(x_coors, 0)
        prop_list[2].append(deepcopy(boulder))

    boulder.set_coors(7, 10)
    prop_list[2].append(deepcopy(boulder))
    boulder.set_coors(7, 11)
    prop_list[2].append(deepcopy(boulder))
    boulder.set_coors(6, 11)
    prop_list[2].append(deepcopy(boulder))
    boulder.set_coors(7, 12)
    prop_list[2].append(deepcopy(boulder))

    # Non-combat Encounters
    DEFAULT_ENC.append(Encounter("[Zinnia] The Leaky Tap", bkgd="./assets/tavern.jpg"))
    DEFAULT_ENC.append(Encounter("[Zinnia] Al's Apothecary", bkgd="./assets/apothecary.jpg"))
    DEFAULT_ENC.append(Encounter("[Zinnia] The Bazaar", bkgd="./assets/bazaar.jpg"))

    DEFAULT_ENC.append(Encounter("[Adgard] Coral Inn", bkgd="./assets/coralinn.jpg"))
    DEFAULT_ENC.append(Encounter("[Adgard] Bard's Den", bkgd="./assets/tavern2.jpg"))
    DEFAULT_ENC.append(Encounter("[Adgard] Crownguard HQ", bkgd="./assets/guardhq.jpg"))

    # Combat Encounters
    DEFAULT_ENC.append(CEncounter("Verdant Wilds", bkgd="./assets/verdantwilds.jpg", anim=foe_lists[0], inanim=prop_list[0]))
    DEFAULT_ENC.append(CEncounter("Jagged Pass", bkgd="./assets/jaggedpass.jpg", anim=foe_lists[1], inanim=prop_list[1]))
    DEFAULT_ENC.append(CEncounter("Rivermouth", bkgd="./assets/rivermouth.jpg", anim=foe_lists[2], inanim=prop_list[2]))

    return DEFAULT_ENC
