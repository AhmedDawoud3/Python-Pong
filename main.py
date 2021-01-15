import pygame
import random
import sys
from pygame.locals import *
import math
import random
WINDOWS_WIDTH = 1280
WINDOWS_HEIGHT = 720

PADDLE_SPEED = 800

pygame.init()
smallFont = pygame.font.Font('font.TTF', 27)

scoreFont = pygame.font.Font('font.TTF', 108)

player1Score = 0
player2Score = 0

player1Y = 30
player2Y = WINDOWS_HEIGHT - 120

pressed_S = False
pressed_W = False

pressed_UP = False
pressed_DOWN = False

ballX = WINDOWS_WIDTH / 2 - 6
ballY = WINDOWS_HEIGHT / 2 - 6

ballDX = random.choice([-350, 350])
ballDY = random.randint(-250, 250)


PADDLE_SIZEX = 15
PADDLE_SIZEY = 80


clock = pygame.time.Clock()

gameState = 'start'


class Pong():
    def __init__(self):
        global gameState
        windowSurface = pygame.display.set_mode(
            (WINDOWS_WIDTH, WINDOWS_HEIGHT))
        pygame.display.set_caption('Pong')

        # Hello
        text = smallFont.render('Hello Pong!', True, (255, 255, 255), 0)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery - 250

        windowSurface.blit(text, textRect)

        # Player One Score
        text = scoreFont.render(str(player1Score), True, (255, 255, 255), 0)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx - 120
        textRect.centery = windowSurface.get_rect().centery - 120

        windowSurface.blit(text, textRect)

        # Player Two Score
        text = scoreFont.render(str(player2Score), True, (255, 255, 255), 0)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx + 120
        textRect.centery = windowSurface.get_rect().centery - 120

        windowSurface.blit(text, textRect)

        if gameState == 'start':
            text = smallFont.render("Start State", True, (255, 255, 255), 1)
            textRect = text.get_rect()
            textRect.centerx = windowSurface.get_rect().centerx
            textRect.centery = windowSurface.get_rect().centery - 200
            windowSurface.blit(text, textRect)
        elif gameState == 'play':
            text = smallFont.render("Play State", True, (255, 255, 255), 1)
            textRect = text.get_rect()
            textRect.centerx = windowSurface.get_rect().centerx
            textRect.centery = windowSurface.get_rect().centery - 200
            windowSurface.blit(text, textRect)

        # Player 1
        Player1 = pygame.draw.rect(windowSurface, (255, 255, 255),
                                   pygame.Rect(15, player1Y, PADDLE_SIZEX, PADDLE_SIZEY))

        # Player 2
        pygame.draw.rect(windowSurface, (255, 255, 255),
                         pygame.Rect(1250, player2Y, PADDLE_SIZEX, PADDLE_SIZEY))

        # Ball
        pygame.draw.rect(windowSurface, (255, 255, 255),
                         pygame.Rect(ballX, ballY, 12, 12))

        pygame.display.update()

    def play(self):
        global player1Y
        global player2Y

        global pressed_S
        global pressed_W
        global pressed_UP
        global pressed_DOWN

        global ballX
        global ballY
        global ballDX
        global ballDY

        global gameState
        dt = 1/clock.tick(30)
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
                        ballX = WINDOWS_WIDTH / 2 - 6
                        ballY = WINDOWS_HEIGHT / 2 - 6

                        ballDX = random.choice([-350, 350])
                        ballDY = random.randint(-250, 250)
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

        if pressed_S:
            player1Y = min(WINDOWS_HEIGHT - PADDLE_SIZEY,
                           player1Y + PADDLE_SPEED*dt)
        elif pressed_W:
            player1Y = max(0, player1Y - PADDLE_SPEED*dt)
        if pressed_DOWN:
            player2Y = min(WINDOWS_HEIGHT - PADDLE_SIZEY,
                           player2Y + PADDLE_SPEED*dt)
        elif pressed_UP:
            player2Y = max(0, player2Y - PADDLE_SPEED*dt)

        if gameState == 'play':
            ballX = ballX + ballDX * dt
            ballY = ballY + ballDY * dt


while True:
    game = Pong()
    play = game.play()

    # for event in pygame.event.get():
    #     if event.type == QUIT:
pygame.quit()
# sys.exit()
