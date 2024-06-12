# Name: Nana Kwasi Owusu
#Program Description: This is a simulation of a snowflake 

# import necessary modules and classes
import pygame
from drawablelab5 import *
import random

# initialize Pygame and create window
pygame.init()
width = 500
height = 500
surface = pygame.display.set_mode((width, height))

#this initiates the situation that the space bar has been pressed to false. A list of background and snowflake objects is added to a list.
pressedSpace = False
objects = []
snowflake = []
ground = Rectangle(0, 300, 500, 300, (0, 255, 0))
objects.append(ground)
sky = Rectangle(0, 000, 500, 300, (0, 0, 255))    
objects.append(sky)                

# the game loop
while True:
    for event in pygame.event.get():  
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
            
        if (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE):
            if pressedSpace == False:
                pressedSpace = True
            else:
                pressedSpace = False
    if pressedSpace == False:
        for item in objects:
            if isinstance(item, Snowflake) == True:
            
                if item.getLoc()[1] < item.getfinalY():
                    item.setLoc((item.getLoc()[0], item.getLoc()[1] + 2))
                else:
                    item.setLoc((item.getLoc()[0], item.getfinalY()))
            item.draw(surface)
        x = random.randint(0, 500)
        
        finalYpos = random.randint(300, 500)
        snow = Snowflake(x, 0, finalYpos, (255, 255, 255))
        objects.append(snow)
    else:
        continue
    
    
    pygame.display.update()
 