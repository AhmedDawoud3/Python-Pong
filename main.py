import pygame
import random
import sys
from pygame.locals import *

WINDOWS_WIDTH = 1280
WINDOWS_HEIGHT = 720

pygame.init()
font = pygame.font.Font('font.TTF', 25)
windowSurface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
# windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

# set up the text
text = font.render('Hello world!', True, (255, 255, 255), 0)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the text onto the surface
windowSurface.blit(text, textRect)

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
