################################################
# File Name: UsingImages.py
# Creator Name: Mr. Acosta
# Date Created: 2-3-2020
# Date Modified: 2-3-2020
################################################
# This program will demonstrate using images
# ################################################

import pygame, sys, time, random
from pygame.locals import *

# Set up pygame. to run pygame, we must always initialize it.
pygame.init()
mainClock = pygame.time.Clock()

# Here we create the window. We store the window height and width in variables so we can use them later.
width = 600
height = 600
windowSurface = pygame.display.set_mode((width, height), 0, 32)

# Set the window title to "Animation"
pygame.display.set_caption('images')

movementSpeed = 3
projectileSpeed = 12

# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
grow = False
angle = 0
left = False
right = False
up = True
down = False

# Set up the color variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

x = 84
y = 72

player = pygame.Rect(300 - 42 , 300 - 36, x, y)
playerImage = pygame.image.load('dagger.gif')



while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_UP or event.key == K_w:
            moveUp = True
        if event.key == K_DOWN or event.key == K_s:
            moveDown = True
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = True
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = True
        if event.key == K_SPACE:
            grow = True
    if event.type == KEYUP:
        if event.key == K_UP or event.key == K_w:
            moveUp = False
        if event.key == K_DOWN or event.key == K_s:
            moveDown = False
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = False
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = False
        if event.key == K_SPACE:
            grow = False
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()



    # Draw the white background onto the surface.
    windowSurface.fill(white)

    playerImageStretch = pygame.transform.scale(playerImage, (x, y))

    # Draw the player onto the surface.
    windowSurface.blit(playerImageStretch, player)

    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)
