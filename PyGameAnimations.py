################################################
# File Name:        PyGameAnimations
# Creator Name:     Mr. Acosta
# Date Created:     1-10-2020
# Date Modified:    1-14-2020
################################################
# This program will demonstrate moving shapes in
# PyGame
################################################

import pygame, sys, time
from pygame.locals import *

# Set up pygame. to run pygame, we must always initialize it.
pygame.init()

# Here we create the window. We store the window height and width in variables so we can use them later.
width = 600
height = 600
windowSurface = pygame.display.set_mode((width, height), 0, 32)

# Set the window title to "Animation"
pygame.display.set_caption('Animation')

# Set up direction variables.
up = 'up'
down = 'down'
left = 'left'
right = 'right'

downLeft = 'downleft'
downRight = 'downright'
upLeft = 'upleft'
upRight = 'upright'

movementSpeed = 4

# Set up the color variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Create up a font object.
basicFont = pygame.font.SysFont("Comic Sans MS", 20)

myText = "Hello"

text = basicFont.render(myText,True, white, black)


# Get the rectangle of the text and start it in the center of the window.
textRect = text.get_rect()
textRect.centerx  = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Set up the box data structure.
blueSquare = {'rect':pygame.Rect(275,275, 50, 50), 'color':blue, 'dir':upRight}
greenRect = {'rect':pygame.Rect(230, 120, 50, 80), 'color': green, 'dir':downRight}
textBox = {'rect': textRect, 'color': white, 'dir': upLeft}
boxes = [blueSquare, greenRect, textBox]

x = 30
circleMovement = 5

# Run the game loop.
while True:
    # Check for the QUIT (window close) event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(white)

    for b in boxes:
        # Move the box data structure base on its stored direction.
        if b['dir'] == downLeft:
            b['rect'].left -= movementSpeed
            b['rect'].top += movementSpeed
        if b['dir'] == downRight:
            b['rect'].left += movementSpeed
            b['rect'].top += movementSpeed
        if b['dir'] == upLeft:
            b['rect'].left -= movementSpeed
            b['rect'].top -= movementSpeed
        if b['dir'] == upRight:
            b['rect'].left += movementSpeed
            b['rect'].top -= movementSpeed

        #The conditionals below are used to check if we hit the edge of the screen.

        if b['rect'].right > width:
            if b['dir'] == upRight:
                b['dir'] = downLeft
            if b['dir'] == downRight:
                b['dir'] = upLeft

        if b['rect'].bottom > height:
            if b['dir'] == downLeft:
                b['dir'] = upRight
            if b['dir'] == downRight:
                b['dir'] = upLeft

        if b['rect'].top < 0:
            if b['dir'] == upLeft:
                b['dir'] = downLeft
            if b['dir'] == upRight:
                b['dir'] = downRight

        if b['rect'].left < 0:
            if b['dir'] == downLeft:
                b['dir'] = downRight
            if b['dir'] == upLeft:
                b['dir'] = upRight

        # Draw the box onto the surface.
        pygame.draw.rect(windowSurface, b['color'], b['rect'])


    # If the X location of the circle is a radius away from the right edge, reverse direction.
    if x == width -30:
        circleMovement = -5
    # If the X location of the circle is a radius away from the left edge, reverse direction.
    if x == 30:
        circleMovement = 5

    # Increase the circle's movement.
    x += circleMovement

    # Draw the circle on the screen.
    pygame.draw.circle(windowSurface, black, (x, 400), 30)

    # Draw the text onto the screen.
    windowSurface.blit(text, textRect)

    # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(.02)
