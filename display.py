import pygame
import random
import time
from os import environ
import sys
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


# test comment
class Display:
    pygame.init()
    WIDTH = 800             # Use 16x16 sprites & tiles. Makes 50x30 grid.
    HEIGHT = 480
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (115, 215, 255)
    CLICK = False
    ICON = pygame.image.load('./assets/autocamp_icon.png')

    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_icon(ICON)
    pygame.display.set_caption('AutoCamp')
    clock = pygame.time.Clock()

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def change_state(self, new_state):
        if new_state == "intro":
            self.page_startup()
        elif new_state == "credits":
            self.page_credits("intro")

    def font_hylia(self, size):
        return pygame.font.Font('./fonts/HyliaSerif.otf', size)

    def font_scaly(self, size):
        return pygame.font.Font('./fonts/Scaly Sans.otf', size)

    def font_nodesto(self, size):
        return pygame.font.Font('./fonts/Nodesto Caps Condensed.otf', size)

    def page_credits(self, prev_state):
        back_button = pygame.Rect(300, 350, 100, 50)

        while True:
            self.gameDisplay.fill(self.BLACK)

            t_credits, r_credits = self.text_objects("AutoCamp Team: Nader Atout, Diana Penalba, Adrian Gavrila", self.font_hylia(20), self.WHITE)
            r_credits.center = ((self.WIDTH / 2), (self.HEIGHT / 2))

            pygame.draw.rect(self.gameDisplay, self.BLUE, back_button)
            t_back, r_back = self.text_objects("Back", self.font_hylia(20), self.BLACK)
            r_back.center = (350, 380)

            self.gameDisplay.blit(t_credits, r_credits)
            self.gameDisplay.blit(t_back, r_back)

            if back_button.collidepoint(pygame.mouse.get_pos()) and self.CLICK:
                self.CLICK = False
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.CLICK = True

            self.clock.tick(15)
            pygame.display.update()

    def page_startup(self):
        B_WIDTH = 200
        B_HEIGHT = 50
        B_CENTER = 300
        B_YPOS = 330

        start_button = pygame.Rect(B_CENTER, B_YPOS - (2 * B_HEIGHT), B_WIDTH, B_HEIGHT)
        credit_button = pygame.Rect(B_CENTER, B_YPOS - B_HEIGHT, B_WIDTH, B_HEIGHT)
        quit_button = pygame.Rect(B_CENTER, B_YPOS, B_WIDTH, B_HEIGHT)

        while True:
            self.gameDisplay.fill(self.WHITE)

            t_title, r_title = self.text_objects("Dungeons & Dragons", self.font_hylia(60), self.BLACK)
            r_title.center = (self.WIDTH / 2, self.HEIGHT / 4)

            pygame.draw.rect(self.gameDisplay, self.BLACK, start_button)
            t_start, r_start = self.text_objects("Start", self.font_scaly(20), self.WHITE)
            r_start.center = (start_button.left + B_WIDTH/2, start_button.top + B_HEIGHT/2)

            pygame.draw.rect(self.gameDisplay, self.BLACK, credit_button)
            t_credits, r_credits = self.text_objects("Credits", self.font_scaly(20), self.WHITE)
            r_credits.center = (credit_button.left + B_WIDTH/2, credit_button.top + B_HEIGHT/2)

            pygame.draw.rect(self.gameDisplay, self.BLACK, quit_button)
            t_quit, r_quit = self.text_objects("Exit", self.font_scaly(20), self.WHITE)
            r_quit.center = (quit_button.left + B_WIDTH / 2, quit_button.top + B_HEIGHT / 2)

            # mx, my = pygame.mouse.get_pos()
            if start_button.collidepoint(pygame.mouse.get_pos()) and self.CLICK:
                break
            if quit_button.collidepoint(pygame.mouse.get_pos()) and self.CLICK:
                sys.exit()
            if credit_button.collidepoint(pygame.mouse.get_pos()) and self.CLICK:
                self.CLICK = False
                self.change_state("credits")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.CLICK = True

            ico = pygame.transform.scale(self.ICON, (B_HEIGHT, B_HEIGHT))
            ltest = [ico, t_start]
            self.gameDisplay.blit(t_title, r_title)
            for item in ltest:
                if item == ico:
                    self.gameDisplay.blit(item, (start_button.left - B_HEIGHT/2 + start_button.width / 2, start_button.top))
                else: self.gameDisplay.blit(item, r_start)
            self.gameDisplay.blit(t_quit, r_quit)
            self.gameDisplay.blit(t_credits, r_credits)

            pygame.display.update()
            self.clock.tick(15)

        pygame.quit()
