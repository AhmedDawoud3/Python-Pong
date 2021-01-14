import pygame
import random
import sys
from pygame.locals import *

WINDOWS_WIDTH = 1280
WINDOWS_HEIGHT = 720

pygame.init()
font = pygame.font.Font('font.TTF', 25)


class Pong():
    def __init__(self):
        windowSurface = pygame.display.set_mode(
            (WINDOWS_WIDTH, WINDOWS_HEIGHT))
        pygame.display.set_caption('Pong')

        text = font.render('Hello Pong!', True, (255, 255, 255), 0)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery

        windowSurface.blit(text, textRect)

        pygame.display.update()

    def play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()


game = Pong()
while True:
    play = game.play()

    # for event in pygame.event.get():
    #     if event.type == QUIT:
pygame.quit()
# sys.exit()
