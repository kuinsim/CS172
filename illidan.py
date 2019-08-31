# Suin Kim CS-172 Section 061

# import enemy abstract base class and random module
from enemy import Enemy
import random


class illidan(Enemy):
    def __init__(self):
        self.__health = 300
        self.__name = 'Illidan Stormrage'
        #sets a random seed with value 0
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
        return 'Illidan Stormrage swings his two glaives at you!'

    #methods for sweeping strike, a slightly stronger attack
    def sweepingStrikeAttack(self, enemy):
        enemy.doDamage(16)

    def sweepingStrikeName(self):
        return 'Illidan Stormrage charges at you and deals a swift blow!'

    #methods for eye beam, the strongest attack
    def eyeBeamAttack(self, enemy):
        enemy.doDamage(20)

    def eyeBeamName(self):
        return 'Illidan Stormrage enters a frenzy and shoots a continous beam from his eyes in your direction!'

    #randomly chooses an attack, but does so with regards to strength of each attack
    def chooseAttack(self, enemy):
        Y = random.randint(1, 10)
        if Y <= 6:
            self.basicAttack(enemy)
            print(self.basicName())
        elif Y <= 9:
            self.sweepingStrikeAttack(enemy)
            print(self.sweepingStrikeName())
        else:
            self.eyeBeamAttack(enemy)
            print(self.eyeBeamName())

    def doDamage(self, damage):
        self.__health = self.__health - damage

    def checkHealth(self):
        if self.__health > 0:
            return True
        else:
            return False