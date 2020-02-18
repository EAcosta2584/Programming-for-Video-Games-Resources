################################################
# File Name: MusicAndMore.py
# Creator Name: Mr. Acosta
# Date Created: 2-18-2020
# Date Modified: 2-18-2020
################################################
# This program will show how to add music and ]
# sound to your games
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
pygame.display.set_caption('MusicAndMore')

sound1 = False
sound2 = False
sound3 = False
sound4 = False
pause = False


# loading our sounds and music
# pygame can use the following file types:
# .wav, .midi, .mp3, and .ogg

# here we are initializing a Sound object called "pew" to use later
pew = pygame.mixer.Sound('audio/sfx/laser5.wav')
boom2 = pygame.mixer.Sound('audio/sfx/boom2.wav')
boom6 = pygame.mixer.Sound('audio/sfx/boom6.wav')
boom7 = pygame.mixer.Sound('audio/sfx/boom7.wav')

# sound effects by Devin Watson, dklon on OpenGameArt.org


# use mixer.music.load to load in the background music file
pygame.mixer.music.load('audio/music/Space Fighter Loop.mp3')

# The music.play will start the music. Run this before the loop, or else it will attempt to start
# with every frame of the game. The first number is how many times it should be repeated. Set to -1 to
# repeat indefinitely. the second is where the file should start in seconds
# pygame.mixer.music.play(number of repeats, where to start (seconds)
pygame.mixer.music.play(-1, 0)
pygame.mixer.music.set_volume(.5)


# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_1:
            sound1 = True
        if event.key == K_2:
            sound2 = True
        if event.key == K_3:
            sound3 = True
        if event.key == K_4:
            sound4 = True
        if event.key == K_SPACE:
            pause = not pause
    if event.type == KEYUP:
        if event.key == K_1:
            sound1 = False
        if event.key == K_2:
            sound2 = False
        if event.key == K_3:
            sound3 = False
        if event.key == K_4:
            sound4 = False
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()


    # Draw the white background onto the surface.
    windowSurface.fill((255,255,255))

    if pause == True:
        pygame.mixer.music.pause()
    elif pause == False:
        pygame.mixer.music.unpause()

    if sound1 == True:
        pew.play()

    if sound2 == True:
        boom2.play()

    if sound3 == True:
        boom6.play()

    if sound4 == True:
        boom7.play()



    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)
