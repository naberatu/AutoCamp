import random
import time
import pygame
from os import environ
import sys
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Screen Dimensions:
WIDTH = 800  # Use 16x16 sprites & tiles. Makes 50x30 grid.
HEIGHT = 480

# Map Dimensions:
MAP_MAX_X = 15
MAP_MAX_Y = 15

TILE_SIZE = int(HEIGHT / MAP_MAX_Y)      # Usually would be 32

# Base Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (115, 215, 255)
DIRT = (197, 145, 84)

# Button Dimensions:
B_WIDTH = 200
B_HEIGHT = 50
B_CENTER = 300
B_YPOS = 330


def font_hylia(size):
    return pygame.font.Font('./fonts/HyliaSerif.otf', size)


def font_scaly(size):
    return pygame.font.Font('./fonts/Scaly Sans.otf', size)


def font_nodesto(size):
    return pygame.font.Font('./fonts/Nodesto Caps Condensed.otf', size)


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


class TileButton:
    def __init__(self, parent=None, left=0, top=0, width=TILE_SIZE, height=TILE_SIZE, color=DIRT):
        self.color = color
        self.rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(parent, self.color, self.rect)

        IMAGE = pygame.image.load("./assets/grasstile.png").convert()
        IMAGE = pygame.transform.scale(IMAGE, (TILE_SIZE, TILE_SIZE))
        img_rect = IMAGE.get_rect()
        img_rect.center = self.rect.center

        parent.blit(IMAGE, img_rect)


class TextButton:
    def __init__(self, parent=None, text="test", t_size=20, t_color=WHITE, t_font="scaly",
                 left=0, top=0, width=100, height=50, color=BLACK):
        self.t_size, self.t_color = t_size, t_color
        self.color = color

        if t_font == "scaly":
            self.t_font = font_scaly(t_size)
        elif t_font == "hylia":
            self.t_font = font_hylia(t_size)
        elif t_font == "nodesto":
            self.t_font = font_nodesto(t_size)

        self.rect = pygame.Rect(left, top, width, height)

        self.text, self.textbox = text_objects(text, self.t_font, t_color)
        self.textbox.center = self.rect.center

        pygame.draw.rect(parent, color, self.rect)
        parent.blit(self.text, self.textbox)


