#################################################
# File Name: PlatformerSettings.py
# Creator Name: Mr. Acosta
# Date Created: 4-14-2020
# Date Modified: 4-14-2020
#################################################
# Display, color, player, and platform settings
# can be stored here.
#################################################

# Display Variables
width = 400
height = 500
gameTitle = "Infinite Platformer"

# Color variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Player variables
lives = 3

# Gravity and movement defaults
gravity = .5
moveX = 4
moveY = 0

# Platform Variables
platH = 20 # platform thickness
# Platform widths
platW_Small = 40
platW_Med = 65
platW_Big = 100
platW = [platW_Small, platW_Med, platW_Big]