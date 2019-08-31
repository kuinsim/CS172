# Suin Kim CS-172 Section 061

# import the enemy abstract base class and random module
from enemy import Enemy
import random

class zergling(Enemy):
    def __init__(self):
        self.__health = 200
        self.__name = 'Zergling'
        # sets a random seed with value 0
        random.seed(0)

    def __str__(self):
        return self.__name

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def basicAttack(self, enemy):
        enemy.doDamage(10)

    def basicName(self):
        return 'Zergling cut you with its claws!'

    # methods for stronger attack
    def specialAttack(self, enemy):
        enemy.doDamage(16)

    def specialName(self):
        return 'Zergling strikes with metabolic boost!'

    def doDamage(self, damage):
        self.__health = self.__health - damage

    # randomly chooses an attack, but does so with regards to strength of each attack
    def chooseAttack(self, enemy):
        Y = random.randint(1, 4)
        if Y <= 3:
            self.basicAttack(enemy)
            print(self.basicName())
        else:
            self.specialAttack(enemy)
            print(self.specialName())

    def checkHealth(self):
        if self.__health > 0:
            return True
        else:
            return False