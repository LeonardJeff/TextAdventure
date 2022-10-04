from monster import Monster
from items import *
from equippables import *
import random



#monster attack will range from 0-20
#monster health will range from 10-75
#monster speed will range from 0-20


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
attack = 2, 
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

def getgoblin(attack = 3, maxhealth = 10, speed = 3, attackvariantion = [0,2], maxhealthvariantion = [0,7] , speedvariantion = [0,4]):  #add defaults and then when u call getgoblin set the random stuff
    m = Monster(
    name = "Goblin", 
    examine = "Green, ugly, and disgusting.",
    dialogue = "A golin approaches!",
    #"A run-of-the-mill goblin who doesn't seem to keen on becoming friends.", 
    inventory = [mushroom],
    attack = attack + random.randint(attackvariantion[0], attackvariantion[1]), 
    maxhealth = maxhealth + random.randint(maxhealthvariantion[0], maxhealthvariantion[1]),
    health = maxhealth,
    speed = speed + random.randint(speedvariantion[0], speedvariantion[1]),
    defense = 3,
    expdrop = 4,
    drops = [leathershoes, apple, mushroom, mushroom1, goblinMask]
    )
    return m

def getcoyote(attack = 3, maxhealth = 10, speed = 4, attackvariantion = [0,2], maxhealthvariantion = [0,10] , speedvariantion = [0,2]):  #add defaults and then when u call getgoblin set the random stuff
    m = Monster(
    name = "Plains Coyote", 
    examine = "It doesn't look too friendly.",
    dialogue = "A Plains Coyote draws near!", 
    inventory = [],
    attack = attack + random.randint(attackvariantion[0], attackvariantion[1]), 
    maxhealth = maxhealth + random.randint(maxhealthvariantion[0], maxhealthvariantion[1]),
    health = maxhealth,
    speed = speed + random.randint(speedvariantion[0], speedvariantion[1]),
    defense = 2,
    expdrop = 5,
    drops = [coyotebones, wildturnip]
    )
    return m

def getdemon(attack = 7, health = 75, speed = 10, defense = 3, level = 25, inventory = None): 
    m = Monster(
    name = "Woods Demon", 
    examine = "The two jagged horns pertruding from both sides of his head suggest he is not a friend.",
    dialogue = "The demon lets out an aggressive screech as it begins to stomp towards you.", 
    inventory = inventory,
    attack = attack,
    health = health,
    speed = speed,
    defense = defense,
    level = level) 
    return m

def getbee(attack = 1, maxhealth = 4, speed = 5, attackvariantion = [0,1], maxhealthvariantion = [0,3] , speedvariantion = [0,1]):  #add defaults and then when u call getgoblin set the random stuff
    m = Monster(
    name = "Bee", 
    examine = "If you had some binoculars, you would likely be able to see it's angry bee face.",
    dialogue = "Bzzzzz Bzzzzz!",
    inventory = [None],
    attack = attack + random.randint(attackvariantion[0], attackvariantion[1]), 
    maxhealth = maxhealth + random.randint(maxhealthvariantion[0], maxhealthvariantion[1]),
    health = maxhealth,
    speed = speed + random.randint(speedvariantion[0], speedvariantion[1]),
    defense = 1,
    expdrop = 3,
    drops = [honeydrop, honeydrop]
    )
    return m