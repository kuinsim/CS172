#Suin Kim, Section 061
from Drawable import Drawable
import pygame
import pygame.freetype

pygame.init()


class Text(Drawable):
    def __init__(self, x, y, visible, score):
        self.__x = x
        self.__y = y
        self.__visible = visible
        self.__color = (0, 0, 0)
        self.__score = score

    def getLoc(self):
        return [self.__x, self.__y]

    def setLoc(self, locList):
        self.__x = locList[0]
        self.__y = locList[1]

    def setVisible(self, visibility):
        self.__visible = visibility

    def getVisible(self):
        return self.__visible

    def updateScore(self):
        self.__score = self.__score + 1

    def resetScore(self):
        self.__score = 0

    def draw(self, surface):
        global words
        words = pygame.freetype.SysFont('Times New Roman', 30, bold=0, italic=0)
        words.render_to(surface, [self.__x, self.__y], 'Score = %i' % self.__score, self.__color)

    def getRect(self):
        return words.get_rect('Score = %i' % self.__score)