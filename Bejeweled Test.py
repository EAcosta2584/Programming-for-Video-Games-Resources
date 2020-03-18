################################################
# File Name: Bejeweled Test.py
# Creator Name: Mr. Acosta
# Date Created: 3-4-2020
# Date Modified: 3-4-2020
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
pygame.display.set_caption('Swap Game Test')


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

redGem = {'rect':pygame.Rect(-50, -50, 50, 50), 'color': red}
greenGem = {'rect':pygame.Rect(-50, -50, 50, 50), 'color': green}
blueGem = {'rect':pygame.Rect(-50, -50, 50, 50), 'color': blue}
blankGem = {'rect':pygame.Rect(-50, -50, 50, 50), 'color': white}


colors = [red, green, blue, white]
gems = []
pieces = []

for i in range(25):
    gems.append(pygame.Rect(-50, -50, 50, 50))
    gems.append(colors[random.randint(0,2)])
    pieces.append(gems)
    gems = []

mList = [
[],
[],
[],
[],
[],
]

a = 0
for piece in mList:
        for i in range (5):
            piece.append(pieces[a])
            a += 1

windowSurface.fill(white)

grid = 150

x = 180
y = 180
a = 0

for i in range (6):
    pygame.draw.line(windowSurface, black, (grid, 150), (grid, 450), 2)
    pygame.draw.line(windowSurface, black, (150, grid), (450, grid), 2)
    grid += 60

for piece in mList:
    for i in range(5):
        piece[i][0].centerx = x + (60 * i)
        piece[i][0].centery = y + (60 * a)
        pygame.draw.rect(windowSurface, piece[i][1], piece[i][0])
        print(piece[i][0].center)
    a += 1
    print("\n")

def checkVert(v, h, color):
    count = 1
    removePiece = []
    removePiece.append(v)
    v +=1
    while v <= 4:
        if mList[v][h][1] == color:
            removePiece.append(v)
            count += 1
            v += 1
        else:
            break
    return removePiece

def checkHoriz(v, h, color):
    count = 1
    removePiece = []
    removePiece.append(h)
    h +=1
    while h <= 4:
        if mList[v][h][1] == color:
            removePiece.append(h)
            count += 1
            h += 1
        else:
            break
    return removePiece

def removeVert(i, remove):
    if len(remove) > 2:
        for piece in remove:
            mList[piece][i][1] = white
            pygame.draw.rect(windowSurface, mList[piece][i][1], mList[piece][i][0])

def removeHoriz(v, remove):
    if len(remove) > 2:
        for piece in remove:
            mList[v][piece][1] = white
            pygame.draw.rect(windowSurface, mList[v][piece][1], mList[v][piece][0])

def checkMatch():
    for t in range(5):
        for i in range(5):
            if mList[t][i][1] == red:
                color = red
                removeVert(i, checkVert(t, i, color))
                removeHoriz(t, checkHoriz(t, i, color))
            if mList[t][i][1] == green:
                color = green
                removeVert(i, checkVert(t, i, color))
                removeHoriz(t, checkHoriz(t, i, color))
            if mList[t][i][1] == blue:
                color = blue
                removeVert(i, checkVert(t, i, color))
                removeHoriz(t, checkHoriz(t, i, color))

def checkBlank():
    for v in range(5):
        for h in range(5):
            if v == 0:
                if mList[v][h][1] == white:
                    mList[v][h][1] = colors[random.randint(0,2)]
                    pygame.draw.rect(windowSurface, mList[v][h][1], mList[v][h][0])
            # elif v > 0:
            #    if mList[v][h][1] == white:
            #         move = v
            #         while move > 0:
            #             tempGem = mList[move][h]
            #             mList[move][h] = mList[move-1][h]
            #             mList[move-1][h] = tempGem
            #             move -=1
            #             # pygame.draw.rect(windowSurface, mList[v][h][1], mList[v][h][0])
            #             # pygame.draw.rect(windowSurface, mList[v-1][h][1], mList[v-1][h][0])
    v = 4
    while v > 0:
        for h in range(5):
           if mList[v][h][1] == white:
                tempGem = mList[v][h]
                mList[v][h] = mList[v-1][h]
                mList[v-1][h] = tempGem
                pygame.draw.rect(windowSurface, mList[v][h][1], mList[v][h][0])
                pygame.draw.rect(windowSurface, mList[v-1][h][1], mList[v-1][h][0])
        v -= 1


pygame.display.update()
store = []

def pauseGame():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                return False
pauseGame()
checkMatch()
# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            for v in range(len(mList)):
                for h in range (len(mList)):
                    if mList[v][h][0].left < x < mList[v][h][0].right and mList[v][h][0].top < y < mList[v][h][0].bottom:
                        store.append(v)
                        store.append(h)
            print(x)
            print(y)
            print(store)


    x = 180
    y = 180
    a = 0
    grid = 150
    for i in range(6):
        pygame.draw.line(windowSurface, black, (grid, 150), (grid, 450), 2)
        pygame.draw.line(windowSurface, black, (150, grid), (450, grid), 2)
        grid += 60

    if len(store) == 4:
        tempGem = mList[store[0]][store[1]]
        mList[store[0]][store[1]] = mList[store[2]][store[3]]
        mList[store[2]][store[3]] = tempGem
        pygame.draw.rect(windowSurface, mList[store[0]][store[1]][1], mList[store[0]][store[1]][0])
        pygame.draw.rect(windowSurface, mList[store[2]][store[3]][1], mList[store[2]][store[3]][0])
        store=[]
        checkMatch()
        # checkBlank()
        for v in range(5):
            for h in range(5):
                mList[v][h][0].centerx = x + (60 * h)
                mList[v][h][0].centery = y + (60 * a)
                pygame.draw.rect(windowSurface, mList[v][h][1], mList[v][h][0])
            a += 1

    # for v in range(5):
    #     for h in range(5):
    #         if v == 0:
    #             if mList[v][h][1] == white:
    #                 mList[v][h][1] = colors[random.randint(0,2)]
    #                 pygame.draw.rect(windowSurface, mList[v][h][1], mList[v][h][0])

    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(12)
