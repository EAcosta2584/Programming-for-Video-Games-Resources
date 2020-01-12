import pygame, sys, time
from pygame.locals import *

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

window = pygame.display.set_mode((500, 400), 0, 32)

window.fill(white)

pygame.display.set_caption('Hello')

basicFont = pygame.font.SysFont("magneto", 90)

myText = "FBI Warning"

text = basicFont.render(myText,True, white, blue)

textRect = text.get_rect()

textRect.centerx  = window.get_rect().centerx
textRect.centery = window.get_rect().centery

pygame.draw.circle(window, blue, (300,250), 20, 10)

pygame.draw.ellipse(window, green, (300, 250, 80, 40), 0)



pygame.draw.rect(window, red, (250, 100, 30, 90))

pygame.draw.polygon(window, (255,120, 0), ((146, 0), (200, 15), (32, 150), (0, 106)))

pygame.draw.line(window, blue, (60, 60), (120, 60), 10)
pygame.draw.line(window, blue, (120, 60), (60, 120), 5)

import random

pixArray = pygame.PixelArray(window)
for x in range(500):
    # for y in range (400):
        pixArray[x] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

del pixArray

right = 'right'

window.blit(text, textRect)
square = {'rect':pygame.Rect(0,200, 30, 30), 'color':red, 'dir': right}

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.fill(white)

    if square['dir'] != 'left':
        square['rect'].left += 4
    pygame.draw.rect(window, square['color'], square['rect'])

    pygame.display.update()
    time.sleep(.2)