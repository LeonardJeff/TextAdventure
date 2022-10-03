import random
from utils import pushtext

class Monster:
    def __init__(self, name, examine, dialogue=[], inventory=None, attack=1, 
    health=5, maxhealth = 5, speed = 1, expdrop = 0, defense = 0, level = 0, drops = None):

        if inventory is None:
            inventory = []
        self.inventory = inventory       
        
        self.name = name
        self.examine = examine
        self.dialogue = dialogue
        self.attack = attack
        self.health = health
        self.maxhealth = maxhealth
        self.speed = speed
        self.expdrop = expdrop
        self.defense = defense
        self.level = level
        self.drops = drops
    def __repr__(self):
        return f"#<Monster: {self.name}{self.health}>"
    
    def calcdamage(self, playerarmor, playerspeed):

        diceroll ={
            0 : 0, # missed attack
            1 : .7,
            2 : .75, 
            3 :.8, 
            4 : .9,
            5 : .9,
            6 : 1,
            7 : 1,
            8 : 1.1,
            9: 1.2,
            10: 1.5
            }
        
        if self.speed >= playerspeed:
            roll = random.randint(1, 10)
        
        else: 
            roll = random.randint(0, 10)
        
        scaler = diceroll.get(roll)
        
        
        
        return int(max(self.attack - playerarmor, 1) * scaler), roll