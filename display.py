
from random import randint
import pygame
import pickle
from player import Player
from enemy import Enemy
from cencounter import CEncounter
from campaign_default import load_default_camp
from items import c_items
from copy import deepcopy

from os import environ
from os import startfile
import platform
import subprocess
import sys
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Screen Dimensions:
WIDTH = 800  # Use 16x16 sprites & tiles. Makes 50x30 grid.
HEIGHT = 450
ORIGIN = (0, 0)

# Map Dimensions:
MAP_MAX_X = 15
MAP_MAX_Y = 15

TILE_SIZE = int(HEIGHT / MAP_MAX_Y)      # Usually would be 32

# Base Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (241, 194, 50)
GREEN = (84, 230, 84)
RED = (255, 0, 0)

# Button Dimensions:
B_WIDTH = 200
B_HEIGHT = 50
B_CENTER = 300
B_YPOS = 330
Q_WD = 70
Q_HT = 50
Q_LF = WIDTH - Q_WD - 10
Q_TP = HEIGHT - Q_HT - 10

# Encounter & Player Data
EMPTY_LIST = list()
PLAYERS = list()
ENCOUNTERS = list()
ENC_INDEX = 1         # Can never be 0, since that's its own index
ASK_SAVE = False
RELOAD_ENC = False


# drawText from Pygame.org wiki
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


def use_font(size=12, font="hylia"):
    if font == "hylia":
        return pygame.font.Font('./fonts/HyliaSerif.otf', size)
    elif font == "scaly":
        return pygame.font.Font('./fonts/Scaly Sans.otf', size)
    elif font == "nodesto":
        return pygame.font.Font('./fonts/Nodesto Caps Condensed.otf', size)


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def load_image(path="./assets", x=1, y=1):
    IMAGE = pygame.image.load(path).convert_alpha()
    IMAGE = pygame.transform.scale(IMAGE, (x, y))
    return IMAGE


def load_pdf(path):
    if platform.system() == "Windows":
        startfile("C:/Users/elite/PycharmProjects/autocamp32/assets/PlayerHandbook.pdf")
    else:
        subprocess.call(["qpdfview", path])


def change_enc(index):
    global PLAYERS, ENCOUNTERS, ENC_INDEX, ASK_SAVE, RELOAD_ENC

    if index == ENC_INDEX:
        return

    PLAYERS = ENCOUNTERS[ENC_INDEX].save_players()

    ENC_INDEX = index
    ENCOUNTERS[ENC_INDEX].load_players(PLAYERS)
    ASK_SAVE = True

    if type(ENCOUNTERS[ENC_INDEX]) == CEncounter:
        RELOAD_ENC = True


def save():
    global PLAYERS, ENCOUNTERS, ENC_INDEX, ASK_SAVE, RELOAD_ENC
    ENCOUNTERS[0] = ENC_INDEX
    pickle.dump(EMPTY_LIST, open("players.camp", "wb"))
    pickle.dump(EMPTY_LIST, open("savegame.camp", "wb"))

    PLAYERS = ENCOUNTERS[ENC_INDEX].read_players()
    pickle.dump(PLAYERS, open("players.camp", "wb"))
    pickle.dump(ENCOUNTERS, open("savegame.camp", "wb"))
    ASK_SAVE = False
    RELOAD_ENC = False


class QuitBox:
    def __init__(self, parent, width, height, t_font, rect):
        box = load_image("./assets/button.png", width, height)

        text1, textbox1 = text_objects("Would you like to", t_font, WHITE)
        textbox1.center = rect.center
        textbox1.top = rect.top + 10

        text2, textbox2 = text_objects("save the game?", t_font, WHITE)
        textbox2.center = rect.center
        textbox2.top = textbox1.bottom

        parent.blit(box, rect)
        parent.blit(text1, textbox1)
        parent.blit(text2, textbox2)


class DiceBox:
    def __init__(self, parent, width, height, t_res, rect):
        self.backgd = load_image("./assets/button.png", width, height)
        self.parent = parent

        title, title_box = text_objects("Dice Tray", use_font(20, "hylia"), WHITE)
        title_box.center = rect.center
        title_box.top = rect.top

        self.results, self.res_rect = text_objects(t_res, use_font(20, "nodesto"), BLACK)
        self.result_field = pygame.Rect(rect.center[0]-100, title_box.bottom + 10, 200, 25)
        self.res_rect.center = self.result_field.center

        self.parent.blit(self.backgd, rect)
        self.parent.blit(title, title_box)
        pygame.draw.rect(self.parent, WHITE, self.result_field)
        self.parent.blit(self.results, self.res_rect)
        self.bottom = self.res_rect.bottom

    def update_result(self, result):
        self.results, self.res_rect = text_objects(result, use_font(20, "nodesto"), BLACK)
        self.res_rect.center = self.result_field.center
        pygame.draw.rect(self.parent, WHITE, self.result_field)
        self.parent.blit(self.results, self.res_rect)


class InvBox:
    def __init__(self, parent, width, height, rect, player_name="Player"):
        self.rect = rect
        self.bkgd = load_image("./assets/backpack.jpg", width, height)
        self.parent = parent

        title, title_box = text_objects("~ " + player_name + "'s Inventory ~", use_font(30, "hylia"), WHITE)
        title_box.center = self.rect.center
        title_box.top = self.rect.top + 10
        self.bottom = title_box.bottom

        self.parent.blit(self.bkgd, self.rect)
        self.parent.blit(title, title_box)


class PlayerBox:
    def __init__(self, parent, width, height, rect):
        self.rect = rect
        pygame.draw.rect(parent, BLACK, self.rect)
        self.parent = parent

        title, title_box = text_objects("Select Player", use_font(16, "hylia"), WHITE)
        title_box.center = self.rect.center
        title_box.top = self.rect.top
        self.bottom = title_box.bottom

        self.parent.blit(title, title_box)


class StatBox:
    def __init__(self, parent, width, height, rect, name, color=WHITE):
        self.backgd = load_image("./assets/backpack.jpg", width, height)
        self.parent = parent
        self.rect = rect

        title, title_box = text_objects(name + "'s Stats", use_font(24, "hylia"), color)
        title_box.center = self.rect.center
        title_box.top = self.rect.top

        self.parent.blit(self.backgd, self.rect)
        self.parent.blit(title, title_box)
        self.bottom = title_box.bottom


class NumberBox:
    def __init__(self, parent, width, height, t_res, rect, title):
        pygame.draw.rect(parent, BLACK, rect)
        self.parent = parent

        title, title_box = text_objects(title, use_font(20, "hylia"), WHITE)
        title_box.center = rect.center
        title_box.top = rect.top

        res_wid = int(0.75 * width)

        self.results, self.res_rect = text_objects(t_res, use_font(20, "nodesto"), BLACK)
        self.result_field = pygame.Rect(rect.center[0] - int(res_wid / 2), title_box.bottom + 10, res_wid, 25)
        self.res_rect.center = self.result_field.center

        self.parent.blit(title, title_box)
        pygame.draw.rect(self.parent, WHITE, self.result_field)
        self.parent.blit(self.results, self.res_rect)
        self.bottom = self.res_rect.bottom

    def update_result(self, result):
        self.results, self.res_rect = text_objects(result, use_font(20, "nodesto"), BLACK)
        self.res_rect.center = self.result_field.center
        pygame.draw.rect(self.parent, WHITE, self.result_field)
        self.parent.blit(self.results, self.res_rect)


class TextButton:
    def __init__(self, parent=None, path="./assets/button.png", text="test", t_size=20, t_color=WHITE, t_font="scaly",
                 left=0, top=0, width=B_WIDTH, height=B_HEIGHT, just="mid"):

        self.textstr = text
        self.parent = parent
        self.just = just
        self.t_size, self.t_color = t_size, t_color
        self.t_font = use_font(size=t_size, font=t_font)

        self.box = load_image(path, width, height)

        self.rect = pygame.Rect(left, top, width, height)

        self.text, self.textbox = text_objects(self.textstr, self.t_font, t_color)
        self.textbox.center = self.rect.center
        if self.just == "left":
            self.textbox.left = self.rect.left + 10
        elif self.just == "right":
            self.textbox.right = self.rect.right - 10

        parent.blit(self.box, self.rect)
        parent.blit(self.text, self.textbox)


