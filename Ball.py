import pygame
import random
import sys
from pygame.locals import *
import math
import random

WINDOWS_WIDTH = 1280
WINDOWS_HEIGHT = 720


class Ball():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.dx = random.choice([-70, 70])
        self.dy = random.randint(-150, 150)

    def collide(self, box):
        if self.x > box.x + box.width or self.x + self.width < box.x:
            return False
        if self.y > box.y + box.height or self.y + self.height < box.y:
            return False

        return True

    def reset(self):
        global WINDOWS_WIDTH
        global WINDOWS_HEIGHT
        self.x = WINDOWS_WIDTH / 2 - 6
        self.y = WINDOWS_HEIGHT / 2 - 6

        self.dx = random.choice([-70, 70])
        self.dy = random.randint(-150, 150)

    def update(self, dt):
        self.x = self.x + self.dx * dt
        self.y = self.y + self.dy * dt
        # print(dt)

    def render(self, windowSurface):
        # Ball
        pygame.draw.rect(windowSurface, (255, 255, 255),
                         pygame.Rect(self.x, self.y, 12, 12))
