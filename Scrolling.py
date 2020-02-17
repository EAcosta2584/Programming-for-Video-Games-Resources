################################################
# File Name: Scrolling.py
# Creator Name: Mr. Acosta
# Date Created: 2-9-2020
# Date Modified: 2-9-2020
#################################################
# This program will demonstrate scrolling backgrounds
#################################################

import pygame, sys, time, random
from pygame.locals import *

# Set up pygame. to run pygame, we must always initialize it.
pygame.init()
mainClock = pygame.time.Clock()

# Set a variable to run the game when True
running = True

# Here we create the window. We store the window height and width in variables so we can use them later.
width = 800
height = 600
windowSurface = pygame.display.set_mode((width, height), 0, 32)

# Set the window title to "Animation"
pygame.display.set_caption('scrolling')

#Movement Control
movementSpeed = 9
projectileSpeed = 10
scrollSpeed = 6

shotFrameCounter = 0
targetFrameCounter = 0
collisionFrameCounter = 0

shots = []
targets = []

maxLives = 3
score = 0

maxTargets = 5
maxShots = 10

# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
shoot = False

# Set up the color variables.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# Image size
x = 48
y = 54

# Create a player the size of the image
player = pygame.Rect(100, 300 - 27, x, y)
bg = pygame.Rect(0, -100, 10, 10)


# Load in the images we are using. Note that the background is in another folder
# so we must include the folder name when loading the image.
background = pygame.image.load('images/StarsPattern.png')
playerImage = pygame.image.load('dagger.gif')

# Our image is normally rotated 90 degrees up, so here we turn it to the right
playerImage = pygame.transform.rotate(playerImage, -90)


font = pygame.font.SysFont("none", 24)

def gameOver(score):
    font = pygame.font.SysFont("none", 90)
    myText = "Game Over"
    text = font.render(myText, True, white)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery - 100

    scoreText = "Final Score: " + str(score)
    text2 = font.render(scoreText, True, white)
    textRect2 = text2.get_rect()
    textRect2.centerx = windowSurface.get_rect().centerx
    textRect2.centery = windowSurface.get_rect().centery + 50

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

        # keep the background moving
        windowSurface.fill(black)
        windowSurface.blit(background, bg)
        bg.left -= scrollSpeed
        if bg.left < -800:
            bg.left = 0

        # Display game over text and score
        windowSurface.blit(text, (textRect))
        windowSurface.blit(text2, (textRect2))

        pygame.display.update()
        mainClock.tick(30)


# Run the game loop.
while running:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(black)

    # Draw the background image onto the bg surface.
    windowSurface.blit(background, bg)

    # Move the background to the left
    bg.left -= scrollSpeed

    # Before we run out of background, reset the left edge
    if bg.left < -800:
        bg.left = 0

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
        if player.top > 0:
            player.top -= movementSpeed
    if moveDown == True:
        if player.bottom < height:
            player.bottom += movementSpeed
    if moveLeft == True:
        if player.left > 0:
            player.left -= movementSpeed
    if moveRight == True:
        if player.right < width:
            player.right += movementSpeed

    # Random set targets on screen and spaces them so they won't overlap
    if len(targets) < maxTargets:
        if targetFrameCounter == 0:
            targetFrameCounter = 10
            targets.append(pygame.Rect(width + 20, random.randint(10, height -10), 20, 20))

    # Draw targets on screen
    for i in range (len(targets)):
        pygame.draw.rect(windowSurface, red, targets[i])
        targets[i].left -= movementSpeed
        if targets[i].colliderect(player):
            targets[i].right = 0
            if collisionFrameCounter == 0:
                collisionFrameCounter = 30
                maxLives -= 1

    # If hit, flash during invincibility
    if collisionFrameCounter > 0:
        if collisionFrameCounter % 3 == 0:
            playerImage.set_alpha(128)
        else:
            playerImage.set_alpha(256)
    else:
        playerImage.set_alpha(256)

    for target in targets[:]:
        if target.left < - 20:
            targets.remove(target)

    # Add a projectile to the shots list, but limit to three shots at a time
    if shoot == True and (len(shots) < maxShots):
        if shotFrameCounter == 0:
            shotFrameCounter = 6
            shots.append(pygame.Rect(player.centerx - 3, player.centery - 3, 6, 6))

    # Draw the shots that have been added to the shots list, and move them up by projectile speed
    for i in range(len(shots)):
        pygame.draw.rect(windowSurface, green, shots[i])
        shots[i].left += projectileSpeed
        for target in targets[:]:
            if shots[i].colliderect(target):
                shots[i].left = 800
                targets.remove(target)
                score += 1

    # If the shot passes the screen, remove it from the list.
    for shot in shots[:]:
        if shot.right > 820:
            shots.remove(shot)

    # Redraw our list of targets
    for i in range(len(targets)):
        pygame.draw.rect(windowSurface, red, targets[i])

    # Draw the player onto the surface.
    windowSurface.blit(playerImage, (player.left - 14, player.top - 16))

    #update lives
    livesText = "Lives: " + str(maxLives)
    text = font.render(livesText, True, white)
    windowSurface.blit(text, (0,0))

    #update Score
    scoreText = "Score: " + str(score)
    text2 = font.render(scoreText, True, white)
    windowSurface.blit(text2, (width-100,0))

    # if out of lives, end game
    if maxLives == 0:
        running = False
        gameOver(score)

    # Draw the window onto the screen.
    pygame.display.update()

    #reset movement
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    # Reset our FrameCounters
    if shotFrameCounter > 0:
        shotFrameCounter -= 1

    if targetFrameCounter > 0:
        targetFrameCounter -= 1

    if collisionFrameCounter > 0:
        collisionFrameCounter -= 1

    # Set the framerate of the game.
    mainClock.tick(30)