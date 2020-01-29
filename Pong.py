################################################
# File Name: Pong.py
# Creator Name: Mr. Acosta
# Date Created: 1-28-2020
# Date Modified: 1-28-2020
################################################
# Making Pong
#################################################

import pygame, sys, time, random
from pygame.locals import *

# Set up pygame. to run pygame, we must always initialize it.
pygame.init()
mainClock = pygame.time.Clock()

# Here we create the window. We store the window height and width in variables so we can use them later.
width = 700
height = 600
windowSurface = pygame.display.set_mode((width, height), 0, 32)

# Set the window title to "Pong"
pygame.display.set_caption('Pong')




# Set up the color variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if event.type == KEYDOWN:
        pass


    if event.type == KEYUP:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()



    # Draw the window onto the screen.
    pygame.display.update()

    # Set the framerate of the game.
    mainClock.tick(30)