class TextBox:
    def __init__(self, parent=None, center=False, text="test", t_size=20, t_color=WHITE, t_font="scaly",
                 left=0, top=0, rect=None, bind_2_rect=False):

        self.t_size, self.t_color = t_size, t_color
        self.t_font = use_font(size=t_size, font=t_font)
        if not rect:
            self.rect = pygame.Rect(left, top, WIDTH - (2 * left), t_size)
        else:
            self.rect = rect

        self.text, self.textbox = text_objects(text, self.t_font, t_color)
        if bind_2_rect:
            self.textbox = self.rect
        elif center:
            self.textbox.center = self.rect.center
            if rect is None:
                self.textbox.top = top
            elif top != 0:
                self.textbox.top -= top
        else:
            self.textbox.left = left
            self.textbox.top = top

        parent.blit(self.text, self.textbox)
        self.right = self.textbox.right
        self.bottom = self.textbox.bottom


class CheckBox:
    def __init__(self, parent=None, rect=None, center=False, coors=(None, None), state=False):
        self.parent = parent
        self.urect = rect

        if center and coors != (None, None):
            self.urect.center = coors
        elif coors != (None, None):
            self.urect.left = coors[0]
            self.urect.top = coors[1]

        self.crect = pygame.Rect(0, 0, int(0.8 * self.urect.width), int(0.8 * self.urect.height))
        self.crect.center = self.urect.center
        self.is_checked = state
        if self.is_checked:
            self.check()
        else:
            self.uncheck()

    def check(self):
        self.is_checked = True
        pygame.draw.rect(self.parent, BLACK, self.crect)

    def uncheck(self):
        self.is_checked = False
        pygame.draw.rect(self.parent, WHITE, self.urect)


