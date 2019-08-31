#Suin Kim, Section 061
from Drawable import Drawable
import pygame

pygame.init()


class Block(Drawable):
    def __init__(self, x, y, visible, width, height, color):
        self.__x = x
        self.__y = y
        self.__visible = visible
        self.__color = color
        self.__width = width
        self.__height = height

    def getLoc(self):
        return [self.__x, self.__y]

    def setLoc(self, locList):
        self.__x = locList[0]
        self.__y = locList[1]

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def setVisible(self, visibility):
        self.__visible = visibility

    def getVisible(self):
        return self.__visible

    def draw(self, surface):
        daRect = pygame.Rect(self.__x, self.__y, self.__width, self.__height)
        pygame.draw.rect(surface, self.__color, daRect, 0)
        pygame.draw.rect(surface, (0, 0, 0), daRect, 1)

    def getRect(self):
        return pygame.Rect(self.__x, self.__y, self.__width, self.__height)