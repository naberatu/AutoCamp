# import pygame
# import random
# import time
#
# # test comment
# pygame.init()
# display_width = 800             # Use 16x16 sprites & tiles. Makes 50x30 grid.
# display_height = 480
# black = (0, 0, 0)
# white = (255, 255, 255)
# red = (255, 0, 0)
#
# gameDisplay = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('AutoCamp32')
# clock = pygame.time.Clock()
#
# def text_objects(text, font):
#     textSurface = font.render(text, True, black)
#     return textSurface, textSurface.get_rect()
#
# def game_intro():
#     intro = True
#
#     while intro:
#         for event in pygame.event.get():
#             print(event)
#             if event.type == pygame.QUIT:
#                 quit()
#
#         gameDisplay.fill(white)
#         largeText = pygame.font.Font('freesansbold.ttf', 60)
#         TextSurf, TextRect = text_objects("Welcome to AutoCamp!", largeText)
#         TextRect.center = ((display_width / 2), (display_height / 2))
#         gameDisplay.blit(TextSurf, TextRect)
#         pygame.display.update()
#         clock.tick(15)
#
# game_intro()