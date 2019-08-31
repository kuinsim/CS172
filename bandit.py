# Suin Kim CS-172 Section 061

# import the enemy abstract base class
from enemy import Enemy


class bandit(Enemy):
    def __init__(self):
        self.__health = 50
        self.__name = 'Bandit'

    def __str__(self):
        return self.__name

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def basicAttack(self, enemy):
        enemy.doDamage(6)

    def basicName(self):
        return 'Bandit cuts you with a dull knife!'

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