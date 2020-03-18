#################################################
# File Name: Platformer.py
# Creator Name: Mr. Acosta
# Date Created: 1-14-2020
# Date Modified: 1-15-2020
#################################################
# This program will create a single screen platformer
# ################################################

import pygame, sys, time, random
from pygame.locals import *

# pygame window setup
pygame.init()
mainClock = pygame.time.Clock()
width = 600
height = 500
windowSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Platformer')

# Setup the color variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Setup player variables.
lives = 3

# Player default movement setup
moveLeft = False
moveRight = False
jump = False

# Gravity and movement defaults
gravity = .5
moveX = 4
moveY = 0

# Player setup
player = pygame.Rect(width/2, 160, 20, 40)
# Player position Y setup
posY = 200

# Platform setup
platform0 = pygame.Rect(0, height - 20, width, 20)
platformList = [platform0]

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
            if event.key == K_SPACE or event.key == K_w:
                jump = True
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_SPACE or event.key == K_w:
                jump = False
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(white)

    # Draw the platforms
    for platform in platformList:
        pygame.draw.rect(windowSurface, green, platform)

    # Gravity is always added to Y movement until it hits an object
    moveY += gravity

    # Set our movement when a direction is True
    if jump == True:
        moveY = -10
    if moveLeft == True and player.left > 0:
        player.left -= moveX
    if moveRight == True and player.right < width:
        player.right += moveX

    # If the player falls off screen, bring them to the top
    if player.top > height:
        posY = 0

    # Y position of the player is updated with the Y movement
    posY += moveY + (.5 * gravity)
    player.bottom = posY

    print(posY)

    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, red, player)


    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)