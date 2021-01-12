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

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('AutoCamp32')
    clock = pygame.time.Clock()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

    def game_intro(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    intro = False

            self.gameDisplay.fill(self.white)
            largeText = pygame.font.Font('freesansbold.ttf', 60)
            TextSurf, TextRect = self.text_objects("Welcome to AutoCamp!", largeText)
            TextRect.center = ((self.display_width / 2), (self.display_height / 2))
            self.gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            self.clock.tick(15)

            if (intro == False):
                pygame.quit()
