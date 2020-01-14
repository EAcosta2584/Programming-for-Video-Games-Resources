################################################
# File Name:        KeyboardInputs.py
# Creator Name:     Mr. Acosta
# Date Created:     1-14-2020
# Date Modified:    1-14-2020
################################################
# This program will demonstrate moving shapes with
# key inputs
################################################

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
pygame.display.set_caption('KeyInputs')


# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

movementSpeed = 6


# Set up the color variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

player = pygame.Rect(300, 100, 50, 50)

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    # Draw the white background onto the surface.
    windowSurface.fill(white)


    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, black, player)



    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(60)