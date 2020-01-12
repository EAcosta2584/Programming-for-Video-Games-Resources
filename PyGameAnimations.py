################################################
# File Name:        PyGameAnimations
# Creator Name:     Mr. Acosta
# Date Created:     1-10-2020
# Date Modified:    1-10-2020
################################################
# This program will demonstrate moving shapes in
# PyGame
################################################

import pygame, sys, time
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window.
width = 600
height = 600
windowSurface = pygame.display.set_mode((width, height), 0, 32)
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

# Set up the colors.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

basicFont = pygame.font.SysFont("magneto", 20)

myText = "FBI Warning"

text = basicFont.render(myText,True, white, blue)

textRect = text.get_rect()

textRect.centerx  = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Set up the box data structure.
blueSquare = {'rect':pygame.Rect(275,275, 50, 50), 'color':blue, 'dir':upRight}
redRect = {'rect':pygame.Rect(230, 120, 50, 80), 'color': red, 'dir':downRight}
textBox =
boxes = [blueSquare, redRect]



# Run the game loop.
while True:
    # Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(white)

    if textRect.centerx > width:


    for b in boxes:
        # Move the box data structure.
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

        windowSurface.blit(text, textRect)

    # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(.02)
