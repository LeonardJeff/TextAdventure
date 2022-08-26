from equippable import Armor, ArmorType
from item import Item
from utils import *
import random

from weapon import Weapon

class Player:
    def __init__(self, startingroom = None, name = "errorname"):

        self.inventory = []
        self.location = startingroom
        self.gold = 3
        self.quests = []
        self.name = name
        self.level = 1
        self.experience = 0
        self.magiclevel = 1
        self.health = 10 #player health will range from 10-99
        self.maxhealth = 10     
        self.attack = 1 #player attack will range from 1-20
        self.magiclevel = 1 #player magiclevel will range 1-99
        self.speed = 3  #player speed will range from 3-20

        #for equip
        self.headslot = None
        self.bodyslot = None
        self.bootslot = None
        self.ringslot = None
        self.weapon   = None
    
    def equip(self, characteritem):
        if isinstance(characteritem, Item):
            if isinstance(characteritem, Weapon):
                self.inventory.append(self.weapon)
                self.weapon = characteritem
            if isinstance(characteritem, ArmorType.HELMET):
                self.inventory.append(self.headslot)
                self.headslot = characteritem
            if isinstance(characteritem, ArmorType.BODY):
                self.inventory.append(self.bodyslot)
                self.bodyslot = characteritem
            if isinstance(characteritem, ArmorType.BOOTS):
                self.inventory.append(self.bootslot)
                self.bootslot = characteritem
            if isinstance(characteritem, ArmorType.RING):
                self.inventory.append(self.ringslot)
                self.ringslot = characteritem
    
    def unequip(self, characteritem):
        if isinstance(characteritem, Item):
            if isinstance(characteritem, Weapon):
                self.inventory.append(self.weapon)
                self.weapon = None
            if isinstance(characteritem, ArmorType.HELMET):
                self.inventory.append(self.headslot)
                self.headslot = None
            if isinstance(characteritem, ArmorType.BODY):
                self.inventory.append(self.bodyslot)
                self.bodyslot = None
            if isinstance(characteritem, ArmorType.BOOTS):
                self.inventory.append(self.bootslot)
                self.bootslot = None
            if isinstance(characteritem, ArmorType.RING):
                self.inventory.append(self.ringslot)
                self.ringslot = None
            
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
    
    def openinv(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(">-----------------------------------------------<")
        print(f"{self.name} - {self.health}/{self.maxhealth} HP - {self.gold} Gold")
        print(f"Weapon - {self.weapon}")
        print(f"Head - {self.headslot}")
        print(f"Ring - {self.ringslot}")
        print(f"Body - {self.bodyslot}")
        print(f"Boots - {self.bootslot}")
        print(">-----------------------------------------------<")
        g = self.inventory
        
        print(self.inventory.sort(key=g))
        for item in self.inventory:
            print(self.inventory[0:8])
        if len(self.inventory) > 9:
            print("[0] Next Page -->")
        playerselect = input()
        pass
    
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