#Suin Kim CS-172 Section 061

#import hero and different enemy classes, as well as random and sys module
from hero import hero
from illidan import illidan
from bandit import bandit
from zergling import zergling
from soldier76 import soldier76
import random
import sys

print('Welcome to Adventure Battle!')
#asks user for name of hero
heroName = input('What is the name of your hero?\n')
#creates hero
Hero = hero(heroName)
#asks user for number of enemies
numEnemies = int(input('How many monsters will %s battle?\n' % Hero.getName()))
#list that contains enemies
enemyList = []
#list that contains random numbers that are associated with enemies
enemyNumList = []
#sets a random seed with value 0
random.seed(0)

#randomly puts enemies in enemyList, but does so with regards to varying enemy strengths
for i in range(numEnemies):
    enemyNumList.append(random.randint(1, 14))
for i in range(numEnemies):
    Y = enemyNumList[i]
    if Y <= 5:
        enemyList.append(bandit())
    elif Y <= 9:
        enemyList.append(soldier76())
    elif Y <= 12:
        enemyList.append(zergling())
    else:
        enemyList.append(illidan())

#sets maximum health for hero as starting health
startHealth = Hero.getHealth()

#hero and enemy combat, one by one
for enemy in enemyList:
    print('\nYou have encountered a %s!' % enemy)
    enemyHealth = enemy.getHealth()
    while True:
        print('%s: %i/%i health' % (Hero.getName(), Hero.getHealth(), startHealth))
        Hero.itemsLeft()
        while True:
            command = input('Enter Command: sword shield fireball potion exit\n')
            if command.lower() == 'exit':
                print("Thanks for Playing")
                sys.exit()
            elif command.lower() == 'sword':
                Hero.basicAttack(enemy)
                print(Hero.basicName())
                if enemy.getHealth() > 0:
                    enemy.chooseAttack(Hero)
                break
            elif command.lower() == 'shield':
                Hero.shieldAttack()
                print(Hero.shieldName())
                if enemy.getHealth() > 0:
                    enemy.chooseAttack(Hero)
                break
            elif command.lower() == 'fireball':
                if Hero.fireballAttack(enemy):
                    print(Hero.fireballName())
                    if enemy.getHealth() > 0:
                        enemy.chooseAttack(Hero)
                    break
                else:
                    print('You are out of fireballs!')
                    continue
            elif command.lower() == 'potion':
                if Hero.potionAttack():
                    print(Hero.potionName())
                    if enemy.getHealth() > 0:
                        enemy.chooseAttack(Hero)
                    break
                else:
                    print('You are out of potions!')
                    continue
            else:
                print('Not a valid input. Try again.')
                continue
        if Hero.checkHealth() == False:
            print('You died! Game over.')
            sys.exit()
        if enemy.checkHealth() == False:
            print('Enemy is defeated!')
            break

print('Congratulations! %s has defeated all monsters and won the day!' % Hero.getName())
