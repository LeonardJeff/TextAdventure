from utils import *
import random

class Player:
    def __init__(self, startingroom = None, name = "errorname"):

        self.inventory = []
        self.location = startingroom
        self.gold = 3
        self.quests = []
        self.name = name
        self.level = 1
        self.experience = 0

        #for combat
        #player attack will range from 0-20
        #player health will range from 0-99
        #player speed will range from 0-20
        self.health = 10
        self.attack = 4
        self.magicattack = 1
        self.speed = 15

        #for equip
        self.headslot = None
        self.bodyslot = None
        self.bootslot = None
        self.ringslot = None
        self.weapon   = None

    def getArmorRating(self):
        total = 0
        if self.headslot:
            total += self.headslot.armor
        if self.bodyslot:
            total += self.bodyslot.armor
        if self.bootslot:
            total += self.bootslot.armor
        if self.ringslot:
            total += self.ringslot.armor
        return total
    
    def calcdamage(self, enemydefense, enemyspeed):
        
        diceroll ={
            0 : 0, # missed attack
            1 : .7,
            2 : .75, 
            3 :.8, 
            4 : .9,
            5 : .9,
            6 : 1,
            7 : 1,
            8 : 1,
            9: 1.1,
            10: 1.75
            }
        
        if self.speed >= enemyspeed:
            roll = random.randint(1, 10)
        
        else: 
            roll = random.randint(0, 10)
        scaler = diceroll.get(roll)
        
        
        return int(max(self.attack - enemydefense, 1) * scaler), roll

    def getAttackRating(self):
        total = self.attack
        if self.weapon:         #refine logic for this
            total += self.weapon.power
        return total

    def setName(self, text):
        self.name = text      