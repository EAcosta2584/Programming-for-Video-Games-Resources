################################################
# File Name: UsingImages.py
# Creator Name: Mr. Acosta
# Date Created: 2-3-2020
# Date Modified: 2-6-2020
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

# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
grow = False
shrink = False
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


# Image size
x = 84
y = 72

# Create a player the size of the image
player = pygame.Rect(300 - 42 , 300 - 36, x, y)

# Load in the image we are using.
playerImage = pygame.image.load('dagger.gif')

# The following image formats can be used with PyGame
# JPG
# PNG
# GIF (non-animated)
# BMP
# PCX
# TGA (uncompressed)
# TIF


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
        if event.key == K_z:
            shrink = True
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
        if event.key == K_z:
            shrink = False
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    # move the player up
    if moveUp == True:
        player.top -= movementSpeed

        # Here we check which direction the player is already facing, and rotate, or flip accordingly

        # This checks if our object's state is "left"
        if left == True:
            # The transform.rotate() function takes an image object and rotates it in degrees.
            # Note that positive is counter-clockwise, and negative is clockwise. The rotation is also relative
            # on its current position, not its original position.
            # pygame.transform.rotate(surface, degrees)
            playerImage = pygame.transform.rotate(playerImage, -90)
            # Here we tell the program we are no longer facing left
            left = False
        if right == True:
            playerImage = pygame.transform.rotate(playerImage, 90)
            right = False
        if down == True:
            # The transform.flip() function flips the image object about its horizontal and/or vertical axis
            # pygame.transform.flip(surface, xbool, ybool)
            playerImage = pygame.transform.flip(playerImage, False, True)
            down = False
        # Here we set the state to "up"
        up = True

    if moveDown == True:
        player.top += movementSpeed
        if left == True:
            playerImage = pygame.transform.rotate(playerImage, 90)
            left = False
        if right == True:
            playerImage = pygame.transform.rotate(playerImage, -90)
            right = False
        if up == True:
            playerImage = pygame.transform.flip(playerImage, False, True)
            up = False
        down = True

    if moveLeft == True:
        player.left -= movementSpeed
        if right == True:
            playerImage = pygame.transform.rotate(playerImage, 180)
            right = False
        if up == True:
            playerImage = pygame.transform.rotate(playerImage, 90)
            up = False
        if down == True:
            playerImage = pygame.transform.rotate(playerImage, -90)
            down = False
        left = True

    if moveRight == True:
        player.right += movementSpeed
        if left == True:
            playerImage = pygame.transform.rotate(playerImage, 180)
            left = False
        if up == True:
            playerImage = pygame.transform.rotate(playerImage, -90)
            up = False
        if down == True:
            playerImage = pygame.transform.rotate(playerImage, 90)
            down = False
        right = True

    # increase or decrease the X and Y values to scale the image
    if grow == True:
        x += 1
        y += 1

    if shrink == True:
        x -= 1
        y -= 1


    # Draw the white background onto the surface.
    windowSurface.fill(white)

    # The transform.scale takes an image object and adjusts its width (x in this example), and height (y in this example)
    # pygame.transform.scale(surface, (width, height))
    playerImageStretch = pygame.transform.scale(playerImage, (x, y))

    # Draw the image onto the player surface.
    windowSurface.blit(playerImageStretch, player)

    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)
