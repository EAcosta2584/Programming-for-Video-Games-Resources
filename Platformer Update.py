#################################################
# File Name: Platformer Update.py
# Creator Name: Mr. Acosta
# Date Created: 3-17-2020
# Date Modified: 4-14-2020
#################################################
#
#################################################

import pygame, sys, time, random
from pygame.locals import *
from PlatformerSettings import *

# pygame window setup
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption(gameTitle)

# Player default movement setup
moveLeft = False
moveRight = False
jump = False

# Player setup
player = pygame.Rect(width/2-20, 160, 20, 40)
# Player position Y setup
posY = height - 20

# Platform setup
platform0 = pygame.Rect(0, height - 20, width, platH)
platform1 = pygame.Rect(200, 400, 100, platH)
platform2 = pygame.Rect(350, 325, 50, platH)
platform3 = pygame.Rect(150, 250, 100, platH)
platform4 = pygame.Rect(0, 200, 100, platH)
platform5 = pygame.Rect(200, 150, 100, platH)
platform6 = pygame.Rect(300, 70, 100, platH)
platform7 = pygame.Rect(150, 25, 100, platH)
platformList = [platform0, platform1, platform2, platform3, platform4, platform5, platform6, platform7]

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
    if moveLeft == True:
        player.left -= moveX
        if player.left < 0:
            player.left = width
    if moveRight == True:
        player.right += moveX
        if player.right > width:
            player.right = 0

    # Y position of the player is updated with the Y movement
    posY += moveY + (.5 * gravity)
    player.bottom = posY

    # Checks for a collision with all platforms in the list and returns the index of the collision
    colliPos = player.collidelist(platformList)

    # if the player is falling, they can land on a platformPlatformer.py
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
            player.bottom = posY
            moveY = 0
    # if the player is jumping, they can't phase through the platform
    elif moveY < 0:
        if colliPos > -1:
            posY = platformList[colliPos].bottom + 40
            player.bottom = posY
            moveY += gravity
            jump = False


    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, red, player)


    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)
