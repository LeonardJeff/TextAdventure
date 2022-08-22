from Monster import Monster
from items import *
import random



#monster attack will range from 0-20
#monster health will range from 0-99
#monster speed will range from 0-20

firstgoblin = Monster(
"Wandering Goblin", 
"Green ugly goblin",
"t", 
drops = [apple, mushroom],
attack = 3, 
health = 10,
speed = 1,
expdrop = 5,
level= 4)

goblin2 = Monster(
"Goblin2", 
"Green ugly goblin",
"Yarrrrrrrr Ima goblin and im going to kill you!", 
apple, 5, 50)

garg = Monster(
"Garg", 
"He looks tough. He's also three times your size.", 
"Puny man! Garg bring glory to goblin brothers!!",
attack = 6,
health = 25
)

def getgoblin(attack = 3, health = 10, attackvariantion = [0,0]):  #add defaults and then when u call getgoblin set the random stuff
    m = Monster(
    "Goblin", 
    "Green ugly goblin",
    "t", 
    drops = [apple, mushroom],
    attack = attack + random.randint(attackvariantion[0], attackvariantion[1]), 
    health = health,
    speed = 1,
    defense = 1,
    expdrop = 5)
    return m
