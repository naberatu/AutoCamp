import random
import time
import pygame
import pickle
from player import Player
from enemy import Enemy
from cencounter import CEncounter
from encounter import Encounter
from campaign_default import load_default_camp
from items import c_items

from os import environ
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
DIRT = (197, 145, 84)
GOLD = (241, 194, 50)

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
ENCOUNTER_INDEX = 1         # Can never be 0, since that's its own index
ASK_SAVE = False


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


def change_enc(index):
    global PLAYERS, ENCOUNTERS, ENCOUNTER_INDEX, ASK_SAVE

    if index == ENCOUNTER_INDEX:
        return

    PLAYERS = ENCOUNTERS[ENCOUNTER_INDEX].save_players()

    ENCOUNTER_INDEX = index
    ENCOUNTERS[ENCOUNTER_INDEX].load_players(PLAYERS)
    ASK_SAVE = True


def save():
    global PLAYERS, ENCOUNTERS, ENCOUNTER_INDEX, ASK_SAVE
    ENCOUNTERS[0] = ENCOUNTER_INDEX
    pickle.dump(EMPTY_LIST, open("players.camp", "wb"))
    pickle.dump(EMPTY_LIST, open("savegame.camp", "wb"))
    pickle.dump(PLAYERS, open("players.camp", "wb"))
    pickle.dump(ENCOUNTERS, open("savegame.camp", "wb"))
    ASK_SAVE = False


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
        title_box.top = rect.top + 10

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


class TileButton:
    def __init__(self, parent=None, img=None, left=0, top=0, width=TILE_SIZE, height=TILE_SIZE):
        self.rect = pygame.Rect(left, top, width, height)
        self.img = img

        self.img_rect = self.img.get_rect()
        self.img_rect.center = self.rect.center

        parent.blit(self.img, self.img_rect)


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
    def __init__(self, parent=None, center=False, text="test", t_size=20, t_color=WHITE, t_font="scaly", left=0, top=0):

        self.t_size, self.t_color = t_size, t_color
        self.t_font = use_font(size=t_size, font=t_font)

        self.rect = pygame.Rect(left, top, WIDTH - (2 * left), 0)

        self.text, self.textbox = text_objects(text, self.t_font, t_color)
        if center:
            self.textbox.center = self.rect.center
        else:
            self.textbox.left = left

        self.textbox.top = top
        parent.blit(self.text, self.textbox)


