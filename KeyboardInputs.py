################################################
# File Name: KeyboardInputs.py
# Creator Name: Mr. Acosta
# Date Created: 1-14-2020
# Date Modified: 1-15-2020
################################################
# This program will demonstrate moving shapes with # key inputs
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
pygame.display.set_caption('KeyInputs')


# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

shoot = False

movementSpeed = 3
projectileSpeed = 12


# Set up the color variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

player = pygame.Rect(250, 250, 50, 50)

shots = []
targets = []

#
for i in range(10):
    targets.append(pygame.Rect(60 * (i+1), 10, 20, 20))

    # Run the game loop.
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
            shoot = True
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
            shoot = False
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    # Set adjust our movement when a direction is True
    if moveUp == True:
        player.top -= movementSpeed
    if moveDown == True:
        player.bottom += movementSpeed
    if moveLeft == True:
        player.left -= movementSpeed
    if moveRight == True:
        player.right += movementSpeed

    # Draw the white background onto the surface.
    windowSurface.fill(white)

    # Add a projectile to the shots list, but limit to three shots at a time
    if shoot == True and (len(shots) < 3 ):
        shots.append(pygame.Rect(player.centerx - 5, player.centery - 5, 10, 10))



    # Draw the shots that have been added to the shots list, and move them up by projectile speed
    for i in range(len(shots)):
        pygame.draw.rect(windowSurface, blue, shots[i])
        shots[i].top -= projectileSpeed
        for target in targets[:]:
            if shots[i].colliderect(target):
                targets.remove(target)

    # If the shot passes the screen, remove it from the list.
    for shot in shots[:]:
        if shot.bottom < 0:
            shots.remove(shot)

    # Redraw our list of targets
    for i in range(len(targets)):
        pygame.draw.rect(windowSurface, red, targets[i])

    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, black, player)

    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)
