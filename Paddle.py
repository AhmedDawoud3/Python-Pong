import pygame
import random
import sys
from pygame.locals import *
import math
import random

WINDOWS_WIDTH = 1280
WINDOWS_HEIGHT = 720

PADDLE_SPEED = 140

PADDLE_SIZEX = 15
PADDLE_SIZEY = 80


class Paddle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.dy = 0

    def update(self, dt):
        if self.dy < 0:
            self, y = max(0, self.y - PADDLE_SPEED * dt)
        elif self.dy > 0:
            self.y = min(WINDOWS_HEIGHT - self.y,
                         self.y + PADDLE_SPEED * dt)

    def render(self, surface):
        Player1 = pygame.draw.rect(surface, (255, 255, 255),
                                   pygame.Rect(self.x, self.y, PADDLE_SIZEX, PADDLE_SIZEY))

    def move(self, dt, direction):
        if direction == "down":
            self.y = min(WINDOWS_HEIGHT - PADDLE_SIZEY,
                         self.y + PADDLE_SPEED*dt)
        elif direction == "up":
            self.y = max(0, self.y - PADDLE_SPEED*dt)
