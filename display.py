import random
import time
import pygame
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
                 left=0, top=0, width=100, height=50):

        self.t_size, self.t_color = t_size, t_color
        self.t_font = use_font(size=t_size, font=t_font)

        self.box = load_image(path, B_WIDTH, B_HEIGHT)

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
class Display():
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

            # Button Functions
            # ==================================
            mouse = pygame.mouse.get_pos()
            if b_start.rect.collidepoint(mouse) and self.CLICK:
                self.CLICK = False
                self.page_map()
            elif b_quit.rect.collidepoint(mouse) and self.CLICK:
                sys.exit()
            elif b_credits.rect.collidepoint(mouse) and self.CLICK:
                self.CLICK = False
                self.page_credits()

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

        # pygame.quit()

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
            b_quitgame = TextButton(parent=self.SCREEN, text="Quit Game",
                                    left=(MAP_MAX_X * TILE_SIZE) + 20, top=int(0.8 * HEIGHT))

            r_test = pygame.Rect((MAP_MAX_X * TILE_SIZE) + 20, int(0.2 * HEIGHT), 50, 50)
            pygame.draw.rect(self.SCREEN, (0, 0, 0, 0), r_test)

            for tile in tile_list:
                tile[0] = TileButton(parent=self.SCREEN, left=tile[1][0], top=tile[1][1], color=DIRT)

            mouse = pygame.mouse.get_pos()
            if b_quitgame.rect.collidepoint(mouse) and self.CLICK:
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

            self.CLK.tick(15)
            pygame.display.update()







