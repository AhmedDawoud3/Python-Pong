# Print Text with [x, y] (NORMAL AXIS) not "pygame axis"
import pygame
import random
import sys
from pygame.locals import *
import math
import random
from Ball import Ball
from Paddle import Paddle

pygame.init()
Defualt = pygame.font.Font('font.TTF', 27)
scoreFont = pygame.font.Font('font.TTF', 108)


class printTxt():
    def __init__(self, windowSurface, text, x, y,  font="Defualt", color=(255, 255, 255)):
        if font == "Defualt":
            text = Defualt.render(str(text), True, color, 0)
            textRect = text.get_rect()
            textRect.centerx = windowSurface.get_rect().centerx + x
            textRect.centery = windowSurface.get_rect().centery - y
            windowSurface.blit(text, textRect)
        elif font == "scoreFont":
            text = scoreFont.render(str(text), True, color, 0)
            textRect = text.get_rect()
            textRect.centerx = windowSurface.get_rect().centerx + x
            textRect.centery = windowSurface.get_rect().centery - y
            windowSurface.blit(text, textRect)
