from monster import Monster
from items import *
import random



#monster attack will range from 0-20
#monster health will range from 10-75
#monster speed will range from 0-20

firstgoblin = Monster(                          #make drop bundle of flowers upon death
"Wandering Goblin",
"You shouldn't get close, its smell might be contagious.",
"The goblin grumbles something before it chucks a few small stones in your direction", 
inventory = [apple, mushroom],
attack = 3, 
health = 12,
maxhealth=12,
speed = 2,
expdrop = 5,
level= 4,
drops = None
)

forestdemon = Monster(
"Woods Demon",
"The two jagged horns pertruding from both sides of his head suggest he is not a friend.",
"The demon lets out an aggressive screech as it begins to stomp towards you.",
inventory = [],
attack = 7,
health = 75,
speed = 10,
defense = 5,
level = 25
)

wanderinggoblin = Monster(
"Wandering Goblin", 
"It seems very aggresive, not sure if it can pack much of a punch though.",
"I'll teach you rude human to respect goblins!", 
attack = 3, 
health = 12, 
maxhealth = 12,
level = 3,
speed = 3,
drops = flowers)

garg = Monster(
"Garg", 
"He looks tough. He's also three times your size.", 
"Puny man! Garg bring glory to goblin brothers!!",
attack = 6,
health = 25
)

def getgoblin(attack = 3, health = 10, speed = 3, attackvariantion = [0,2], healthvariantion = [0,7] , speedvariantion = [0,4]):  #add defaults and then when u call getgoblin set the random stuff
    m = Monster(
    name = "Goblin", 
    examine = "Green, ugly, and disgusting.",
    dialogue = "The goblin grumbles something before it chucks a few small stones in your direction",
    #"A run-of-the-mill goblin who doesn't seem to keen on becoming friends.", 
    inventory = [mushroom],
    attack = attack + random.randint(attackvariantion[0], attackvariantion[1]), 
    health = health + random.randint(healthvariantion[0], healthvariantion[1]),
    speed = speed + random.randint(speedvariantion[0], speedvariantion[1]),
    defense = 3,
    expdrop = 4,
    drops = mushroom
    )
    return m

def getcoyote(attack = 3, health = 10, speed = 4, attackvariantion = [0,2], healthvariantion = [0,7] , speedvariantion = [0,2]):  #add defaults and then when u call getgoblin set the random stuff
    m = Monster(
    name = "Plains Coyote", 
    examine = "It doesn't look too friendly.",
    dialogue = "A Plains Coyote draws near!", 
    inventory = [],
    attack = attack + random.randint(attackvariantion[0], attackvariantion[1]), 
    health = health + random.randint(healthvariantion[0], healthvariantion[1]),
    speed = speed + random.randint(speedvariantion[0], speedvariantion[1]),
    defense = 2,
    expdrop = 5,
    drops = coyotebones
    )
    return m

def getdemon(attack = 7, health = 75, speed = 10, defense = 3, level = 25, inventory = None): 
    m = Monster(
    "Woods Demon", 
    "The two jagged horns pertruding from both sides of his head suggest he is not a friend.",
    "The demon lets out an aggressive screech as it begins to stomp towards you.", 
    inventory = inventory,
    attack = attack,
    health = health,
    speed = speed,
    defense = defense,
    level = level) 
    return m
