import random
import time
import pygame
import pickle
from player import Player
from enemy import Enemy
from cencounter import CEncounter
from encounter import Encounter

from os import environ
import sys
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Screen Dimensions:
WIDTH = 800  # Use 16x16 sprites & tiles. Makes 50x30 grid.
HEIGHT = 480
ORIGIN = (0, 0)

# Map Dimensions:
MAP_MAX_X = 15
MAP_MAX_Y = 15

TILE_SIZE = int(HEIGHT / MAP_MAX_Y)      # Usually would be 32

# Base Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DIRT = (197, 145, 84)

# Button Dimensions:
B_WIDTH = 200
B_HEIGHT = 50
B_CENTER = 300
B_YPOS = 330

# Encounter & Player Data
MODE = "Battle"         # Can also be "Explore"
EMPTY_LIST = list()
PLAYERS = list()
ENCOUNTERS = list()
ENCOUNTER_INDEX = 1         # Can never be 0, since that's its own index


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
    global ENCOUNTERS, ENCOUNTER_INDEX, MODE
    ENCOUNTER_INDEX = index
    ENCOUNTERS[0] = ENCOUNTER_INDEX
    if type(ENCOUNTERS[ENCOUNTER_INDEX]) == CEncounter:
        MODE = "Battle"
    else:
        MODE = "Explore"


def save():
    global PLAYERS, ENCOUNTERS
    pickle.dump(EMPTY_LIST, open("players.camp", "wb"))
    pickle.dump(EMPTY_LIST, open("savegame.camp", "wb"))
    pickle.dump(PLAYERS, open("players.camp", "wb"))
    pickle.dump(ENCOUNTERS, open("savegame.camp", "wb"))


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


class TileButton:
    def __init__(self, parent=None, left=0, top=0, width=TILE_SIZE, height=TILE_SIZE, color=DIRT):
        self.color = color
        self.rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(parent, self.color, self.rect)

        IMAGE = pygame.image.load("./assets/grasstile.png").convert()
        IMAGE = pygame.transform.scale(IMAGE, (TILE_SIZE, TILE_SIZE))
        self.img_rect = IMAGE.get_rect()
        self.img_rect.center = self.rect.center

        parent.blit(IMAGE, self.img_rect)


