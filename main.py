import pygame
import random
import sys
from pygame.locals import *
import math
from Ball import Ball
from Paddle import Paddle
from Text import printTxt

WINDOWS_WIDTH = 1280
WINDOWS_HEIGHT = 720

PADDLE_SPEED = 120

pygame.init()
smallFont = pygame.font.Font('font.TTF', 27)

scoreFont = pygame.font.Font('font.TTF', 108)

player1Score = 0
player2Score = 0

pressed_S = False
pressed_W = False

pressed_UP = False
pressed_DOWN = False


clock = pygame.time.Clock()

gameState = 'start'

dt = 1/clock.tick(30)

ball = Ball(WINDOWS_WIDTH / 2 - 6, WINDOWS_HEIGHT / 2 - 6,
            12, 12)

player1 = Paddle(15, 30, 15, 80)

player2 = Paddle(1250, WINDOWS_HEIGHT - 120, 15, 80)


class Pong():
    def __init__(self):

        global dt
        windowSurface = pygame.display.set_mode(
            (WINDOWS_WIDTH, WINDOWS_HEIGHT))

        # Hello Pong !
        printTxt(windowSurface, "Hello Pong!", 0, 250)

        # Player One Score
        printTxt(windowSurface, player1Score, 120, 120, "scoreFont")

        # Player Two Score
        printTxt(windowSurface, player2Score, -120, 120, "scoreFont")

        if gameState == 'start':
            printTxt(windowSurface, "Start State", 0, 200)
        elif gameState == 'play':
            printTxt(windowSurface, "Play State", 0, 200)

        player1.render(windowSurface)
        player2.render(windowSurface)
        Ball.render(ball, windowSurface)

        pygame.display.update()

    def play(self):
        global ball

        global pressed_S
        global pressed_W
        global pressed_UP
        global pressed_DOWN

        global gameState
        global dt
        # print(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_RETURN:
                    if gameState == 'start':
                        gameState = 'play'
                    elif gameState == 'play':
                        gameState = "start"
                        ball.reset()

                elif event.key == pygame.K_s:
                    pressed_S = True
                elif event.key == pygame.K_w:
                    pressed_W = True
                elif event.key == pygame.K_UP:
                    pressed_UP = True
                elif event.key == pygame.K_DOWN:
                    pressed_DOWN = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    pressed_S = False
                elif event.key == pygame.K_w:
                    pressed_W = False
                elif event.key == pygame.K_UP:
                    pressed_UP = False
                elif event.key == pygame.K_DOWN:
                    pressed_DOWN = False
        if ball.collide(player1):
            ball.dx = -ball.dx * random.choice([0.95, 1.05])
            ball.dy = ball.dy * random.choice([0.95, 1.05])

        if ball.collide(player2):
            ball.dx = - ball.dx * random.choice([0.95, 1.05])
            ball.dy = ball.dy * random.choice([0.95, 1.05])

        if ball.y >= WINDOWS_HEIGHT - 12:
            ball.dy = -ball.dy

        if ball.y <= 0:
            ball.dy = - ball.dy

        if pressed_S:
            player1.move(dt, "down")

        elif pressed_W:
            player1.move(dt, "up")
        if pressed_DOWN:
            player2.move(dt, "down")
        elif pressed_UP:
            player2.move(dt, "up")

        if gameState == 'play':
            ball.update(dt)

        player1.update(dt)
        player2.update(dt)


while True:
    game = Pong()
    play = game.play()


pygame.quit()
