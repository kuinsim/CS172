#Suin Kim CS-172 Section 061

#import the abstract base class and abstractmethod
from abc import ABC, abstractmethod

#abstract enemy class
class Enemy(ABC):
    def __init__(self):
        return
    def __str__(self):
        return "An Enemy"

    #@abstractmethod declares the following methods as abstract methods and need to be instantiated
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getHealth(self):
        pass

    @abstractmethod
    def basicAttack(self,enemy):
        pass

    @abstractmethod
    def basicName(self):
        pass

    @abstractmethod
    def doDamage(self,damage):
        pass

    @abstractmethod
    def checkHealth(self):
        pass
