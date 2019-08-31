#Suin Kim CS-172 Section 061

#import the enemy abstract base class
from enemy import Enemy

#hero class
class hero(Enemy):
    def __init__(self, name):
        self.__name = name
        self.__health = 100
        self.__shield = False
        self.__numFireballs = 10
        self.__numPotions = 6

    def __str__(self):
        return self.__name

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    #method that tells player how many fireballs and potions the hero has left
    def itemsLeft(self):
        print('Remaining: %i Fireballs, %i Potions' % (self.__numFireballs, self.__numPotions))

    def basicAttack(self, enemy):
        enemy.doDamage(25)

    def basicName(self):
        return '\nSword Slash Attack!'

    #method for shield defense
    def shieldAttack(self):
        self.__shield = True

    def shieldName(self):
        return '\nHide Behind Shield!'

    #method for fireball attack
    def fireballAttack(self, enemy):
        if self.__numFireballs > 0:
            enemy.doDamage(50)
            self.__numFireballs = self.__numFireballs - 1
            return True
        else:
            return False

    def fireballName(self):
        return '\nFireball Attack Successful!'

    #method for potion, an "attack" that does -25 damage which is the same as recovering 25 health
    def potionAttack(self):
        if self.__numPotions > 0:
            self.doDamage(-25)
            self.__numPotions = self.__numPotions - 1
            return True
        else:
            return False

    def potionName(self):
        return '\nYou drank a potion.'

    #method for damage dealt to hero
    def doDamage(self, damage):
        if self.__shield:
            self.__health = self.__health - (damage/2)
            self.__shield = False
        else:
            self.__health = self.__health - damage
            if self.__health > 100:
                self.__health = 100

    #method that checks if hero is alive
    def checkHealth(self):
        if self.__health > 0:
            return True
        else:
            return False