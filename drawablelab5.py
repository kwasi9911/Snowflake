#File Name:   drawablelab5.py
#Purpose:     Abstract class that allows us to create drawable objects
#             with different shapes, at a given location (x, y)

import pygame
from abc import ABC, abstractmethod

# Abstract Base Class: Drawable
class Drawable(ABC):
    '''
    Methods in this class were designed by A.Medlock 4/24/24
    '''
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    def getLoc(self):
        return (self.__x, self.__y)
        
    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]
    
    @abstractmethod
    def draw(self, surface):
        pass
        
#this class draws the background of the animation, giving it the dimensions and color       
class Rectangle(Drawable):
    def __init__(self, x, y, width, height, color):
        super().__init__(x,y)
        self.__width = width
        self.__height = height
        self.__color = color
        
    def draw(self,surface):
        location = self.getLoc()
        pygame.draw.rect(surface, self.__color, ((location[0], location[1]), (self.__width, self.__height)))
        
        

#this class is used to draw the snowflakes and give it its color and the y position it must reach before sticking to the ground 
class Snowflake(Drawable):
    def __init__(self,x,y,finalY,color):
        super().__init__(x,y)
        self.__color = color
        self.__finalY = finalY
        
    def getfinalY(self):
        return self.__finalY
    
    def draw(self,surface):
        location = self.getLoc()
        pygame.draw.line(surface, self.__color, (location[0] - 5, location[1]), (location[0] + 5,location[1]))
        pygame.draw.line(surface, self.__color, (location[0], location[1]-5), (location[0],location[1]+5))
        pygame.draw.line(surface, self.__color, (location[0] - 5, location[1]-5), (location[0] + 5,location[1]+5))
        pygame.draw.line(surface, self.__color, (location[0] - 5, location[1]+5), (location[0] + 5,location[1]-5))

        
        

