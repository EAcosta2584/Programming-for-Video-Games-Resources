################################################
# File Name: MouseInputs.py
# Creator Name: Mr. Acosta
# Date Created: 1-17-2020
# Date Modified: 1-17-2020
################################################
# This program will demonstrate moving shapes with
# mouse inputs
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
pygame.display.set_caption('MouseInputs')


# Set up the color variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

downShapes = []
upShapes = []

color = []
wheelColors = white

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == KEYUP:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()


    # Draw the white background onto the surface.
    windowSurface.fill(white)

    # if event.type == MOUSEBUTTONDOWN:
    #     downShapes.append(pygame.Rect((event.pos[0], event.pos[1], 25, 25)))
    #     color.append((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    if event.type == MOUSEBUTTONUP:
        if event.button == 1:
            upShapes.append(pygame.Rect((event.pos[0], event.pos[1], 25, 25)))
            color.append((random.randint(0,255), random.randint(0,255), random.randint(0,255)))



    for i in range(len(upShapes)):
        pygame.draw.rect(windowSurface, color[i], upShapes[i])

    # for i in range(len(downShapes)):
    #     pygame.draw.rect(windowSurface, color[i], downShapes[i])

    if event.type == MOUSEMOTION:
        pygame.draw.circle(windowSurface, red, (event.pos[0], event.pos[1]), 12)

    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)