class TextBox:
    def __init__(self, parent=None, center=False, text="test", t_size=20, t_color=WHITE, t_font="scaly", left=0, top=0):
        self.t_size, self.t_color = t_size, t_color

        if t_font == "scaly":
            self.t_font = font_scaly(t_size)
        elif t_font == "hylia":
            self.t_font = font_hylia(t_size)
        elif t_font == "nodesto":
            self.t_font = font_nodesto(t_size)

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

    CLICK = False
    ICON = pygame.image.load('./assets/autocamp_icon.png')

    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_icon(ICON)
    pygame.display.set_caption('AutoCamp')
    clock = pygame.time.Clock()

    def change_state(self, new_state):
        if new_state == "intro":
            self.page_startup()
        elif new_state == "credits":
            self.page_credits("intro")

    def page_startup(self):
        while True:
            self.gameDisplay.fill(WHITE)
            b_start = TextButton(parent=self.gameDisplay, text="Start", left=B_CENTER, top=B_YPOS - (2 * B_HEIGHT), width=B_WIDTH, height=B_HEIGHT)
            b_credits = TextButton(parent=self.gameDisplay, text="Credits", left=B_CENTER, top=B_YPOS - B_HEIGHT, width=B_WIDTH, height=B_HEIGHT)
            b_quit = TextButton(parent=self.gameDisplay, text="Exit", left=B_CENTER, top=B_YPOS, width=B_WIDTH, height=B_HEIGHT)

            t_title, r_title = text_objects("Dungeons & Dragons", font_hylia(60), BLACK)
            r_title.center = (WIDTH / 2, HEIGHT / 4)
            self.gameDisplay.blit(t_title, r_title)

            # Button Functions
            # ==================================
            mouse = pygame.mouse.get_pos()
            if b_start.rect.collidepoint(mouse) and self.CLICK:
                self.page_map()
            elif b_quit.rect.collidepoint(mouse) and self.CLICK:
                sys.exit()
            elif b_credits.rect.collidepoint(mouse) and self.CLICK:
                self.CLICK = False
                self.change_state("credits")

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
            #         self.gameDisplay.blit(item, (start_button.left - B_HEIGHT/2 + start_button.width / 2, start_button.top))
            #     else:
            #         self.gameDisplay.blit(item, r_start)
            # self.gameDisplay.blit(t_credits, r_credits)

            pygame.display.update()
            self.clock.tick(15)

        pygame.quit()

    def page_map(self):
        tile_list = list()
        x, y = 0, 0
        for y_tile in range(MAP_MAX_Y):
            y = int(TILE_SIZE * y_tile)
            for x_tile in range(MAP_MAX_X):
                x = int(TILE_SIZE * x_tile)
                b_tile = TileButton(parent=self.gameDisplay, left=x, top=y, color=DIRT)
                tile_list.append([b_tile, (x, y)])

        while True:
            self.gameDisplay.fill(DIRT)

            b_quitgame = TextButton(parent=self.gameDisplay, text="Quit Game", left=(MAP_MAX_X * TILE_SIZE) + 20)

            for tile in tile_list:
                tile[0] = TileButton(parent=self.gameDisplay, left=tile[1][0], top=tile[1][1], color=DIRT)


            mouse = pygame.mouse.get_pos()
            if b_quitgame.rect.collidepoint(mouse) and self.CLICK:
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
            self.clock.tick(15)

    def page_credits(self, prev_state):
        while True:
            self.gameDisplay.fill(BLACK)

            tb_title = TextBox(parent=self.gameDisplay, text="AutoCamp Team", t_font="hylia", t_size=30,
                               top=50, center=True)
            tb_member1 = TextBox(parent=self.gameDisplay, text="Nader Atout", t_font="hylia", t_size=20, center=True,
                                 top=tb_title.textbox.top + tb_title.textbox.height)
            tb_member2 = TextBox(parent=self.gameDisplay, text="Diana Penalba", t_font="hylia", t_size=20, center=True,
                                 top=tb_member1.textbox.top + tb_member1.textbox.height)
            tb_member3 = TextBox(parent=self.gameDisplay, text="Adrian Gavrila", t_font="hylia", t_size=20, center=True,
                                 top=tb_member2.textbox.top + tb_member2.textbox.height)

            tb_advisor = TextBox(parent=self.gameDisplay, text="Team Advisor", t_font="hylia", t_size=30, center=True,
                                 top=tb_member3.textbox.top + tb_member3.textbox.height + 30)
            tb_advname = TextBox(parent=self.gameDisplay, text="Asst. Prof. Salma Elmalaki", t_font="hylia", t_size=20,
                                 center=True, top=tb_advisor.textbox.top + tb_advisor.textbox.height)

            tb_game = TextBox(parent=self.gameDisplay, text="Original Tabletop Game", t_font="hylia", t_size=30,
                              center=True, top=tb_advname.textbox.top + tb_advname.textbox.height + 30)
            tb_wizards = TextBox(parent=self.gameDisplay, text="Wizards of the Coast", t_font="hylia", t_size=20,
                                 center=True, top=tb_game.textbox.top + tb_game.textbox.height)

            b_back = TextButton(parent=self.gameDisplay, text="Back", left=B_CENTER, top=B_YPOS + 50, width=B_WIDTH,
                                height=B_HEIGHT, color=BLUE)

            if b_back.rect.collidepoint(pygame.mouse.get_pos()) and self.CLICK:
                # self.CLICK = False
                break

            # Click Event Monitor
            # ==================================
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.CLICK = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.CLICK = False

            self.clock.tick(15)
            pygame.display.update()