class Display:
    pygame.init()

    # Window Creation
    # ==================================
    ICON = pygame.image.load('./assets/autocamp_icon.png')
    pygame.display.set_icon(ICON)
    pygame.display.set_caption('AutoCamp')
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Class Variables
    # ==================================
    BG_STARTUP = load_image("./assets/bg_start_screen.jpg", WIDTH, HEIGHT)
    BG_TAVERN = load_image("./assets/tavern.jpg", WIDTH, HEIGHT)
    CLICK = False
    CLK = pygame.time.Clock()
    PLAYERS_OK = False
    ENCOUNTERS_OK = False
    TO_MAIN_MENU = False
    TO_TRAVEL = False

    global PLAYERS, ENCOUNTERS, ENC_INDEX, EMPTY_LIST

    # Load Data
    # ==================================
    try:
        # global PLAYERS, ENCOUNTERS, ENC_INDEX
        PLAYERS = pickle.load(open("players.camp", "rb"))
        PLAYERS_OK = True
        ENCOUNTERS = pickle.load(open("savegame.camp", "rb"))
        ENCOUNTERS_OK = True
    except:
        if not PLAYERS_OK:
            PLAYERS.append(Player(name="Kru'ul Kanath", race="Orc", role="Warlock"))
            PLAYERS.append(Player(name="Kepesk", race="Tiefling", role="Cleric"))
            PLAYERS.append(Player(name="Naybur Sturmgeist", race="Human", role="Wizard"))
            PLAYERS.append(Player(name="Alduin Rambert", race="Aasimar", role="Barbarian"))
            PLAYERS.append(Player(name="Vana Moore", race="Goblin", role="Rogue"))

            for hero in PLAYERS:
                hero.set_stats("Strength", randint(6, 18))
                hero.set_stats("Dexterity", randint(6, 18))
                hero.set_stats("Constitution", randint(6, 18))
                hero.set_stats("Intellect", randint(6, 18))
                hero.set_stats("Wisdom", randint(6, 18))
                hero.set_stats("Charisma", randint(6, 18))

                hero.set_weapon("Shortsword")
                hero.set_armor("Chain Mail")
                hero.inv_add("Mana Potion", randint(1, 6))
                hero.inv_add("Bread (Loaf)", randint(1, 4))
                hero.inv_add("Spyglass", 1)
                hero.inv_add("Fishing Tackle", 2)
                hero.inv_add("Clothes (Common)", randint(3, 8))
                hero.inv_add("Handaxe", randint(1, 2))
                hero.inv_add("Net", randint(1, 2))
                hero.inv_add("Leather Armor", 1)

            pickle.dump(EMPTY_LIST, open("players.camp", "wb"))
            pickle.dump(PLAYERS, open("players.camp", "wb"))
            ENCOUNTERS_OK = False

        if not ENCOUNTERS_OK:
            ENCOUNTERS = load_default_camp()
            pickle.dump(EMPTY_LIST, open("savegame.camp", "wb"))
            pickle.dump(ENCOUNTERS, open("savegame.camp", "wb"))

    ENC_INDEX = ENCOUNTERS[0]
    change_enc(ENC_INDEX)

    # Pages and Menus
    # ==================================
    def page_startup(self):
        st_font = "hylia"

        while True:
            global ENCOUNTERS
            # Graphics Generation
            # ==================================
            self.SCREEN.blit(self.BG_STARTUP, ORIGIN)
            temp = int((B_WIDTH - 5) / 2)
            b_start = TextButton(parent=self.SCREEN, text="Start", t_font=st_font, left=B_CENTER,
                                 top=B_YPOS - (2 * B_HEIGHT) - 5, width=B_WIDTH, height=B_HEIGHT)
            b_credits = TextButton(parent=self.SCREEN, text="Credits", t_font=st_font, left=b_start.rect.left,
                                   top=B_YPOS - B_HEIGHT, width=temp, height=B_HEIGHT)
            b_handbook = TextButton(parent=self.SCREEN, text="PHB", t_font=st_font, left=b_start.rect.right - temp,
                                    top=B_YPOS - B_HEIGHT, width=temp, height=B_HEIGHT)
            b_quit = TextButton(parent=self.SCREEN, text="Exit", t_font=st_font, left=b_start.rect.left,
                                top=B_YPOS + 5, width=B_WIDTH, height=B_HEIGHT)

            # TODO: Integrate Character Creation Loop

            # Button Functions
            # ==================================
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                self.CLICK = False
                if b_start.rect.collidepoint(mouse):
                    # ENCOUNTERS = pickle.load(open("savegame.camp", "rb"))
                    # ENC_INDEX = ENCOUNTERS[0]
                    ENCOUNTERS[ENC_INDEX].load_players(PLAYERS)
                    while True:
                        if self.TO_MAIN_MENU:
                            self.TO_MAIN_MENU = False
                            break
                        if self.TO_TRAVEL:
                            self.travel_prompt()
                        elif type(ENCOUNTERS[ENC_INDEX]) == CEncounter:
                            self.page_map()
                        else:
                            self.page_nce()
                elif b_quit.rect.collidepoint(mouse):
                    sys.exit()
                elif b_credits.rect.collidepoint(mouse):
                    self.page_credits()
                elif b_handbook.rect.collidepoint(mouse):
                    load_pdf("/home/pi/PycharmProjects/autocamp32/assets/PlayerHandbook.pdf")

            self.end_page()

    def page_map(self):
        global RELOAD_ENC, ASK_SAVE
        map_reload = True
        move_reload = False
        move_select = False
        leave_message = "Travel"
        ds_text = "Death Save"
        map_pixels = (TILE_SIZE * MAP_MAX_X, TILE_SIZE * MAP_MAX_Y)
        action_text = ""
        move_text = ""
        show_message = ""

        # prepare move_tile list ahead of time
        move_tiles = list()
        for x in range(MAP_MAX_X):
            move_tiles.append(list())
            for y in range(MAP_MAX_Y):
                move_tiles[x].append(None)

        # entity selection variables
        turn_index = ENCOUNTERS[ENC_INDEX].get_turn()
        ent_index = turn_index
        ent_select = None
        ent_target = None
        ent_coors = [-1, -1]

        action_used = False
        rem_speed = ENCOUNTERS[ENC_INDEX].get_entity(turn_index).get_stat("Speed")
        x_start, x_end, y_start, y_end = 0, 0, 0, 0

        map_tile = list()
        background = load_image(ENCOUNTERS[ENC_INDEX].get_bkgd(), map_pixels[0], map_pixels[1])

        if RELOAD_ENC:
            RELOAD_ENC = False
            ENCOUNTERS[ENC_INDEX].start_encounter()

            y_mid = int(MAP_MAX_Y / 2)
            player_pos = list()
            radius = 2
            x_start = 0
            y_start = y_mid - radius
            x_end = radius
            y_end = y_mid + radius

            for y_coor in range(y_start, y_end + 1):
                for x_coor in range(x_start, x_end + 1):
                    player_pos.append((x_coor, y_coor))

            for ent in ENCOUNTERS[ENC_INDEX].get_anim():
                if type(ent) == Enemy:
                    left_lim = int(MAP_MAX_X / 2)
                    right_lim = MAP_MAX_X - 1
                    upper_lim = 0
                    lower_lim = MAP_MAX_Y - 1
                    coors = (MAP_MAX_X - 1, y_mid)
                    z_val = ent.get_coors()[2]
                    ent.set_coors(coors[0], coors[1], z_val)
                    while True:
                        if ENCOUNTERS[ENC_INDEX].enc_move(coors[0], coors[1], z_val,
                                                          int(max(MAP_MAX_X, MAP_MAX_Y) * 5),
                                                          randint(left_lim, right_lim),
                                                          randint(upper_lim, lower_lim))[0]:
                            break

                if type(ent) == Player:
                    coors = ent.get_coors()
                    while True:
                        index = randint(0, len(player_pos) - 1)
                        cell = player_pos[index]

                        if ENCOUNTERS[ENC_INDEX].enc_move(coors[0], coors[1], coors[2], 30, cell[0], cell[1])[0]:
                            del player_pos[index]
                            break
        else:
            ENCOUNTERS[ENC_INDEX].start_encounter(reset_init=False)

        while True:
            if ENCOUNTERS[ENC_INDEX].no_enemies():
                if leave_message == "Flee":
                    map_reload = True
                leave_message = "Travel"
            else:
                if leave_message == "Travel":
                    map_reload = True
                leave_message = "Flee"

            if ASK_SAVE:
                save_text = "Save"
            else:
                save_text = "Saved!"

            # Map Reloading
            # ==================================
            if map_reload:
                map_reload = False
                self.SCREEN.blit(load_image("./assets/travel_bg.jpg", WIDTH, HEIGHT), ORIGIN)
                self.SCREEN.blit(background, ORIGIN)
                menu_rect = pygame.Rect(map_pixels[0], 0, WIDTH - map_pixels[0], HEIGHT)
                if action_used:
                    action_text = "Action Used"
                if rem_speed == 0:
                    move_text = "Move Used"

                map_tile = list()
                for x_coor in range(MAP_MAX_X):
                    map_tile.append(list())
                    for y_coor in range(MAP_MAX_Y):
                        button = pygame.Rect(x_coor * TILE_SIZE, y_coor * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                        map_tile[x_coor].append(button)

                ent_select = ENCOUNTERS[ENC_INDEX].get_entity(ent_index)
                if ent_select is not None:
                    ent_coors = [ent_select.get_coors()[0], ent_select.get_coors()[1]]
                    if "Unconscious" in ent_select.get_conditions():
                        if "has perished" in show_message:
                            ENCOUNTERS[ENC_INDEX].get_anim().remove(ent_select)
                            ent_select = ENCOUNTERS[ENC_INDEX].get_entity(ent_index)
                            ent_coors = [ent_select.get_coors()[0], ent_select.get_coors()[1]]
                            action_used = False
                            rem_speed = ENCOUNTERS[ENC_INDEX].get_entity(turn_index).get_stat("Speed")
                        else:
                            # action_used = True
                            rem_speed = 0
                            if not action_used:
                                action_text = ds_text
                            move_text = "Cannot Move"
                else:
                    ent_coors = [-1, -1]

                # Control Buttons
                # ==================================
                BT_WID = 73
                b_quitgame = TextButton(parent=self.SCREEN, text="Quit", left=WIDTH - BT_WID - 10, top=10,
                                        width=BT_WID, height=Q_HT)
                b_travel = TextButton(parent=self.SCREEN, text=leave_message, left=b_quitgame.rect.left - BT_WID - 10,
                                      top=b_quitgame.rect.top, width=BT_WID, height=Q_HT)
                b_save = TextButton(parent=self.SCREEN, text=save_text, left=b_travel.rect.left - BT_WID - 10,
                                    top=b_quitgame.rect.top, width=BT_WID, height=Q_HT)
                b_handbook = TextButton(parent=self.SCREEN, text="PHB", left=b_save.rect.left - BT_WID - 10,
                                        top=b_quitgame.rect.top, width=BT_WID, height=Q_HT)

                # ==================================
                turn_title = "- " + ENCOUNTERS[ENC_INDEX].get_entity(turn_index).get_name() + "'s Turn -"
                TextBox(parent=self.SCREEN, text=turn_title, t_size=26, t_color=BLACK, t_font="hylia",
                        center=True, rect=menu_rect, top=135)
                text_hp = "HP: " + str(ENCOUNTERS[ENC_INDEX].get_entity(turn_index).get_stat("Current HP")) \
                          + " / " + str(ENCOUNTERS[ENC_INDEX].get_entity(turn_index).get_stat("Max HP"))

                TextBox(parent=self.SCREEN, text=text_hp, t_size=20, t_color=BLACK, t_font="hylia",
                        center=True, rect=menu_rect, top=110)

                message_rect = deepcopy(menu_rect)
                message_rect.top = menu_rect.centery - 60
                message_rect.left = menu_rect.left + 20
                message_rect.height = 50
                message_rect.width = menu_rect.width - 20

                try:
                    str_1, str_2 = show_message.split("|")

                    drawText(self.SCREEN, str_1, BLACK, message_rect, use_font(20, "scaly"))

                    message_rect.top = menu_rect.centery - 20
                    drawText(self.SCREEN, str_2, BLACK, message_rect, use_font(20, "scaly"))
                except:
                    drawText(self.SCREEN, show_message, BLACK, message_rect, use_font(20, "scaly"))


                # ==================================
                AB_WID = int((menu_rect.width - 35) / 2)
                right = b_quitgame.rect.right - AB_WID
                b_endturn = TextButton(parent=self.SCREEN, text=">> End Turn >>", left=right,
                                       top=HEIGHT - Q_HT - 10, width=AB_WID, height=Q_HT)

                b_stats = TextButton(parent=self.SCREEN, text="View Stats", left=b_endturn.rect.left - AB_WID - 10,
                                     top=b_endturn.rect.top, width=AB_WID, height=Q_HT)

                b_dice = TextButton(parent=self.SCREEN, text="Roll Dice", left=b_endturn.rect.left,
                                    top=b_endturn.rect.top - Q_HT - 10, width=AB_WID, height=Q_HT)

                b_inv, b_move = None, None
                if turn_index == ent_index:
                    if rem_speed > 0:
                        move_text = "Move"
                    b_move = TextButton(parent=self.SCREEN, text=move_text, left=b_stats.rect.left,
                                        top=b_dice.rect.top, width=AB_WID, height=Q_HT)

                    if type(ENCOUNTERS[ENC_INDEX].get_entity(turn_index)) is Player:
                        b_inv = TextButton(parent=self.SCREEN, text="Inventory", left=b_endturn.rect.left,
                                           top=b_dice.rect.top - Q_HT - 10, width=AB_WID, height=Q_HT)

                else:
                    ent_name = ENCOUNTERS[ENC_INDEX].get_entity(ent_index)
                    if ent_name is not None:
                        ent_name = ent_name.get_name()
                        turn_title = "- Selected: " + ent_name + " -"
                        TextBox(parent=self.SCREEN, text=turn_title, t_size=16, t_color=BLACK, t_font="hylia",
                                center=True, rect=menu_rect, top=80)

                b_attack = None
                target_found, ent_target = ENCOUNTERS[ENC_INDEX].enemyInRange()[0], ENCOUNTERS[ENC_INDEX].enemyInRange()[1]

                if target_found and turn_index == ent_index:
                    if not action_used and action_text != ds_text:
                        action_text = "Attack"
                        t_color = RED
                    elif not action_used and action_text == ds_text:
                        t_color = GOLD
                    else:
                        t_color = WHITE

                    b_attack = TextButton(parent=self.SCREEN, text=action_text, left=b_stats.rect.left, t_color=t_color,
                                          top=b_dice.rect.top - Q_HT - 10, width=AB_WID, height=Q_HT)
                    ent_target = ENCOUNTERS[ENC_INDEX].get_entity(ent_target)

                # Blit out Entities:
                # ==================================
                entity_list = ENCOUNTERS[ENC_INDEX].get_inanim() + ENCOUNTERS[ENC_INDEX].get_anim()

                for index, ent in enumerate(entity_list):
                    coors = [ent.get_coors()[0], ent.get_coors()[1]]
                    tile_rect = pygame.Rect(TILE_SIZE * coors[0], TILE_SIZE * coors[1], TILE_SIZE, TILE_SIZE)
                    # if index == turn_index and type(ent) is not Inanimate:
                    #     self.SCREEN.blit(load_image("./assets/b_credits.png", TILE_SIZE, TILE_SIZE), tile_rect)
                    if coors == ent_coors:
                        self.SCREEN.blit(load_image("./assets/button.png", TILE_SIZE, TILE_SIZE), tile_rect)
                    self.SCREEN.blit(load_image(ent.get_icon(), TILE_SIZE, TILE_SIZE), tile_rect)

            # Move Reloading
            # ==================================
            if move_reload:
                move_reload = False
                for x in range(x_start, x_end):
                    for y in range(y_start, y_end):
                        if move_tiles[x][y] is not None:
                            self.SCREEN.blit(load_image("./assets/movetile.png", TILE_SIZE, TILE_SIZE),
                                             (x * TILE_SIZE, y * TILE_SIZE))
                move_select = True

            # Mouse Events
            # ==================================
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                self.CLICK = False
                map_reload = True
                show_message = ""

                if move_select:
                    move_select = False

                    flag = False
                    for x in range(x_start, x_end):
                        if flag:
                            break
                        for y in range(y_start, y_end):
                            if move_tiles[x][y] is not None and move_tiles[x][y].collidepoint(mouse):
                                moved = ENCOUNTERS[ENC_INDEX].enc_move(ent_coors[0], ent_coors[1], 0,
                                                                       rem_speed, x, y)
                                if moved[0]:
                                    rem_speed -= moved[1]
                                flag = True
                                break
                    map_reload = True
                    ent_select = None
                    ent_coors = [-1, -1]
                    ASK_SAVE = True

                elif b_quitgame.rect.collidepoint(mouse):
                    if self.prompt_quit():
                        return

                elif b_save.rect.collidepoint(mouse):
                    save()

                elif b_travel.rect.collidepoint(mouse):

                    # TODO: Add some kind of encounter reset
                    self.travel_prompt()
                    return

                elif b_handbook.rect.collidepoint(mouse):
                    load_pdf("/home/pi/PycharmProjects/autocamp32/assets/PlayerHandbook.pdf")

                elif b_endturn.rect.collidepoint(mouse):
                    ENCOUNTERS[ENC_INDEX].next_turn()
                    turn_index = ENCOUNTERS[ENC_INDEX].get_turn()
                    ent_index = turn_index
                    rem_speed = ENCOUNTERS[ENC_INDEX].get_entity(turn_index).get_stat("Speed")
                    ASK_SAVE = True
                    action_used = False

                elif b_inv is not None and b_inv.rect.collidepoint(mouse):
                    pl_index = None  # TODO: Figure out better fix for inv-startup bug.
                    for index, ent in enumerate(ENCOUNTERS[ENC_INDEX].get_anim()):
                        if type(ent) == Player and ent.get_name() == ENCOUNTERS[ENC_INDEX].get_entity(turn_index).get_name():
                            pl_index = index
                    if pl_index is not None:
                        self.inv_prompt(ent_select, 120, pl_index)

                elif b_attack is not None and b_attack.rect.collidepoint(mouse) and not action_used:
                    if action_text != ds_text:
                        attacker = ENCOUNTERS[ENC_INDEX].get_entity(turn_index)
                        damage = ENCOUNTERS[ENC_INDEX].attack(ent_target, False, False)
                        if damage is not None:
                            show_message = attacker.get_name() + " attacked " + ent_target.get_name() + ", dealing " \
                                           + str(damage) + " damage! | " + ent_target.get_name() + " HP: " \
                                           + str(ent_target.get_stat("Current HP")) + " / " \
                                           + str(ent_target.get_stat("Max HP"))
                        else:
                            show_message = attacker.get_name() + " attacked " + ent_target.get_name() + ", but failed! | "
                        action_used = True
                        ASK_SAVE = True

                    else:
                        result = ENCOUNTERS[ENC_INDEX].rollDice(1, 20)
                        show_message = "Rolled: " + str(result) + "... "
                        if result >= 10:
                            if result == 20:
                                show_message += ent_select.death_evade(True)
                            else:
                                show_message += ent_select.death_evade(False)
                        elif result < 10:
                            if result == 1:
                                show_message += ent_select.death_strike(True, True)
                            else:
                                show_message += ent_select.death_strike(False)

                        ASK_SAVE = True
                        action_used = True

                elif b_stats.rect.collidepoint(mouse):
                    self.stat_prompt(ent_select)

                elif b_dice.rect.collidepoint(mouse):
                    self.dice_prompt(ent_select)

                elif b_move is not None and b_move.rect.collidepoint(mouse) and ent_select is not None\
                        and rem_speed > 0:
                    x_start = max(0, ent_coors[0] - int(rem_speed / 5))
                    x_end = min(MAP_MAX_X, ent_coors[0] + int(rem_speed / 5))
                    y_start = max(0, ent_coors[1] - int(rem_speed / 5))
                    y_end = min(MAP_MAX_Y, ent_coors[1] + int(rem_speed / 5))

                    # empty out grid
                    for x, i in enumerate(move_tiles):
                        for y, j in enumerate(move_tiles[x]):
                            move_tiles[x][y] = None

                    for x_coor in range(x_start, x_end):
                        for y_coor in range(y_start, y_end):
                            if ENCOUNTERS[ENC_INDEX].entity_at(x_coor, y_coor) is None:
                                move_tiles[x_coor][y_coor] = map_tile[x_coor][y_coor]
                                move_reload = True

                # TODO: Integrate hint system.

                else:
                    flag = False
                    for x_coor in range(MAP_MAX_X):
                        if flag:
                            break
                        for y_coor in range(MAP_MAX_Y):
                            if map_tile[x_coor][y_coor].collidepoint(mouse):
                                ent_index = ENCOUNTERS[ENC_INDEX].entity_at(x_coor, y_coor)
                                ent_coors = [x_coor, y_coor]
                                ent_select = ENCOUNTERS[ENC_INDEX].get_entity(ent_index)
                                map_reload = True
                                flag = True
                                break

            self.end_page()

    def page_nce(self):
        global ASK_SAVE
        menu_top = 390
        menu_left = 670
        cwid = 100
        offs = cwid + 10
        background = load_image(ENCOUNTERS[ENC_INDEX].get_bg(), WIDTH, HEIGHT)
        player_index = 0
        current_player = PLAYERS[0]

        while True:
            if ASK_SAVE:
                save_text = "Save"
            else:
                save_text = "Saved!"

            self.SCREEN.blit(background, ORIGIN)

            # TODO: Integrate Resting here.

            TextButton(parent=self.SCREEN, text=ENCOUNTERS[ENC_INDEX].get_name(), t_size=24, t_font="hylia",
                       left=int(WIDTH / 2) - 150, top=10, width=300, height=50)
            b_quitgame = TextButton(parent=self.SCREEN, text="Quit", left=Q_LF, top=10, width=Q_WD, height=Q_HT)
            b_save = TextButton(parent=self.SCREEN, text=save_text, left=Q_LF - Q_WD - 10, top=10, width=Q_WD, height=Q_HT)
            b_handbook = TextButton(parent=self.SCREEN, text="PHB", left=b_save.rect.left - Q_WD - 10, top=10, width=Q_WD, height=Q_HT)
            b_travel = TextButton(parent=self.SCREEN, text="Travel", left=menu_left, top=menu_top, width=cwid)
            b_roll = TextButton(parent=self.SCREEN, text="Roll", left=menu_left - offs, top=menu_top, width=cwid)
            b_inv = TextButton(parent=self.SCREEN, text="Inventory", left=menu_left-(2*offs), top=menu_top, width=cwid)
            b_stats = TextButton(parent=self.SCREEN, text="Stats", left=menu_left-(3*offs), top=menu_top, width=cwid)
            b_party = TextButton(parent=self.SCREEN, text="Party", left=menu_left-(4*offs), top=menu_top, width=cwid)

            # ==================================
            # Player Buttons
            # ==================================
            p_top = 10
            exp_buttons = list()
            for index, player in enumerate(PLAYERS):
                if index == player_index:
                    exp_buttons.append(
                        TextButton(parent=self.SCREEN, text=player.get_name(), t_size=20, t_font="nodesto",
                                   left=10, top=p_top, width=cwid, t_color=GOLD))
                    current_player = PLAYERS[index]
                else:
                    exp_buttons.append(
                        TextButton(parent=self.SCREEN, text=player.get_name(), t_size=16, t_font="nodesto",
                                   left=10, top=p_top, width=cwid))
                p_top += B_HEIGHT + 10

            # ==================================
            # Mouse Monitor
            # ==================================
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                if b_quitgame.rect.collidepoint(mouse):
                    if self.prompt_quit():
                        return False

                elif b_save.rect.collidepoint(mouse):
                    save()

                elif b_travel.rect.collidepoint(mouse):
                    self.TO_TRAVEL = True
                    return

                elif b_roll.rect.collidepoint(mouse):
                    self.dice_prompt(current_player)

                elif b_handbook.rect.collidepoint(mouse):
                    load_pdf("/home/pi/PycharmProjects/autocamp32/assets/PlayerHandbook.pdf")

                elif b_inv.rect.collidepoint(mouse):
                    self.inv_prompt(current_player, cwid, player_index)

                elif b_stats.rect.collidepoint(mouse):
                    self.stat_prompt(current_player)

                elif b_party.rect.collidepoint(mouse):
                    pass

                else:
                    for index, button in enumerate(exp_buttons):
                        if button.rect.collidepoint(mouse):
                            player_index = index

            self.end_page()

    def page_credits(self):
        while True:
            self.SCREEN.fill(BLACK)

            tb_title = TextBox(parent=self.SCREEN, text="AutoCamp Team", t_font="hylia", t_size=30,
                               top=30, center=True, t_color=GOLD)
            tb_member1 = TextBox(parent=self.SCREEN, text="Nader Atout", t_font="hylia", t_size=20, center=True,
                                 top=tb_title.textbox.top + tb_title.textbox.height)
            tb_member2 = TextBox(parent=self.SCREEN, text="Diana Penalba", t_font="hylia", t_size=20, center=True,
                                 top=tb_member1.textbox.top + tb_member1.textbox.height)
            tb_member3 = TextBox(parent=self.SCREEN, text="Adrian Gavrila", t_font="hylia", t_size=20, center=True,
                                 top=tb_member2.textbox.top + tb_member2.textbox.height)

            tb_advisor = TextBox(parent=self.SCREEN, text="Team Advisor", t_font="hylia", t_size=30, center=True,
                                 top=tb_member3.textbox.top + tb_member3.textbox.height + 20, t_color=GREEN)
            tb_advname = TextBox(parent=self.SCREEN, text="Asst. Prof. Salma Elmalaki", t_font="hylia", t_size=20,
                                 center=True, top=tb_advisor.textbox.top + tb_advisor.textbox.height)

            tb_game = TextBox(parent=self.SCREEN, text="Original Tabletop Game", t_font="hylia", t_size=30,
                              center=True, top=tb_advname.textbox.top + tb_advname.textbox.height + 20, t_color=RED)
            tb_wizards = TextBox(parent=self.SCREEN, text="Wizards of the Coast", t_font="hylia", t_size=20,
                                 center=True, top=tb_game.textbox.top + tb_game.textbox.height)

            tb_images = TextBox(parent=self.SCREEN, text="All artwork and sprites found through Google Images and Game-Icons.net", t_font="hylia",
                                t_size=20, center=True, top=tb_wizards.textbox.top + tb_wizards.textbox.height + 20)

            b_back = TextButton(parent=self.SCREEN, path="./assets/b_credits.png", text="Back", left=B_CENTER,
                                top=B_YPOS + 60, width=B_WIDTH, height=B_HEIGHT)

            if b_back.rect.collidepoint(pygame.mouse.get_pos()) and self.CLICK:
                return

            self.end_page()

    def inv_prompt(self, player, bwid, player_index):
        global ASK_SAVE
        width, height = WIDTH - bwid - 20, HEIGHT
        rect = pygame.Rect(WIDTH - width, 0, width, height)

        # Item list Parameters
        # ==================================
        item_width, item_height = 330, 35
        start_index, list_len = 0, 6
        item_buttons = list()
        item_sel_index = -3
        items_left = WIDTH - 20 - item_width
        reload = True
        sel_button = 0
        EQP, DQP, USE = 1, 2, 3
        font_size = 20

        while True:
            if reload:
                # Critical to ensure that it blits at the right time.
                reload = False

                # Other Parameters
                # ==================================
                inv_box = InvBox(self.SCREEN, width, height, rect, player_name=player.get_name())
                b_close = TextButton(parent=self.SCREEN, text="X", t_font="hylia", t_size=24, left=rect.right - 30,
                                     top=rect.top, width=30, height=30)

                # Equipped Items Buttons
                # ==================================
                eq_width, eq_top = int(item_width / 2) - 5, inv_box.bottom + 10
                arm_left = WIDTH - 20 - eq_width

                if item_sel_index == -1:
                    b_weapon = TextButton(parent=self.SCREEN, text=player.get_weapon(), t_font="nodesto", t_size=font_size,
                                          left=items_left, top=eq_top, width=eq_width, height=item_height, t_color=GOLD)
                else:
                    b_weapon = TextButton(parent=self.SCREEN, text=player.get_weapon(), t_font="nodesto", t_size=font_size,
                                          left=items_left, top=eq_top, width=eq_width, height=item_height)

                if item_sel_index == -2:
                    b_armor = TextButton(parent=self.SCREEN, text=player.get_armor(), t_font="nodesto", t_size=font_size,
                                         left=arm_left, top=eq_top, width=eq_width, height=item_height, t_color=GOLD)
                else:
                    b_armor = TextButton(parent=self.SCREEN, text=player.get_armor(), t_font="nodesto", t_size=font_size,
                                         left=arm_left, top=eq_top, width=eq_width, height=item_height)

                t_weapon, wep_box = text_objects("Equipped Weapon", use_font(13), WHITE)
                wep_box.center = b_weapon.rect.center
                wep_box.top = b_weapon.rect.bottom

                t_armor, arm_box = text_objects("Equipped Armor", use_font(13), WHITE)
                arm_box.center = b_armor.rect.center
                arm_box.top = b_armor.rect.bottom

                self.SCREEN.blit(t_weapon, wep_box)
                self.SCREEN.blit(t_armor, arm_box)

                # Item List Buttons
                # ==================================
                b_scrollup = TextButton(parent=self.SCREEN, text='<< Prev <<', t_font="hylia", t_size=16,
                                        left=items_left, top=wep_box.bottom + 5, width=item_width, height=item_height)

                items_bottom = b_scrollup.rect.bottom + (list_len * item_height)
                b_scrolldown = TextButton(parent=self.SCREEN, text='>> Next >>', t_font="hylia", t_size=16, left=items_left,
                                          top=items_bottom, width=item_width, height=item_height)

                # Determine items to show
                # ==================================
                items_to_show = list()
                inventory = list(player.inventory)
                end_index = start_index + list_len
                if end_index >= len(player.inventory):
                    end_index = len(player.inventory)
                for index in range(start_index, end_index):
                    items_to_show.append(inventory[index])

                # Display Items
                # ==================================
                item_top = b_scrollup.rect.bottom
                item_buttons = list()

                for index, item in enumerate(items_to_show):
                    if index == item_sel_index and item_sel_index >= 0:
                        item_buttons.append(
                            TextButton(parent=self.SCREEN, text=item, t_size=font_size, t_font="nodesto", left=items_left,
                                       top=item_top, width=item_width, height=item_height, just="left",
                                       t_color=GOLD))
                        a_text, a_box = text_objects("x" + str(player.inventory[item]), use_font(font_size, "nodesto"), GOLD)
                    else:
                        item_buttons.append(
                            TextButton(parent=self.SCREEN, text=item, t_size=font_size, t_font="nodesto", left=items_left,
                                       top=item_top, width=item_width, height=item_height, just="left"))
                        a_text, a_box = text_objects("x" + str(player.inventory[item]), use_font(font_size, "nodesto"), WHITE)

                    # Math stage
                    a_box.center = item_buttons[index].rect.center
                    a_box.right = item_buttons[index].rect.right - 10
                    self.SCREEN.blit(a_text, a_box)
                    item_top += item_height

                # Action Buttons
                # ==================================
                awid, aheight = 100, 40
                if item_sel_index >= -2:
                    b_discard = TextButton(parent=self.SCREEN, text="Discard", t_font="nodesto", t_size=20,
                                           left=WIDTH - awid - 20, top=HEIGHT - aheight - 10, width=awid, height=aheight)

                    b_give = TextButton(parent=self.SCREEN, text="Give", t_font="nodesto", t_size=20,
                                        left=b_scrollup.rect.center[0] - int(awid / 2),
                                        top=HEIGHT - aheight - 10, width=awid, height=aheight)

                    if sel_button == EQP:
                        b_equip = TextButton(parent=self.SCREEN, text="Equip", t_font="nodesto", t_size=20,
                                             left=items_left, top=HEIGHT - aheight - 10, width=awid, height=aheight)
                    if sel_button == DQP:
                        b_dequip = TextButton(parent=self.SCREEN, text="Dequip", t_font="nodesto", t_size=20,
                                              left=items_left, top=HEIGHT - aheight - 10, width=awid, height=aheight)
                    if sel_button == USE:
                        b_use = TextButton(parent=self.SCREEN, text="Use", t_font="nodesto", t_size=20,
                                           left=items_left, top=HEIGHT - aheight - 10, width=awid, height=aheight)

                # Description Box
                # ==================================
                if 0 <= item_sel_index < list_len:
                    description = c_items[items_to_show[item_sel_index]].get_details()
                elif item_sel_index == -1 and player.get_weapon():
                    description = c_items[player.get_weapon()].get_details()
                elif item_sel_index == -2 and player.get_armor():
                    description = c_items[player.get_armor()].get_details()
                else:
                    description = ""

                desc_left = WIDTH - width + 20

                desc_width = items_left - desc_left - 10
                desc_height = HEIGHT - b_scrollup.rect.top - 10

                desc_rect = pygame.Rect(desc_left, b_scrollup.rect.top, desc_width, desc_height)
                self.SCREEN.blit(load_image("./assets/button.png", desc_width, desc_height), desc_rect)
                tb_desc = TextBox(parent=self.SCREEN, text="Description", t_size=13, t_font="hylia",
                                  left=desc_left + 10, top=b_scrollup.rect.top + 1)

                desc_rect = pygame.Rect(desc_left + 10, tb_desc.rect.bottom + 25, desc_width - 15, desc_height - 20)
                drawText(self.SCREEN, description, WHITE, desc_rect, use_font(17, "scaly"))

                # Money Box
                # ==================================
                wallet = player.get_money()
                money = ("{:3} GP           {:2} SP          {:2} CP").format(
                    wallet["gold"], wallet["silver"], wallet["copper"])

                money_box = TextButton(parent=self.SCREEN, text=money, t_font="hylia", t_size=16, left=desc_left,
                                       top=b_weapon.rect.top, width=desc_width, height=item_height)

            # ==================================
            # Mouse Events
            # ==================================
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                self.CLICK = False
                if b_close.rect.collidepoint(mouse):
                    return

                reload = True

                try:
                    if sel_button == EQP:
                        if b_equip.rect.collidepoint(mouse):
                            player.inv_equip(items_to_show[item_sel_index])
                            ASK_SAVE = True

                    elif sel_button == DQP:
                        if b_dequip.rect.collidepoint(mouse):
                            if item_sel_index == -1:
                                player.inv_dequip(player.get_weapon())
                                ASK_SAVE = True
                            if item_sel_index == -2:
                                player.inv_dequip(player.get_armor())
                                ASK_SAVE = True

                    if b_discard.rect.collidepoint(mouse):
                        amt = self.number_prompt("Discard Item", player.inventory[items_to_show[item_sel_index]],
                                                 desc_left, tb_desc.rect.bottom, width=desc_width, height=desc_height)
                        if amt:
                            ASK_SAVE = True
                            if item_sel_index == -1 or item_sel_index == -2:
                                player.inv_remove(items_to_show[item_sel_index], dropping=True)
                            else:
                                player.inv_remove(items_to_show[item_sel_index], amount=amt, discarding=True)
                    elif b_give.rect.collidepoint(mouse):
                        rec_index = self.player_prompt(player_index, desc_left, tb_desc.rect.bottom, width=desc_width,
                                                       height=desc_height)
                        if rec_index >= player_index:
                            rec_index += 1

                        if rec_index >= 0:
                            amt = self.number_prompt("Give Item", player.inventory[items_to_show[item_sel_index]],
                                                     desc_left, tb_desc.rect.bottom, width=desc_width, height=desc_height)
                            if amt:
                                ASK_SAVE = True
                                ENCOUNTERS[ENC_INDEX].inv_give(PLAYERS[player_index], PLAYERS[rec_index],
                                                               items_to_show[item_sel_index], amount=amt)

                except: pass

                if b_scrollup.rect.collidepoint(mouse) and start_index > 0:
                    item_sel_index = -3
                    start_index -= list_len
                elif b_scrolldown.rect.collidepoint(mouse) \
                        and start_index + list_len < len(player.inventory):
                    item_sel_index = -3
                    start_index += list_len
                elif b_weapon.rect.collidepoint(mouse):
                    sel_button = DQP
                    item_sel_index = -1
                elif b_armor.rect.collidepoint(mouse):
                    sel_button = DQP
                    item_sel_index = -2
                else:
                    for index, b_item in enumerate(item_buttons):
                        if b_item.rect.collidepoint(mouse):
                            item_sel_index = index
                            if c_items[items_to_show[item_sel_index]].get_is_weapon() \
                                    or c_items[items_to_show[item_sel_index]].get_is_armor():
                                sel_button = EQP
                            else:
                                sel_button = USE

            self.end_page()

    def stats_prompt(self, entity):
        return

    def travel_prompt(self):
        self.SCREEN.blit(load_image("./assets/travel_bg.jpg", WIDTH, HEIGHT), ORIGIN)
        e_top = 10
        e_left = 10
        cwid = 150
        cheight = 50
        max_cols = int(WIDTH / (cwid + 10))
        col_size = int(HEIGHT / (cheight + 10))
        go_to_index = ENC_INDEX

        encbuttons = list()
        columns = 1
        next_page_start = 1
        for index, enc in enumerate(ENCOUNTERS):
            if index > 0:
                # encbuttons.append(TextButton())
                if index == ENC_INDEX:
                    encbuttons.append(
                        TextButton(parent=self.SCREEN, text=enc.get_name(), t_size=18, t_font="nodesto",
                                   left=e_left, top=e_top, width=cwid, height=cheight, t_color=GOLD))
                else:
                    encbuttons.append(
                        TextButton(parent=self.SCREEN, text=enc.get_name(), t_size=14, t_font="nodesto",
                                   left=e_left, top=e_top, width=cwid, height=cheight))
                if index % col_size == 0:
                    e_top = 10
                    e_left += cwid + 10
                    columns += 1
                else:
                    e_top += cheight + 10
                if columns % max_cols == 0:
                    next_page_start = index + 1

        while True:
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                for index, enc in enumerate(encbuttons, 1):
                    if enc.rect.collidepoint(mouse):
                        change_enc(index)
                        self.CLICK = False
                        self.TO_TRAVEL = False
                        return

            self.end_page()

    def number_prompt(self, title, max_amt, in_left, in_top, width=200, height=320):
        result = ""
        rect = pygame.Rect(in_left, in_top, width, height)
        NumBox = NumberBox(self.SCREEN, width, height, result, rect, title)

        cl_left = rect.left + width - 30
        kp_top = NumBox.bottom + 10
        kp_dim = 50
        kp_left = rect.center[0] - int(kp_dim / 2) - kp_dim - 5

        can_clr = False
        keypad = list()

        b_close = TextButton(parent=self.SCREEN, text="X", t_font="hylia", t_size=24, left=cl_left, top=rect.top,
                             width=30, height=30)

        for num in range(1, 13):
            if num == 10:
                keypad.append(TextButton(parent=self.SCREEN, text="0", t_font="hylia", t_size=24,
                                         left=kp_left + kp_dim + 5, top=kp_top, width=kp_dim, height=kp_dim))
            elif num == 11:
                keypad.append(TextButton(parent=self.SCREEN, text="clr", t_font="hylia", t_size=20,
                                         left=kp_left - kp_dim - 5, top=kp_top, width=kp_dim, height=kp_dim))
            elif num == 12:
                keypad.append(TextButton(parent=self.SCREEN, text="en", t_font="hylia", t_size=20,
                                         left=kp_left + 5, top=kp_top, width=kp_dim, height=kp_dim))
            else:
                keypad.append(TextButton(parent=self.SCREEN, text=str(num), t_font="hylia", t_size=24,
                                         left=kp_left, top=kp_top, width=kp_dim, height=kp_dim))

            if num % 3 == 0:
                kp_left, kp_top = rect.center[0] - int(kp_dim / 2) - kp_dim - 5, kp_top + kp_dim + 5
            else:
                kp_left += kp_dim + 5

        while True:
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                if b_close.rect.collidepoint(mouse):
                    return
                for num, key in enumerate(keypad):
                    if key.rect.collidepoint(mouse):
                        key_val = num + 1

                        if can_clr:
                            result = ""
                            can_clr = False
                        if key_val == 10:
                            result += "0"
                        if key_val == 11:
                            result = ""
                        if key_val == 12:
                            if int(result) <= max_amt:
                                return int(result)
                            result = "You don't have that many!"
                            can_clr = True
                        else:
                            result += str(key_val)
                        NumBox.update_result(result)
                        self.CLICK = False
            self.end_page()

    def player_prompt(self, giver_index, in_left, in_top, width=200, height=320):
        rect = pygame.Rect(in_left, in_top, width, height)
        reload = True
        new_index = -1
        valid_selection = False
        recipients = list()
        for index, player in enumerate(PLAYERS):
            if index != giver_index:
                recipients.append(player)

        while True:
            if reload:
                reload = False

                p_box = PlayerBox(self.SCREEN, width, height, rect)
                p_buttons = list()

                cl_left = rect.left + width - 30
                b_close = TextButton(parent=self.SCREEN, text="X", t_font="hylia", t_size=24, left=cl_left, top=rect.top,
                                     width=30, height=30)
                p_top = p_box.bottom + 10
                b_ht = 35

                for index, player in enumerate(recipients):
                    if index == new_index:
                        p_color = GOLD
                    else:
                        p_color = WHITE

                    p_buttons.append(TextButton(parent=self.SCREEN, text=player.get_name(), t_size=20,
                                                just="left", t_font="nodesto", left=in_left, top=p_top,
                                                width=width, height=b_ht, t_color=p_color))
                    p_top += b_ht

                if valid_selection:
                    button_text = "> Confirm <"
                    button_color = GREEN
                else:
                    button_text = "Please select a recipient."
                    button_color = WHITE

                b_confirm = TextButton(parent=self.SCREEN, text=button_text, t_font="nodesto", t_color=button_color,
                                       t_size=20, left=in_left, top=in_top+height-b_ht, width=width, height=b_ht)

            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                self.CLICK = False

                if b_close.rect.collidepoint(mouse):
                    return -1
                elif b_confirm.rect.collidepoint(mouse) and valid_selection:
                    return new_index
                for num, player in enumerate(p_buttons):
                    if player.rect.collidepoint(mouse):
                        reload = True
                        new_index = num
                        valid_selection = True

            self.end_page()

    def dice_prompt(self, ent=None):
        entity = ent

        dice_options = ["d4", "d6", "d8", "d10", "d12", "d20"]
        width, height = 515, 320
        rect = pygame.Rect(int(WIDTH / 2) - int(width / 2), int(HEIGHT * 0.2), width, height)
        cl_left = rect.left + width - 30
        kp_dim = 50
        can_clr = False
        result = ""
        keypad = list()
        dicepad = list()
        checklist = list()

        dice_box = DiceBox(self.SCREEN, width, height, result, rect)
        kp_top = dice_box.bottom + 10
        kp_left = rect.left + 15

        dp_size = 60
        b_sum = 0       # Just to start it off.
        b_set = 0       # Just to start it off.

        b_close = TextButton(parent=self.SCREEN, text="X", t_font="hylia", t_size=24, left=cl_left, top=rect.top,
                             width=30, height=30)

        for num in range(1, 12):
            if num == 10:
                keypad.append(TextButton(parent=self.SCREEN, text="0", t_font="hylia", t_size=20,
                                         left=kp_left + kp_dim + 5, top=kp_top, width=kp_dim, height=kp_dim))
            elif num == 11:
                keypad.append(TextButton(parent=self.SCREEN, text="clr", t_font="hylia", t_size=24,
                                         left=kp_left + kp_dim + 5, top=kp_top, width=kp_dim, height=kp_dim))
            else:
                keypad.append(TextButton(parent=self.SCREEN, text=str(num), t_font="hylia", t_size=24,
                                         left=kp_left, top=kp_top, width=kp_dim, height=kp_dim))

            if num % 3 == 0:
                kp_left, kp_top = rect.left + 15, kp_top + kp_dim + 5
            else:
                kp_left += kp_dim + 5

        kp_top = dice_box.bottom + 10
        dp_left = kp_left + kp_dim + 15

        for num in range(6):
            dicepad.append(TextButton(parent=self.SCREEN, text=dice_options[num], t_font="hylia", t_size=20,
                                      left=dp_left, top=kp_top, width=dp_size, height=kp_dim))
            if num == 2:
                kp_top += kp_dim + 5
                b_set = TextButton(parent=self.SCREEN, text="Set", t_font="hylia", t_size=24, left=dp_left,
                                   top=kp_top, width=dp_size, height=kp_dim)
                dp_left += 65
                kp_top = dice_box.bottom + 10
            else:
                kp_top += kp_dim + 5
                if num == 5:
                    b_sum = TextButton(parent=self.SCREEN, text="Sum", t_font="hylia", t_size=24, left=dp_left,
                                       top=kp_top, width=dp_size, height=kp_dim)

        dp_left = dicepad[5].rect.right + 20
        kp_top = dicepad[1].rect.top
        chk_size = 80

        stat_name = ["Strength", "Dexterity", "Constitution", "Wisdom", "Intellect", "Charisma"]
        for num in range(6):
            checklist.append(TextButton(parent=self.SCREEN, text=stat_name[num][0:3], t_font="hylia", t_size=24,
                                        left=dp_left, top=kp_top, width=chk_size, height=kp_dim))
            if num == 2:
                kp_top = dicepad[1].rect.top
                dp_left += chk_size + 5
            else:
                kp_top += kp_dim + 5

        c_dim = 20
        cbox1 = pygame.Rect(dicepad[5].rect.right + 20, dice_box.bottom + 10, c_dim, c_dim)
        cbox1.center = (checklist[0].rect.left + int(c_dim / 2), dicepad[3].rect.centery)
        cbox2 = deepcopy(cbox1)
        cbox2.centerx = checklist[3].rect.left + int(c_dim / 2)

        cbox_adv = CheckBox(parent=self.SCREEN, rect=cbox1, center=True, state=False)
        cbox_dis = CheckBox(parent=self.SCREEN, rect=cbox2, center=True, state=False)

        c_temp = deepcopy(cbox1)
        c_temp.left = cbox_adv.urect.right + 5
        TextBox(parent=self.SCREEN, text="Advant.", t_size=16, t_font="nodesto", rect=c_temp, bind_2_rect=True)
        c_temp.left = cbox_dis.urect.right + 5
        TextBox(parent=self.SCREEN, text="Disadv.", t_size=16, t_font="nodesto", rect=c_temp, bind_2_rect=True)

        # ==================================
        # Mouse Events
        # ==================================
        while True:
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                self.CLICK = False
                if b_close.rect.collidepoint(mouse):
                    return

                elif b_sum.rect.collidepoint(mouse):
                    try:
                        int(result) == int
                    except:
                        try:
                            num_dice, diceface = result.split("d")
                            result = str(ENCOUNTERS[ENC_INDEX].rollDice(int(num_dice), int(diceface),
                                                                        print_results=False))
                        except:
                            result = "ERROR"

                    dice_box.update_result(result)
                    can_clr = True

                elif b_set.rect.collidepoint(mouse):
                    try:
                        int(result) == int
                    except:
                        try:
                            num_dice, diceface = result.split("d")
                            result = str(ENCOUNTERS[ENC_INDEX].rollDice(int(num_dice), int(diceface), print_results=False, set_form=True))
                        except:
                            result = "ERROR"

                    dice_box.update_result(result)
                    can_clr = True

                elif cbox_adv.urect.collidepoint(mouse):
                    if cbox_adv.is_checked:
                        cbox_adv.uncheck()
                    else:
                        cbox_adv.check()
                elif cbox_dis.urect.collidepoint(mouse):
                    if cbox_dis.is_checked:
                        cbox_dis.uncheck()
                    else:
                        cbox_dis.check()
                else:
                    for num, key in enumerate(keypad):
                        if key.rect.collidepoint(mouse):
                            key_val = num + 1

                            if can_clr:
                                result = ""
                                can_clr = False
                            if key_val == 10:
                                result += "0"
                            if key_val == 11:
                                result = ""
                            else:
                                result += str(key_val)
                            dice_box.update_result(result)

                    for num, diceface in enumerate(dicepad):
                        if diceface.rect.collidepoint(mouse):
                            if can_clr:
                                result = ""
                                can_clr = False
                            result += dice_options[num]
                            dice_box.update_result(result)

                    for num, check in enumerate(checklist):
                        if check.rect.collidepoint(mouse):
                            result = ENCOUNTERS[ENC_INDEX].performCheck(stat_name[num], None, entity,
                                                                        advantage=cbox_adv.is_checked,
                                                                        disadvantage=cbox_dis.is_checked,
                                                                        print_results=False)[0]

                            if result >= 0:
                                dice_box.update_result(str(result))
                            else:
                                result = 0
                                dice_box.update_result(str(result))
                            can_clr = True

            self.end_page()

    def stat_prompt(self, ent=None):
        statblock = ent.get_stat_block()

        width, height = 400, HEIGHT
        rect = pygame.Rect(WIDTH - width, 0, width, height)
        stat_box = StatBox(self.SCREEN, width, height, rect, ent.get_name())
        color = WHITE

        b_close = TextButton(parent=self.SCREEN, text="X", t_font="hylia", t_size=24, left=rect.right - 30,
                             top=rect.top, width=30, height=30)

        # Text fields
        s_left, s_top = stat_box.rect.left + 20, stat_box.bottom + 10

        tb_level = TextBox(parent=self.SCREEN, text="Lv. " + str(ent.get_level()), left=s_left, top=s_top,
                           t_font="hylia", t_color=color)

        if type(ent) == Player:
            tb_race = TextBox(parent=self.SCREEN, text=ent.get_race(), left=tb_level.right + 10, top=s_top,
                              t_font="hylia", t_color=color)
            tb_role = TextBox(parent=self.SCREEN, text=ent.get_role(), left=tb_race.right + 5, top=s_top,
                              t_font="hylia", t_color=color)
        else:
            tb_race = TextBox(parent=self.SCREEN, text=ent.get_name(), left=tb_level.right + 10, top=s_top,
                              t_font="hylia", t_color=color)

        s_top = tb_level.bottom + 10
        hp = str(statblock.get_stat("Current HP")) + "/" + str(statblock.get_stat("Max HP"))
        hd = str(statblock.get_stat("Hit Dice Quantity")) + "/" + str(ent.get_level()) + "d" + str(statblock.get_stat("Hit Dice"))

        # Text Fields
        tb_ac = TextBox(parent=self.SCREEN, text="Armor Class: ", left=s_left, top=s_top, t_font="nodesto")
        tb_hp = TextBox(parent=self.SCREEN, text="Hit Points: ", left=s_left, top=tb_ac.bottom, t_font="nodesto")
        if type(ent) == Player:
            tb_hd = TextBox(parent=self.SCREEN, text="Hit Dice: ", left=s_left, top=tb_hp.bottom, t_font="nodesto")
            s_left = max(tb_ac.right, tb_hp.right, tb_hd.right) + 20
        else:
            s_left = max(tb_ac.right, tb_hp.right) + 20

        # Values
        value_size = 16
        TextBox(parent=self.SCREEN, text=str(statblock.get_stat("Armor Class")), left=s_left,
                top=s_top + int(0.25 * value_size), t_size=value_size, t_font="nodesto")
        TextBox(parent=self.SCREEN, text=hp, left=s_left, top=tb_ac.bottom + int(0.25 * value_size),
                t_size=value_size, t_font="nodesto")
        if type(ent) == Player:
            TextBox(parent=self.SCREEN, text=hd, left=s_left, top=tb_hp.bottom + int(0.25 * value_size),
                    t_size=value_size, t_font="nodesto")
            s_left = max(tb_ac.right, tb_hp.right, tb_hd.right) + 100
        else:
            s_left = max(tb_ac.right, tb_hp.right) + 100

        s_top = tb_ac.rect.top

        # Text Fields
        tb_speed = TextBox(parent=self.SCREEN, text="Max Speed: ", left=s_left, top=s_top, t_font="nodesto")
        tb_init = TextBox(parent=self.SCREEN, text="Inspiration: ", left=s_left, top=tb_speed.bottom, t_font="nodesto")
        tb_profb = TextBox(parent=self.SCREEN, text="Prof. Bonus: ", left=s_left, top=tb_init.bottom, t_font="nodesto")

        s_left = max(tb_speed.right, tb_init.right, tb_profb.right) + 20

        # Values
        TextBox(parent=self.SCREEN, text=str(statblock.get_stat("Speed")), left=s_left,
                top=tb_speed.rect.top + int(0.25 * value_size), t_size=value_size, t_font="nodesto")
        TextBox(parent=self.SCREEN, text=str(statblock.get_stat("Inspiration")), left=s_left,
                top=tb_init.rect.top + int(0.25 * value_size), t_size=value_size, t_font="nodesto")
        TextBox(parent=self.SCREEN, text=str(statblock.get_stat("Proficiency Bonus")), left=s_left,
                top=tb_profb.rect.top + int(0.25 * value_size), t_size=value_size, t_font="nodesto")

        s_top = tb_profb.bottom + 10

        statlist = list()
        temp = list(statblock.get_dict())
        temp = temp[8:14]
        maxleft = [0, 0, 0, 0]

        # Stat Text Loop
        for num, stat in enumerate(temp):
            if num % 2 == 0:
                if num > 0:
                    s_top = statlist[num - 1].bottom
                s_left = stat_box.rect.left + 20

            statlist.append(TextBox(parent=self.SCREEN, text=stat + ": ", left=s_left, top=s_top, t_font="nodesto"))
            if num % 2 == 0:
                maxleft[0] = max(maxleft[0], statlist[num].right)
            else:
                maxleft[1] = max(maxleft[1], statlist[num].right)

            if num > 1:
                s_left = statlist[1].rect.left
            else:
                s_left = statlist[num].right + 120

        # Base Stat Loop
        s_top = statlist[0].rect.top
        for num, stat in enumerate(temp):
            if num % 2 == 0:
                if num > 0:
                    s_top = statlist[num - 1].bottom
                s_left = maxleft[0]
            else:
                s_left = maxleft[1]

            val = statblock.get_stat(stat)
            if val < 10:
                val = " " + str(val)
            else:
                val = str(val)

            tb_value = TextBox(parent=self.SCREEN, text=val, left=s_left, top=s_top, t_font="nodesto")
            if num % 2 == 0:
                maxleft[2] = max(maxleft[2], tb_value.right)
            else:
                maxleft[3] = max(maxleft[3], tb_value.right)

        # Modifier Loop
        s_top = statlist[0].rect.top
        for num, stat in enumerate(temp):
            if num % 2 == 0:
                if num > 0:
                    s_top = statlist[num - 1].bottom
                s_left = maxleft[2] + 5
            else:
                s_left = maxleft[3] + 5

            val = statblock.get_mod(stat)
            if val >= 0:
                val = "(+" + str(val) + ")"
            else:
                val = "(" + str(val) + ")"

            tb_value = TextBox(parent=self.SCREEN, text=val, left=s_left, top=s_top)

        # Fresh Start for skills.
        temp = list(statblock.get_dict())
        temp = temp[14:]
        maxleft = [0, 0]
        s_top += 40

        skilllist = list()
        for num, stat in enumerate(temp):
            if num % 2 == 0:
                if num > 0:
                    s_top = skilllist[num - 1].bottom
                s_left = stat_box.rect.left + 20
            else:
                if num > 1:
                    s_left = skilllist[1].rect.left
                else:
                    s_left = statlist[1].rect.left - 20

            skilllist.append(TextBox(parent=self.SCREEN, text=stat + ": ", left=s_left, top=s_top, t_font="nodesto"))
            if num % 2 == 0:
                maxleft[0] = max(maxleft[0], skilllist[num].right)
            else:
                maxleft[1] = max(maxleft[1], skilllist[num].right)

        str_list = [17]
        dex_list = [14, 29, 30]
        int_list = [16, 19, 22, 24, 28]
        wis_list = [15, 20, 23, 25, 31]
        cha_list = [18, 21, 26, 27]

        for num, stat in enumerate(temp, 14):
            if num % 2 == 0:
                s_top = skilllist[num-14].rect.top
                s_left = maxleft[0] + 5
            else:
                s_left = maxleft[1] + 5

            if num in str_list:
                val = statblock.get_mod("Strength")
            elif num in dex_list:
                val = statblock.get_mod("Dexterity")
            elif num in int_list:
                val = statblock.get_mod("Intellect")
            elif num in wis_list:
                val = statblock.get_mod("Wisdom")
            elif num in cha_list:
                val = statblock.get_mod("Charisma")

            if val > 0:
                val = "+" + str(val)
            else:
                val = str(val)

            skilllist.append(TextBox(parent=self.SCREEN, text=val, left=s_left, top=s_top))

        while True:
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                self.CLICK = False
                if b_close.rect.collidepoint(mouse):
                    return

            self.end_page()

    def prompt_quit(self):
        global ASK_SAVE     # TODO: Fix bug where encounter won't reset after decline without exit.
        if not ASK_SAVE:
            self.TO_MAIN_MENU = True
            return True

        width, height = 280, 120
        t_font = use_font(size=20, font="hylia")
        rect = pygame.Rect(B_CENTER, int(HEIGHT * 0.33), width, height)
        b_top = rect.center[1] + 10
        ch_width = 70
        cl_left = rect.left + width - 30

        QuitBox(self.SCREEN, width, height, t_font, rect)
        b_yes = TextButton(parent=self.SCREEN, text="Accept", t_size=20,
                           left=rect.center[0]-ch_width-5, top=b_top, width=ch_width, height=30)
        b_no = TextButton(parent=self.SCREEN, text="Decline", t_size=20,
                          left=rect.center[0]+5, top=b_top, width=ch_width, height=30)
        b_close = TextButton(parent=self.SCREEN, text="X", t_font="hylia", t_size=24, left=cl_left, top=rect.top,
                             width=30, height=30)
        while True:
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                self.CLICK = False
                if b_yes.rect.collidepoint(mouse):
                    save()
                    ASK_SAVE = False
                    self.TO_MAIN_MENU = True
                    return True
                elif b_no.rect.collidepoint(mouse):
                    self.TO_MAIN_MENU = True
                    ASK_SAVE = True
                    return True
                elif b_close.rect.collidepoint(mouse):
                    return False

            self.end_page()

    def end_page(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.CLICK = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.CLICK = False

        pygame.display.update()
        self.CLK.tick(15)


disp = Display()
disp.page_startup()
