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
    if ENCOUNTERS[ENCOUNTER_INDEX].is_combat:
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

        self.t_size, self.t_color = t_size, t_color
        self.t_font = use_font(size=t_size, font=t_font)

        self.box = load_image(path, width, height)

        self.rect = pygame.Rect(left, top, width, height)

        self.text, self.textbox = text_objects(text, self.t_font, t_color)
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
        while True:

            # Graphics Generation
            # ==================================
            self.SCREEN.blit(self.BG_STARTUP, ORIGIN)
            b_start = TextButton(parent=self.SCREEN, text="Start", left=B_CENTER, top=B_YPOS - (2 * B_HEIGHT), width=B_WIDTH, height=B_HEIGHT)
            b_credits = TextButton(parent=self.SCREEN, text="Credits", left=B_CENTER, top=B_YPOS - B_HEIGHT, width=B_WIDTH, height=B_HEIGHT)
            b_quit = TextButton(parent=self.SCREEN, text="Exit", left=B_CENTER, top=B_YPOS, width=B_WIDTH, height=B_HEIGHT)
            b_encmode = TextButton(parent=self.SCREEN, text=MODE, left=int(WIDTH * 0.75), top=B_YPOS - B_HEIGHT, width=int(B_WIDTH/2), height=B_HEIGHT)

            # Button Functions
            # ==================================
            mouse = pygame.mouse.get_pos()
            if b_start.rect.collidepoint(mouse) and self.CLICK:
                self.CLICK = False
                if MODE == "Battle":
                    self.page_map()
                elif MODE == "Explore":
                    self.page_explore()
            elif b_quit.rect.collidepoint(mouse) and self.CLICK:
                # save()
                sys.exit()
            elif b_credits.rect.collidepoint(mouse) and self.CLICK:
                self.CLICK = False
                self.page_credits()
            elif b_encmode.rect.collidepoint(mouse) and self.CLICK:
                self.CLICK = False
                if ENCOUNTER_INDEX == 1:
                    change_enc(2)
                elif ENCOUNTER_INDEX == 2:
                    change_enc(1)

            # Click Event Monitor
            # ==================================
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.CLICK = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.CLICK = False

            # ico = pygame.transform.scale(self.ICON, (B_HEIGHT, B_HEIGHT))
            # ltest = [ico, t_start]
            # for item in ltest:
            #     if item == ico:
            #         self.SCREEN.blit(item, (start_button.left - B_HEIGHT/2 + start_button.width / 2, start_button.top))
            #     else:
            #         self.SCREEN.blit(item, r_start)
            # self.SCREEN.blit(t_credits, r_credits)

            pygame.display.update()
            self.CLK.tick(15)

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

        while True:
            self.SCREEN.fill(DIRT)
            # self.SCREEN.blit(load_image("./assets/button.png", 800, 480), ORIGIN)
            tile_coors = "Tile: "
            if x >= 0 and y >= 0:
                tile_coors += "(" + str(x) + ", " + str(y) + ")"

            tb_coors = TextBox(parent=self.SCREEN, text=tile_coors,
                               left=(MAP_MAX_X * TILE_SIZE) + 20, top=int(HEIGHT/2))
            b_quitgame = TextButton(parent=self.SCREEN, text="Quit Game", left=(MAP_MAX_X * TILE_SIZE) + 20,
                                    top=int(0.8 * HEIGHT))

            r_test = pygame.Rect((MAP_MAX_X * TILE_SIZE) + 20, int(0.2 * HEIGHT), 50, 50)
            pygame.draw.rect(self.SCREEN, (0, 0, 0, 0), r_test)

            for tile in tile_list:
                tile[0] = TileButton(parent=self.SCREEN, left=tile[1][0], top=tile[1][1], color=DIRT)

            mouse = pygame.mouse.get_pos()
            if b_quitgame.rect.collidepoint(mouse) and self.CLICK:
                self.prompt_quit()
                return
            if mouse[0] <= (MAP_MAX_Y + 1) * TILE_SIZE and self.CLICK:
                x = int(mouse[0] / TILE_SIZE)
                y = int(mouse[1] / TILE_SIZE)

            # Click Event Monitor
            # ==================================
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.CLICK = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.CLICK = False

            pygame.display.update()
            self.CLK.tick(15)

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

            # Click Event Monitor
            # ==================================
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.CLICK = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.CLICK = False

            pygame.display.update()
            self.CLK.tick(15)

    def page_explore(self):
        while True:
            self.SCREEN.blit(self.BG_TAVERN, ORIGIN)
            b_quitgame = TextButton(parent=self.SCREEN, text="Quit Game", left=(MAP_MAX_X * TILE_SIZE) + 20,
                                    top=int(0.8 * HEIGHT))

            mouse = pygame.mouse.get_pos()
            if b_quitgame.rect.collidepoint(mouse) and self.CLICK:
                self.prompt_quit()
                return

            # Click Event Monitor
            # ==================================
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.CLICK = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.CLICK = False

            pygame.display.update()
            self.CLK.tick(15)

    def prompt_quit(self):
        width, height = 200, 100
        t_font = use_font(size=20, font="scaly")
        rect = pygame.Rect(B_CENTER, int(HEIGHT * 0.33), width, height)

        while True:
            quit_box = QuitBox(self.SCREEN, width, height, t_font, rect)
            b_yes = TextButton(parent=self.SCREEN, text="Yes", left=rect.center[0]-50, top=rect.center[1]+10, width=50, height=30)
            b_no = TextButton(parent=self.SCREEN, text="No", left=rect.center[0], top=rect.center[1]+10, width=50, height=30)

            mouse = pygame.mouse.get_pos()
            if b_yes.rect.collidepoint(mouse) and self.CLICK:
                self.CLICK = False
                save()
                return
            if b_no.rect.collidepoint(mouse) and self.CLICK:
                self.CLICK = False
                return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.CLICK = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.CLICK = False

            pygame.display.update()
            self.CLK.tick(15)