# test comment
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

    global PLAYERS, ENCOUNTERS, ENCOUNTER_INDEX, MODE, EMPTY_LIST

    # Load Data
    # ==================================
    try:
        # global PLAYERS, ENCOUNTERS, ENCOUNTER_INDEX
        PLAYERS = pickle.load(open("players.camp", "rb"))
        PLAYERS_OK = True
        ENCOUNTERS = pickle.load(open("savegame.camp", "rb"))
        ENCOUNTERS_OK = True
    except:
        if not PLAYERS_OK:
            PLAYERS.append(Player("Fjord", "Orc", "Warlock"))
            PLAYERS.append(Player("Jester Lavorre", "Tiefling", "Cleric"))
            PLAYERS.append(Player("Caleb Widowgast", "Human", "Wizard"))
            PLAYERS.append(Player("Yasha Nyoodrin", "Aasimar", "Barbarian"))
            PLAYERS.append(Player("Veth Brenatto", "Goblin", "Rogue"))

            for hero in PLAYERS:
                hero.set_weapon("Shortsword")
                hero.set_armor("Chain Mail")
                hero.inv_add("Mana Potion", random.randint(1, 6))
                hero.inv_add("Bread (Loaf)", random.randint(1, 4))
                hero.inv_add("Spyglass", 1)
                hero.inv_add("Fishing Tackle", 2)
                hero.inv_add("Clothes (Common)", random.randint(3, 8))
                hero.inv_add("Handaxe", random.randint(1, 2))
                hero.inv_add("Net", random.randint(1, 2))
                hero.inv_add("Leather Armor", 1)

            pickle.dump(EMPTY_LIST, open("players.camp", "wb"))
            pickle.dump(PLAYERS, open("players.camp", "wb"))
            ENCOUNTERS_OK = False

        if not ENCOUNTERS_OK:
            # # for index in range(e_battle.get_al_size()):
            # #     entity = e_battle.get_entity(True, index)
            # #
            # #     while e_battle.enc_move(entity, max(MAP_MAX_X, MAP_MAX_Y) * 5,
            # #                        random.randint(1, MAP_MAX_X), random.randint(1, MAP_MAX_Y))[1]:
            # #         pass
            ENCOUNTERS = load_default_camp()
            pickle.dump(EMPTY_LIST, open("savegame.camp", "wb"))
            pickle.dump(ENCOUNTERS, open("savegame.camp", "wb"))

    ENCOUNTER_INDEX = ENCOUNTERS[0]
    change_enc(ENCOUNTER_INDEX)

    # Pages and Menus
    # ==================================
    def page_startup(self):
        st_font = "hylia"

        while True:
            # Graphics Generation
            # ==================================
            self.SCREEN.blit(self.BG_STARTUP, ORIGIN)
            b_start = TextButton(parent=self.SCREEN, text="Start", t_font=st_font, left=B_CENTER,
                                 top=B_YPOS - (2 * B_HEIGHT) - 5, width=B_WIDTH, height=B_HEIGHT)
            b_credits = TextButton(parent=self.SCREEN, text="Credits", t_font=st_font, left=B_CENTER,
                                   top=B_YPOS - B_HEIGHT, width=B_WIDTH, height=B_HEIGHT)
            b_quit = TextButton(parent=self.SCREEN, text="Exit", t_font=st_font, left=B_CENTER,
                                top=B_YPOS + 5, width=B_WIDTH, height=B_HEIGHT)

            # Button Functions
            # ==================================
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                if b_start.rect.collidepoint(mouse):
                    self.CLICK = False
                    ENCOUNTERS[ENCOUNTER_INDEX].load_players(PLAYERS)
                    while True:
                        if self.TO_MAIN_MENU:
                            self.TO_MAIN_MENU = False
                            break
                        if self.TO_TRAVEL:
                            self.travel_prompt()
                        if type(ENCOUNTERS[ENCOUNTER_INDEX]) == CEncounter:
                            self.page_map()
                        else:
                            self.page_nce()
                elif b_quit.rect.collidepoint(mouse):
                    sys.exit()
                elif b_credits.rect.collidepoint(mouse):
                    self.CLICK = False
                    self.page_credits()

            self.end_page()

    def page_map(self):
        reload = True
        leave_message = "Travel"

        tile_list = list()
        x, y = 0, 0
        tile_img = load_image(ENCOUNTERS[ENCOUNTER_INDEX].get_tile_img(), TILE_SIZE, TILE_SIZE)
        self.SCREEN.blit(tile_img, ORIGIN)

        for y_tile in range(MAP_MAX_Y):
            y = int(TILE_SIZE * y_tile)
            for x_tile in range(MAP_MAX_X):
                x = int(TILE_SIZE * x_tile)
                b_tile = TileButton(parent=self.SCREEN, img=tile_img, left=x, top=y)
                tile_list.append([b_tile, (x, y)])

        x, y = -1, -1

        while True:
            tile_coors = "Tile: "
            if x >= 0 and y >= 0:
                tile_coors += "(" + str(x) + ", " + str(y) + ")"

            if ENCOUNTERS[ENCOUNTER_INDEX].no_enemies():
                if leave_message == "Flee":
                    reload = True
                leave_message = "Travel"
            else:
                if leave_message == "Travel":
                    reload = True
                leave_message = "Flee"

            if reload:
                self.SCREEN.blit(load_image("./assets/travel_bg.jpg", WIDTH, HEIGHT), ORIGIN)

                reload = False
                # Control Buttons
                # ==================================
                TextBox(parent=self.SCREEN, text=tile_coors, t_color=BLACK, left=(MAP_MAX_X * TILE_SIZE) + 20, top=int(HEIGHT/2))

                b_quitgame = TextButton(parent=self.SCREEN, text="Quit", left=Q_LF, top=10, width=Q_WD, height=Q_HT)
                b_travel = TextButton(parent=self.SCREEN, text=leave_message, left=Q_LF - Q_WD - 10,
                                      top=b_quitgame.rect.top, width=Q_WD, height=Q_HT)

                for tile in tile_list:
                    tile[0] = TileButton(parent=self.SCREEN, img=tile_img, left=tile[1][0], top=tile[1][1])

            # Mouse Events
            # ==================================
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                if b_quitgame.rect.collidepoint(mouse):
                    if self.prompt_quit():
                        return
                if mouse[0] <= MAP_MAX_Y * TILE_SIZE:
                    reload = True
                    x = int(mouse[0] / TILE_SIZE)
                    y = int(mouse[1] / TILE_SIZE)
                if b_travel.rect.collidepoint(mouse):
                    self.travel_prompt()
                    return

            self.end_page()

    def page_nce(self):
        global ASK_SAVE
        menu_top = 390
        menu_left = 670
        cwid = 120
        offs = cwid + 10
        background = load_image(ENCOUNTERS[ENCOUNTER_INDEX].get_bg(), WIDTH, HEIGHT)
        player_index = 0
        current_player = PLAYERS[0]

        while True:
            if ASK_SAVE:
                save_text = "Save"
            else:
                save_text = "Saved!"

            self.SCREEN.blit(background, ORIGIN)
            title = TextButton(parent=self.SCREEN, text=ENCOUNTERS[ENCOUNTER_INDEX].get_name(), t_size=24, t_font="hylia",
                               left=int(WIDTH / 2) - 150, top=10, width=300, height=50)
            b_quitgame = TextButton(parent=self.SCREEN, text="Quit", left=Q_LF, top=10, width=Q_WD, height=Q_HT)
            b_save = TextButton(parent=self.SCREEN, text=save_text, left=Q_LF - Q_WD - 10, top=10, width=Q_WD, height=Q_HT)
            b_travel = TextButton(parent=self.SCREEN, text="Travel", left=menu_left, top=menu_top, width=cwid)
            b_roll = TextButton(parent=self.SCREEN, text="Roll", left=menu_left - offs, top=menu_top, width=cwid)
            b_inv = TextButton(parent=self.SCREEN, text="Inventory", left=menu_left-(2*offs), top=menu_top, width=cwid)

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
                if b_save.rect.collidepoint(mouse):
                    save()
                if b_travel.rect.collidepoint(mouse):
                    self.TO_TRAVEL = True
                    return
                if b_roll.rect.collidepoint(mouse):
                    self.dice_prompt()
                if b_inv.rect.collidepoint(mouse):
                    self.inv_prompt(current_player, cwid)
                for index, button in enumerate(exp_buttons):
                    if button.rect.collidepoint(mouse):
                        player_index = index

            self.end_page()

    def page_credits(self):
        while True:
            self.SCREEN.fill(BLACK)

            tb_title = TextBox(parent=self.SCREEN, text="AutoCamp Team", t_font="hylia", t_size=30,
                               top=30, center=True)
            tb_member1 = TextBox(parent=self.SCREEN, text="Nader Atout", t_font="hylia", t_size=20, center=True,
                                 top=tb_title.textbox.top + tb_title.textbox.height)
            tb_member2 = TextBox(parent=self.SCREEN, text="Diana Penalba", t_font="hylia", t_size=20, center=True,
                                 top=tb_member1.textbox.top + tb_member1.textbox.height)
            tb_member3 = TextBox(parent=self.SCREEN, text="Adrian Gavrila", t_font="hylia", t_size=20, center=True,
                                 top=tb_member2.textbox.top + tb_member2.textbox.height)

            tb_advisor = TextBox(parent=self.SCREEN, text="Team Advisor", t_font="hylia", t_size=30, center=True,
                                 top=tb_member3.textbox.top + tb_member3.textbox.height + 20)
            tb_advname = TextBox(parent=self.SCREEN, text="Asst. Prof. Salma Elmalaki", t_font="hylia", t_size=20,
                                 center=True, top=tb_advisor.textbox.top + tb_advisor.textbox.height)

            tb_game = TextBox(parent=self.SCREEN, text="Original Tabletop Game", t_font="hylia", t_size=30,
                              center=True, top=tb_advname.textbox.top + tb_advname.textbox.height + 20)
            tb_wizards = TextBox(parent=self.SCREEN, text="Wizards of the Coast", t_font="hylia", t_size=20,
                                 center=True, top=tb_game.textbox.top + tb_game.textbox.height)

            tb_images = TextBox(parent=self.SCREEN, text="All artwork found through Google Images", t_font="hylia",
                                t_size=20, center=True, top=tb_wizards.textbox.top + tb_wizards.textbox.height + 20)

            b_back = TextButton(parent=self.SCREEN, path="./assets/b_credits.png", text="Back", left=B_CENTER,
                                top=B_YPOS + 60, width=B_WIDTH, height=B_HEIGHT)

            if b_back.rect.collidepoint(pygame.mouse.get_pos()) and self.CLICK:
                return

            self.end_page()

    def inv_prompt(self, player, bwid):
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
        update_inv_list = True
        sel_button = 0
        EQP, DQP, USE = 1, 2, 3
        font_size = 20

        while True:
            if update_inv_list:
                # Critical to ensure that it blits at the right time.
                update_inv_list = False

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
                if item_sel_index >= -2:
                    awid, aheight = 100, 40
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

            # ==================================
            # Mouse Events
            # ==================================
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                self.CLICK = False
                if b_close.rect.collidepoint(mouse):
                    return

                update_inv_list = True

                try:
                    self.CLICK = False
                    if sel_button == EQP:
                        if b_equip.rect.collidepoint(mouse):
                            player.inv_equip(items_to_show[item_sel_index])
                            ASK_SAVE = True

                    if sel_button == DQP:
                        if b_dequip.rect.collidepoint(mouse):
                            if item_sel_index == -1:
                                player.inv_dequip(player.get_weapon())
                                ASK_SAVE = True
                            if item_sel_index == -2:
                                player.inv_dequip(player.get_armor())
                                ASK_SAVE = True


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

    def travel_prompt(self):
        self.SCREEN.blit(load_image("./assets/travel_bg.jpg", WIDTH, HEIGHT), ORIGIN)
        e_top = 10
        e_left = 10
        cwid = 150
        cheight = 50
        max_cols = int(WIDTH / (cwid + 10))
        col_size = int(HEIGHT / (cheight + 10))
        go_to_index = ENCOUNTER_INDEX

        encbuttons = list()
        columns = 1
        next_page_start = 1
        for index, enc in enumerate(ENCOUNTERS):
            if index > 0:
                # encbuttons.append(TextButton())
                if index == ENCOUNTER_INDEX:
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

    def dice_prompt(self):
        dice_options = ["d4", "d6", "d8", "d10", "d12", "d20"]
        width, height = 335, 320
        rect = pygame.Rect(int(WIDTH/2) - int(width / 2), int(HEIGHT * 0.2), width, height)
        cl_left = rect.left + width - 30
        kp_dim = 50
        can_clr = False
        result = ""
        keypad = list()
        dicepad = list()
        dice_box = DiceBox(self.SCREEN, width, height, result, rect)
        kp_top = dice_box.bottom + 10
        kp_left = rect.left + 10
        dp_size = 60
        dp_left = rect.right - 20 - (2 * dp_size)
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
                kp_left, kp_top = rect.left + 10, kp_top + kp_dim + 5
            else:
                kp_left += kp_dim + 5

        kp_top = dice_box.bottom + 10
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

        # ==================================
        # Mouse Events
        # ==================================
        while True:
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                if b_close.rect.collidepoint(mouse):
                    return

                if b_sum.rect.collidepoint(mouse):
                    try:
                        int(result) == int
                    except:
                        try:
                            num_dice, diceface = result.split("d")
                            result = str(ENCOUNTERS[ENCOUNTER_INDEX].rollDice(int(num_dice), int(diceface),
                                                                                   print_results=False))
                        except:
                            result = "ERROR"

                    dice_box.update_result(result)
                    can_clr = True

                if b_set.rect.collidepoint(mouse):
                    try:
                        int(result) == int
                    except:
                        try:
                            num_dice, diceface = result.split("d")
                            result = str(ENCOUNTERS[ENCOUNTER_INDEX].rollDice(int(num_dice), int(diceface), print_results=False, set_form=True))
                        except:
                            result = "ERROR"

                    dice_box.update_result(result)
                    can_clr = True

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
                        self.CLICK = False

                for num, diceface in enumerate(dicepad):
                    if diceface.rect.collidepoint(mouse):
                        if can_clr:
                            result = ""
                            can_clr = False
                        result += dice_options[num]
                        dice_box.update_result(result)
                        self.CLICK = False

            self.end_page()

    def prompt_quit(self):
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
                if b_yes.rect.collidepoint(mouse):
                    self.CLICK = False
                    save()
                    self.TO_MAIN_MENU = True
                    return True
                if b_no.rect.collidepoint(mouse):
                    self.CLICK = False
                    self.TO_MAIN_MENU = True
                    return True
                if b_close.rect.collidepoint(mouse):
                    self.CLICK = False
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