class TextButton:
    def __init__(self, parent=None, path="./assets/button.png", text="test", t_size=20, t_color=WHITE, t_font="scaly",
                 left=0, top=0, width=B_WIDTH, height=B_HEIGHT):

        self.textstr = text
        self.parent = parent
        self.t_size, self.t_color = t_size, t_color
        self.t_font = use_font(size=t_size, font=t_font)

        self.box = load_image(path, width, height)

        self.rect = pygame.Rect(left, top, width, height)

        self.text, self.textbox = text_objects(self.textstr, self.t_font, t_color)
        self.textbox.center = self.rect.center

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

            pickle.dump(EMPTY_LIST, open("players.camp", "wb"))
            pickle.dump(PLAYERS, open("players.camp", "wb"))
            ENCOUNTERS_OK = False

        if not ENCOUNTERS_OK:
            e_town = Encounter("Tavern")
            e_battle = CEncounter("Grassy Plain")
            e_battle.enc_fill_map()

            # Example Entities
            e_battle.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
            e_battle.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
            e_battle.add_entity(Enemy("Werewolf", "Wolf", "Doggo"))
            # for player in PLAYERS:            # TODO Only add players when starting this encounter.
            #     e_battle.add_entity(player)
            # e_battle.start_encounter()

            # Populator Loop
            # for index in range(e_battle.get_al_size()):
            #     entity = e_battle.get_entity(True, index)
            #
            #     while e_battle.enc_move(entity, max(MAP_MAX_X, MAP_MAX_Y) * 5,
            #                        random.randint(1, MAP_MAX_X), random.randint(1, MAP_MAX_Y))[1]:
            #         pass

            ENCOUNTERS.append(1)                # Encounter tracker.
            ENCOUNTERS.append(e_battle)         # Encounter 1
            ENCOUNTERS.append(e_town)           # Encounter 2
            pickle.dump(EMPTY_LIST, open("savegame.camp", "wb"))
            pickle.dump(ENCOUNTERS, open("savegame.camp", "wb"))

    change_enc(ENCOUNTERS[0])
    CURRENT_ENCOUNTER = ENCOUNTERS[ENCOUNTER_INDEX]

    # Pages and Menus
    # ==================================
    def page_startup(self):
        st_font = "hylia"

        while True:
            # Graphics Generation
            # ==================================
            self.SCREEN.blit(self.BG_STARTUP, ORIGIN)
            b_start = TextButton(parent=self.SCREEN, text="Start", t_font=st_font, left=B_CENTER, top=B_YPOS - (2 * B_HEIGHT), width=B_WIDTH, height=B_HEIGHT)
            b_credits = TextButton(parent=self.SCREEN, text="Credits", t_font=st_font, left=B_CENTER, top=B_YPOS - B_HEIGHT, width=B_WIDTH, height=B_HEIGHT)
            b_quit = TextButton(parent=self.SCREEN, text="Exit", t_font=st_font, left=B_CENTER, top=B_YPOS, width=B_WIDTH, height=B_HEIGHT)

            # Button Functions
            # ==================================
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                if b_start.rect.collidepoint(mouse):
                    self.CLICK = False
                    while True:
                        if self.TO_MAIN_MENU:
                            self.TO_MAIN_MENU = False
                            break
                        if ENCOUNTERS[ENCOUNTER_INDEX].is_combat:
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
        tile_list = list()
        x, y = 0, 0
        for y_tile in range(MAP_MAX_Y):
            y = int(TILE_SIZE * y_tile)
            for x_tile in range(MAP_MAX_X):
                x = int(TILE_SIZE * x_tile)
                b_tile = TileButton(parent=self.SCREEN, left=x, top=y, color=DIRT)
                tile_list.append([b_tile, (x, y)])

        x, y = -1, -1
        mb_width = 60

        while True:
            self.SCREEN.fill(DIRT)
            tile_coors = "Tile: "
            if x >= 0 and y >= 0:
                tile_coors += "(" + str(x) + ", " + str(y) + ")"

            # Control Buttons
            # ==================================
            tb_coors = TextBox(parent=self.SCREEN, text=tile_coors,
                               left=(MAP_MAX_X * TILE_SIZE) + 20, top=int(HEIGHT/2))
            b_quitgame = TextButton(parent=self.SCREEN, text="Quit Game", left=(MAP_MAX_X * TILE_SIZE) + 20,
                                    top=int(0.8 * HEIGHT), width=120)
            b_move = TextButton(parent=self.SCREEN, text="Move", left=WIDTH - mb_width - 10,
                                top=b_quitgame.rect.top, width=mb_width)

            for tile in tile_list:
                tile[0] = TileButton(parent=self.SCREEN, left=tile[1][0], top=tile[1][1], color=DIRT)

            # Mouse Events
            # ==================================
            mouse = pygame.mouse.get_pos()
            if self.CLICK:
                if b_quitgame.rect.collidepoint(mouse):
                    if self.prompt_quit():
                        return
                if mouse[0] <= (MAP_MAX_Y + 1) * TILE_SIZE:
                    x = int(mouse[0] / TILE_SIZE)
                    y = int(mouse[1] / TILE_SIZE)
                if b_move.rect.collidepoint(mouse):
                    change_enc(2)
                    return

            self.end_page()

    def page_nce(self):
        menu_top = 420
        menu_left = 670
        cwid = 120
        offs = cwid + 10
        background = self.BG_TAVERN
        player_index = 0
        current_player = PLAYERS[0]

        while True:
            self.SCREEN.blit(background, ORIGIN)
            title = TextButton(parent=self.SCREEN, text=ENCOUNTERS[ENCOUNTER_INDEX].get_name(), t_size=24, t_font="hylia",
                               left=int(WIDTH / 2) - 150, top=10, width=300, height=50)
            b_quitgame = TextButton(parent=self.SCREEN, text="Quit Game", left=menu_left, top=menu_top, width=cwid)
            b_travel = TextButton(parent=self.SCREEN, text="Travel", left=menu_left, top=menu_top - B_HEIGHT - 10,
                                  width=cwid)
            b_move = TextButton(parent=self.SCREEN, text="Move", left=menu_left - offs, top=menu_top, width=cwid)
            b_roll = TextButton(parent=self.SCREEN, text="Roll", left=menu_left - offs, top=menu_top - B_HEIGHT - 10,
                                width=cwid)

            # ==================================
            # Player Buttons
            # ==================================
            p_top = 10
            exp_buttons = list()
            for index, player in enumerate(PLAYERS):
                if index == player_index:
                    exp_buttons.append(
                        TextButton(parent=self.SCREEN, text=player.get_name(), t_size=20, t_font="nodesto",
                                   left=10, top=p_top, width=cwid, t_color=(241, 194, 50)))
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
                if b_move.rect.collidepoint(mouse):
                    change_enc(1)
                    return
                if b_roll.rect.collidepoint(mouse):
                    self.dice_prompt()
                for index, button in enumerate(exp_buttons):
                    if button.rect.collidepoint(mouse):
                        player_index = index

            self.end_page()

    def page_credits(self):
        while True:
            self.SCREEN.fill(BLACK)

            tb_title = TextBox(parent=self.SCREEN, text="AutoCamp Team", t_font="hylia", t_size=30,
                               top=50, center=True)
            tb_member1 = TextBox(parent=self.SCREEN, text="Nader Atout", t_font="hylia", t_size=20, center=True,
                                 top=tb_title.textbox.top + tb_title.textbox.height)
            tb_member2 = TextBox(parent=self.SCREEN, text="Diana Penalba", t_font="hylia", t_size=20, center=True,
                                 top=tb_member1.textbox.top + tb_member1.textbox.height)
            tb_member3 = TextBox(parent=self.SCREEN, text="Adrian Gavrila", t_font="hylia", t_size=20, center=True,
                                 top=tb_member2.textbox.top + tb_member2.textbox.height)

            tb_advisor = TextBox(parent=self.SCREEN, text="Team Advisor", t_font="hylia", t_size=30, center=True,
                                 top=tb_member3.textbox.top + tb_member3.textbox.height + 30)
            tb_advname = TextBox(parent=self.SCREEN, text="Asst. Prof. Salma Elmalaki", t_font="hylia", t_size=20,
                                 center=True, top=tb_advisor.textbox.top + tb_advisor.textbox.height)

            tb_game = TextBox(parent=self.SCREEN, text="Original Tabletop Game", t_font="hylia", t_size=30,
                              center=True, top=tb_advname.textbox.top + tb_advname.textbox.height + 30)
            tb_wizards = TextBox(parent=self.SCREEN, text="Wizards of the Coast", t_font="hylia", t_size=20,
                                 center=True, top=tb_game.textbox.top + tb_game.textbox.height)

            b_back = TextButton(parent=self.SCREEN, path="./assets/b_credits.png", text="Back", left=B_CENTER,
                                top=B_YPOS + 50, width=B_WIDTH, height=B_HEIGHT)

            if b_back.rect.collidepoint(pygame.mouse.get_pos()) and self.CLICK:
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
                            result = str(self.CURRENT_ENCOUNTER.rollDice(int(num_dice), int(diceface), print_results=False))
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
                            result = str(self.CURRENT_ENCOUNTER.rollDice(int(num_dice), int(diceface),
                                                                         print_results=False, set_form=True))
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

