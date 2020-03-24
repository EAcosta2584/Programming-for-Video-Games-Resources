#################################################
# File Name: Platformer.py
# Creator Name: Mr. Acosta
# Date Created: 3-17-2020
# Date Modified: 3-19-2020
#################################################
# This program will create a single screen platformer
#################################################

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
player = pygame.Rect(0, 160, 20, 40)
# Player position Y setup
posY = height - 20

# Platform setup
platform0 = pygame.Rect(0, height - 20, width, 20)
platform1 = pygame.Rect(0, 200, 100, 20)
platform2 = pygame.Rect(150, 250, 100, 20)
platform3 = pygame.Rect(200, 400, 100, 20)
platform4 = pygame.Rect(350, 325, 100, 20)
platformList = [platform0, platform1, platform2, platform3, platform4]

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
        # The player may only jump if they are touching a platform
        if player.collidelist(platformList) > -1:
            moveY = -10
    if moveLeft == True and player.left > 0:
        player.left -= moveX
    if moveRight == True and player.right < width:
        player.right += moveX

    # Y position of the player is updated with the Y movement
    posY += moveY + (.5 * gravity)
    player.bottom = posY

    # Checks for a collision with all platforms in the list and returns the index of the collision
    colliPos = player.collidelist(platformList)

    # if the player is falling, they can land on a platform
    if moveY > 0:
        # if the player hits the side of a platform while falling, stop their horizontal movement by
        # keeping the player side and platform side the same.
        if moveRight and player.bottom > platformList[colliPos].centery:
            if colliPos > -1:
                jump = False
                moveRight = False
                if platformList[colliPos].left <= 0:
                    player.right = player.right
                else:
                    player.right = platformList[colliPos].left
        elif moveLeft and player.bottom > platformList[colliPos].centery:
            if colliPos > -1:
                jump = False
                moveLeft = False
                if platformList[colliPos].right >= width:
                    player.left = player.left
                else:
                    player.left = platformList[colliPos].right
        # if the index is greater that -1, the player must be touching ground, else, they are falling
        elif colliPos > -1:
            posY = platformList[colliPos].top + 1
            moveY = 0
    # if the player is jumping, they can't phase through the platform
    elif moveY < 0:
        if colliPos > -1:
            posY = platformList[colliPos].bottom + 40
            player.bottom = posY
            moveY += gravity
            jump = False

    # If the player falls off screen, lose a life
    # if player.top > height:
    #     lives -= 1
    #     player.center = (0, 160)

    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, red, player)

    # when out of lives, game over
    if lives <= 0:
        windowSurface.fill(black)

    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)