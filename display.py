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
    BLUE = (0, 35, 220)
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
        if (new_state == "intro"):
            self.game_intro()
        elif (new_state == "credits"):
            self.game_credits("intro")

    def font_hylia(self, size):
        return pygame.font.Font('./fonts/HyliaSerif.otf', size)

    def font_scaly(self, size):
        return pygame.font.Font('./fonts/Scaly Sans.otf', size)

    def game_credits(self, prev_state):
        credits = True
        back_button = pygame.Rect(300, 350, 100, 50)

        while credits:
            mx, my = pygame.mouse.get_pos()
            self.gameDisplay.fill(self.BLACK)

            CredSurf, CredRect = self.text_objects("AutoCamp Team: Nader Atout, Diana Penalba, Adrian Gavrila", self.font_hylia(20), self.WHITE)
            CredRect.center = ((self.WIDTH / 2), (self.HEIGHT / 2))

            pygame.draw.rect(self.gameDisplay, (self.BLUE), back_button)
            BackSurf, BackRect = self.text_objects("Back", self.font_hylia(20), self.BLACK)
            BackRect.center = (350, 380)

            self.gameDisplay.blit(CredSurf, CredRect)
            self.gameDisplay.blit(BackSurf, BackRect)

            if back_button.collidepoint((mx, my)):
                if self.CLICK:
                    credits = False

            self.CLICK = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    credits = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.CLICK = True

            self.clock.tick(15)

            pygame.display.update()

    def game_intro(self):
        intro = True
        change_state = False
        new_state = ""
        start_button = pygame.Rect(100, 330, 100, 50)
        quit_button = pygame.Rect(600, 330, 100, 50)
        credit_button = pygame.Rect(350, 330, 100, 50)

        while intro:
            self.gameDisplay.fill(self.WHITE)

            TextSurf, TextRect = self.text_objects("Welcome to AutoCamp!", self.font_hylia(60), self.BLACK)
            TextRect.center = ((self.WIDTH / 2), (self.HEIGHT / 2))

            pygame.draw.rect(self.gameDisplay, (self.BLUE), start_button)
            StartSurf, StartRect = self.text_objects("Start!!", self.font_scaly(20), self.BLACK)
            StartRect.center = (150, 355)

            pygame.draw.rect(self.gameDisplay, (self.RED), quit_button)
            QuitSurf, QuitRect = self.text_objects("Leave? D:", self.font_scaly(20), self.BLACK)
            QuitRect.center = (650, 355)

            pygame.draw.rect(self.gameDisplay, (self.GREEN), credit_button)
            CredSurf, CredRect = self.text_objects("Credits", self.font_scaly(20), self.BLACK)
            CredRect.center = (400, 355)

            mx, my = pygame.mouse.get_pos()
            if start_button.collidepoint((mx, my)):
                if self.CLICK:
                    break
            if quit_button.collidepoint((mx, my)):
                if self.CLICK:
                    sys.exit()
            if credit_button.collidepoint((mx, my)):
                if self.CLICK:
                    change_state = True
                    new_state = "credits"

            self.CLICK = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.CLICK = True

            self.gameDisplay.blit(TextSurf, TextRect)
            self.gameDisplay.blit(StartSurf, StartRect)
            self.gameDisplay.blit(QuitSurf, QuitRect)
            self.gameDisplay.blit(CredSurf, CredRect)
            pygame.display.update()
            self.clock.tick(15)

            # if (intro == False):
            #     pygame.quit()
            #     sys.exit()
            if (change_state == True):
                self.change_state(new_state)

            change_state = False
            new_state = ""

        pygame.quit()