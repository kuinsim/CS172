#Suin Kim, Section 061
from Drawable import Drawable
import pygame

pygame.init()


class Ball(Drawable):
    def __init__(self, x, y, visible):
        self.__x = x
        self.__y = y
        self.__visible = visible
        self.__color = (255, 0, 0)
        self.__radius = 8

    def getLoc(self):
        return [self.__x, self.__y]

    def setLoc(self, locList):
        self.__x = locList[0]
        self.__y = locList[1]

    def getWidth(self):
        return self.__radius

    def getHeight(self):
        return self.__radius

    def setVisible(self, visibility):
        self.__visible = visibility

    def getVisible(self):
        return self.__visible

    def draw(self, surface):
        pygame.draw.circle(surface, self.__color, [int(self.__x), int(self.__y)], self.__radius, 0)

    def getRect(self):
        return pygame.Rect(self.__x, self.__y, 16, 16)