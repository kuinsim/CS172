#Suin Kim, Section 061
from abc import ABC, abstractmethod


class Drawable():
    def __init__(self, x=0, y=0, visible=True):
        self.__x = x
        self.__y = y
        self.___visible = visible

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def get_rect(self):
        pass