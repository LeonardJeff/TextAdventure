from utils import *
class Player:
    def __init__(self, startingroom = None, name = "errorname"):

        self.inventory = []
        self.location = startingroom
        self.gold = 3
        self.quests = []
        self.name = name

        #for combat
        #player attack will range from 0-20
        #player health will range from 0-99
        #player speed will range from 0-20
        self.health = 10
        self.attack = 1
        self.magicattack = 1
        self.speed = 1

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

    def getAttackRating(self):
        total = self.attack
        if self.weapon:         #refine logic for this
            total += self.weapon.power
        return total

    def setName(self, text):
        self.name = text      