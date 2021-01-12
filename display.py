import pygame
import random
import time

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

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

    def game_intro(self):
        intro = True
        start_button = pygame.Rect(100, 330, 100, 50)
        quit_button = pygame.Rect(600, 330, 100, 50)

        while intro:

            self.gameDisplay.fill(self.white)

            largeText = pygame.font.Font('freesansbold.ttf', 60)
            TextSurf, TextRect = self.text_objects("Welcome to AutoCamp!", largeText)
            TextRect.center = ((self.display_width / 2), (self.display_height / 2))

            pygame.draw.rect(self.gameDisplay, (self.blue), start_button)
            StartText = pygame.font.Font('freesansbold.ttf', 20)
            StartSurf, StartRect = self.text_objects("Start!!", StartText)
            StartRect.center = (150, 355)

            pygame.draw.rect(self.gameDisplay, (self.red), quit_button)
            QuitText = pygame.font.Font('freesansbold.ttf', 20)
            QuitSurf, QuitRect = self.text_objects("Leave? D:", QuitText)
            QuitRect.center = (650, 355)

            mx, my = pygame.mouse.get_pos()
            if start_button.collidepoint((mx, my)):
                if self.click:
                    intro = False
            if quit_button.collidepoint((mx, my)):
                if self.click:
                    intro = False

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
            pygame.display.update()
            self.clock.tick(15)

            if (intro == False):
                pygame.quit()
