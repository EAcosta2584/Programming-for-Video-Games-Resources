################################################
# File Name: LearningPyGame.py
# Creator Name: Mr. Acosta
# Date Created: 1-05-2020
# Date Modified: 5-19-2020
################################################
# This program will demonstrate some of the
# basic rendering functions for PyGame
# ##############################################

import pygame, sys  # pygame requires importing the pygame module and sys module
from pygame.locals import *

import random

# This line is required to initialize the pygame commands in the program.
pygame.init()

# Color in pygame uses 256 RGB values stored in a tuple (R,G,B)
# Creating preset colors for use later
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# This creates the window that pygame will draw on. It is 500x400 pixels. There are other commands that can be set
# but it is best to leave those blank.
windowSurface = pygame.display.set_mode((500, 400))

# In Pygame, the top left corner of the window is the origin.
# Imagine the following is a 4x4 window. The top left is (0,0) and the bottom right is (4,4)
#
#           (0,0)+-+-+-+
#                +-+-+-+
#                +-+-+-+
#                +-+-+-+(4,4)
#

# To make the window visible, it must be filled with a color
windowSurface.fill(white)

# This command changes the text in the title bar of the window
pygame.display.set_caption('Hello')

# pygame can make use of system fonts. Here we create a font object set to "magneto," and font size 90. If the font
# named does not exist on a system, it will use the default system font.
basicFont = pygame.font.SysFont("magneto", 90)

# This is the string we want to display
myText = "Hello Class"

# Here we create a text object with the font and string we created. The first argument is the string we want to display,
# the second is a boolean for whether we want it to turn on anti-aliasing, the third is the text color, and the fourth is
# the text box color. If you ommit the fourth argument, the textbox will be clear.
text = basicFont.render(myText,True, white, blue)

# The basicFont object "text" we created above has a rectangle bounding box. Many objects in pygame have one.
# Here we are creating a new rect based on the object's bounding box
textRect = text.get_rect()

# A Rects top, bottom, left, right, or center positions can be updated
# Here we are using the window's rect center positions to update the textRect's center positions.
textRect.centerx  = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# For the text to render, we need to attach it to a rect or coordinate
# The blit function takes in the text, and the rect or coordinate to render it to.
windowSurface.blit(text, textRect)

# Pygame has functions to create basic shapes.
# to draw a circle, you need the circle center coordinates, radius, and line thickness
# pygame.draw.cirle(window to draw on, color, (center x,y position), radius, line thickness)
pygame.draw.circle(windowSurface, blue, (300, 250), 20, 1)

# a thickness of 0 fills the circle or ellipse

# to draw an ellipse, you need the top left corner of the ellipse's bounding box, its width, height, and line thickness
# pygame.draw.ellipse(window to draw on, color, (top left corner x,y position, width, and height), line thickness)
pygame.draw.ellipse(windowSurface, green, (300, 250, 80, 40), 0)

# to draw a rectangle, you need the top left vertex, and the width and height
# pygame.draw.rect(window to draw on, color, (top left corner x,y position, width, and height)
pygame.draw.rect(windowSurface, red, (250, 100, 30, 90))

# pygame does not have functions for less than four sides or more than four sides. To draw those, the polygon
# function is needed. The polygon function can take in any number of vertices
# pygame.draw.line(window, color, (vertex1, vertex2, vertex 3, etc...))
pygame.draw.polygon(windowSurface, (255, 120, 0), ((146, 0), (200, 15), (32, 150), (0, 106)))

# Lines are drawn by declaring the start and finish coordinates, as well as line thickness
# pygame.draw.line(window, color, first point, second point, line thickness)
pygame.draw.line(windowSurface, blue, (60, 60), (120, 60), 10)
pygame.draw.line(windowSurface, blue, (120, 60), (60, 120), 5)

# A PixelArray is a 2D list of individual pixels
# The first index in the PixelArray list is the x coordinate, and the second index is the y coordinate
pixArray = pygame.PixelArray(windowSurface)
for x in range(10):
    for y in range (10):
        pixArray[x][y] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# Once we're done with a PixelArray, we can delete it to save memory
del pixArray

# This line is used to update the window with all of the draw and render commands we made before
pygame.display.update()

# Finally, there needs to be something to keep the program from ending
# here is an infinite loop that waits for the user to exit the window.
while True:
    # This loop is looking for pygame events
    for event in pygame.event.get():
        # if the event is a QUIT event (clicking the close button on the window), it will terminate the program
        if event.type == QUIT:
            pygame.quit()
            sys.exit()