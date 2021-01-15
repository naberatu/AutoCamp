import pygame
import random
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# test comment
class Display:
    pygame.init()
    display_width = 800             # Use 16x16 sprites & tiles. Makes 50x30 grid.
    display_height = 480
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    click = False

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('AutoCamp32')
    clock = pygame.time.Clock()

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def change_state(self, new_state):
        if (new_state == "intro"):
            self.game_intro()
        elif (new_state == "credits"):
            self.game_credits("intro")


    def game_credits(self, prev_state):

        credits = True
        back_button = pygame.Rect(300, 350, 100, 50)

        while credits:

            mx, my = pygame.mouse.get_pos()

            self.gameDisplay.fill(self.black)

            creditText = pygame.font.Font('freesansbold.ttf', 20)
            CredSurf, CredRect = self.text_objects("AutoCamp Team: Nader Atout, Diana Penalba, Adrian Gavrila", creditText, self.white)
            CredRect.center = ((self.display_width / 2), (self.display_height / 2))

            pygame.draw.rect(self.gameDisplay, (self.blue), back_button)
            BackText = pygame.font.Font('freesansbold.ttf', 20)
            BackSurf, BackRect = self.text_objects("Back", BackText, self.black)
            BackRect.center = (350, 380)

            self.gameDisplay.blit(CredSurf, CredRect)
            self.gameDisplay.blit(BackSurf, BackRect)

            if back_button.collidepoint((mx, my)):
                if self.click:
                    credits = False

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    credits = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

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

            self.gameDisplay.fill(self.white)

            largeText = pygame.font.Font('freesansbold.ttf', 60)
            TextSurf, TextRect = self.text_objects("Welcome to AutoCamp!", largeText, self.black)
            TextRect.center = ((self.display_width / 2), (self.display_height / 2))

            pygame.draw.rect(self.gameDisplay, (self.blue), start_button)
            StartText = pygame.font.Font('freesansbold.ttf', 20)
            StartSurf, StartRect = self.text_objects("Start!!", StartText, self.black)
            StartRect.center = (150, 355)

            pygame.draw.rect(self.gameDisplay, (self.red), quit_button)
            QuitText = pygame.font.Font('freesansbold.ttf', 20)
            QuitSurf, QuitRect = self.text_objects("Leave? D:", QuitText, self.black)
            QuitRect.center = (650, 355)

            pygame.draw.rect(self.gameDisplay, (self.green), credit_button)
            CredText = pygame.font.Font('freesansbold.ttf', 20)
            CredSurf, CredRect = self.text_objects("Credits", CredText, self.black)
            CredRect.center = (400, 355)

            mx, my = pygame.mouse.get_pos()
            if start_button.collidepoint((mx, my)):
                if self.click:
                    intro = False
            if quit_button.collidepoint((mx, my)):
                if self.click:
                    intro = False
            if credit_button.collidepoint((mx, my)):
                if self.click:
                    change_state = True
                    new_state = "credits"

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            self.gameDisplay.blit(TextSurf, TextRect)
            self.gameDisplay.blit(StartSurf, StartRect)
            self.gameDisplay.blit(QuitSurf, QuitRect)
            self.gameDisplay.blit(CredSurf, CredRect)
            pygame.display.update()
            self.clock.tick(15)

            if (intro == False):
                pygame.quit()
            elif (change_state == True):
                self.change_state(new_state)

            change_state = False
            new_state = ""
