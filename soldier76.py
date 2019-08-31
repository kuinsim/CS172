#Suin Kim CS-172 Section 061

#import enemy abstract base class
from enemy import Enemy


class soldier76(Enemy):
    def __init__(self):
        self.__health = 100
        self.__name = 'Soldier: 76'

    def __str__(self):
        return self.__name

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def basicAttack(self, enemy):
        enemy.doDamage(8)

    def basicName(self):
        return 'Soldier: 76 fires some bullets at you!'

    def doDamage(self, damage):
        self.__health = self.__health - damage

    def chooseAttack(self, enemy):
        self.basicAttack(enemy)
        print(self.basicName())

    def checkHealth(self):
        if self.__health > 0:
            return True
        else:
            return False