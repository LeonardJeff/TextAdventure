import os
import Monster
from player import Player
from utils import getLowerInput
from utils import pushtext
from enum import Enum
import time
import quests
import sys
import random
import monsters
import combatbehavior

class CombatOption(Enum):
            attack = 1
            items = 2
            examine = 3
            run = 4
            magic = 5
            jump = 6


class Combat:
    
    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 0
        self.turndesc = ["","","",""]               
        self.OptionNumber = {
            "1" : CombatOption.attack,
            "2" : CombatOption.items, 
            "3" : CombatOption.examine, 
            "4" : CombatOption.run
            }
        self.combatEnd = 0   #set to 1 to end combat
    
    def runaway(self, subject):
        if type(subject) == Player:
            pushtext("You have run from battle",cutscenemode = True )
            self.combatEnd = 1
            self.startcombat
        if type(subject) == Monster:
            pushtext("The " + str(subject) + " fled from battle.",cutscenemode = True )
        
    def checkstate(self):
        if self.player.health <= 0:
            print("You died")
            sys.exit(0) 
        if self.enemy.health <= 0:
            print("You defeated " + self.enemy.name + "!")
            self.combatEnd = 1
            self.startcombat
        
        
        
    def startcombat(self):
        
        if monsters.firstgoblin.health <= 0:
            self.OptionNumber.update({"1" : CombatOption.attack})
            self.OptionNumber.update({"2" : CombatOption.magic})
            self.OptionNumber.update({"3" : CombatOption.items})
            self.OptionNumber.update({"4" : CombatOption.examine})       
            self.OptionNumber["5"] = CombatOption.run   #keeping this here because im emotionally attached

        os.system('cls' if os.name == 'nt' else 'clear')
        #firstpart
        print(str(self.player.health) + "				" + str(self.enemy.health))
        print(str(self.player.name) + "				" + str(self.enemy.name))
        #second part
        print("_________________________________________________")
        print("|")
        print("|")
        print("|")
        print("|")
        #third part
        print(">-----------------------------------------------<")
        print("| [1]    Attack                |")
        if monsters.firstgoblin.health <= 0:
            print("| [2]    Magic                 |")
            print("| [3]    Items                 |")
            print("| [4]    Examine               |")
            print("| [5]    Run(%)                |")
        if monsters.firstgoblin.health > 0:
            print("| [2]    Items                 |")
            print("| [3]    Examine               |")
            print("| [4]    Run(%)                |")
            print(">-----------------------------------------------<")
        if self.enemy.dialogue:
            time.sleep(0.6)
            pushtext(self.enemy.dialogue, cutscenemode=True, speed = 0.04, speaker=self.enemy.name)
            self.turndesc.append(f"{self.enemy.name}: {self.enemy.dialogue}")
            input()
        while self.player.health > 0 and self.enemy.health > 0:           
            self.displaycombat()
            if self.combatEnd == 1:
                return
      
         

    def displaycombat(self):        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(str(self.player.health) + "				" + str(self.enemy.health)) #replace with f strings
        print(str(self.player.name) + "				" + str(self.enemy.name))
        print("_________________________________________________")
        print(f"| {self.turndesc[-1]}")
        print(f"| {self.turndesc[-2]}")
        print(f"| {self.turndesc[-3]}")
        print(f"| {self.turndesc[-4]}")
        print(">-----------------------------------------------<")
        print("| [1]    Attack                |")
        if monsters.firstgoblin.health <= 0:
            print("| [2]    Magic                 |")
            print("| [3]    Items                 |")
            print("| [4]    Examine               |")
            print("| [5]    Run(%)                |")
            print(">-----------------------------------------------<")                       
        if monsters.firstgoblin.health > 0:
            print("| [2]    Items                 |")
            print("| [3]    Examine               |")
            print("| [4]    Run(%)                |")
            print(">-----------------------------------------------<")                 
        if self.combatEnd == 1:
            return    
        playerinput = getLowerInput()           

        if playerinput not in self.OptionNumber:
            print("Invalid input")
            input()

        if self.OptionNumber.get(playerinput) == CombatOption.attack:
            pushtext("you choose to attack")   
            playerdamage = Player.calcdamage(self.player, self.enemy.defense, self.enemy.speed)
            enemydamage = combatbehavior.goblinbehavior(self.enemy, self.player)
            self.combatturnhandler(playerdamage,enemydamage)
            #self.enemy.health -= damage
            #if self.enemy.health <= 0 
                #return
        
        if self.OptionNumber.get(playerinput) == CombatOption.magic:
            #send to combat handler
            print("you perform a magic attack")
            input()

        if self.OptionNumber.get(playerinput) == CombatOption.items:
            print("You open your bag:")
            input()
            
        if self.OptionNumber.get(playerinput) == CombatOption.examine:
            print(f"you examine {self.enemy.name}")
            input()
        #import pdb 
        #pdb.set_trace() 
        if self.OptionNumber.get(playerinput) == CombatOption.run:           
            run = random.randint(0, 3)
            match run:
                case 0:
                    pushtext("you make an attempt to run -"  )
                case 1:
                    pushtext("you attempt to escape -"  )
                case 2:
                    pushtext("you attempt to run away from the fight -"  )
                case 3:                   
                    pushtext("you attempt to flee -")

            runchance = random.randint(0,(max(self.enemy.level - self.player.level, 1)))
            match runchance:
                case 0:
                    pushtext("you successfully escape!")
                    self.turndesc.append(f"{self.player.name}" +": You flee from bottle.")
                    self.runaway(self.player)
                case 1:
                    pushtext("you manage to flee the battle!")
                    self.turndesc.append(f"{self.player.name}" +": You flee from bottle.")
                    self.runaway(self.player)
                case runchance if runchance >= 2:
                    if runchance == 2:
                        pushtext("and are unsuccessful in doing so.")
                        self.turndesc.append(f"{self.player.name}" +": You fail to run away.")
                    if runchance == 3:
                        pushtext("but you don't find an opening for escape.")
                        self.turndesc.append(f"{self.player.name}" +": You fail to run away.")
                    if runchance > 4:                      
                        pushtext("but you end up tripping over your shoelace.")
                        self.turndesc.append(f"{self.player.name}" +": You fail to run away.")
                case _:
                    pushtext("error")

   
    
    
    def combatturnhandler (self, playeraction = None, enemyaction = None):
        self.playeraction = playeraction
        self.enemyaction = enemyaction
        pushtext("Debug playerdamage, roll: " + str(playeraction))
        pushtext("Debug enemydamage, roll: " + str(enemyaction))
        
        if self.player.speed >= self.enemy.speed:       
            if playeraction[1] == 0:
                    pushtext("Your attack misses!")
            if playeraction[1] == 10:
                    pushtext("Critical strike!") 
            pushtext("you do " + str(playeraction[0]) + " damage") 
            self.enemy.health -= playeraction[0]

            if self.enemy.health >0:
                if type(enemyaction[0]) == int:
                    if enemyaction[1] == 0:
                        pushtext("The enemy misses!")
                    if enemyaction[1] == 10:
                        pushtext("The enemy lands a critical strike!")                          
                    pushtext("the enemy does " + str(enemyaction[0]) + " damage")
                    self.player.health -= enemyaction[0]
            
                if type(enemyaction[0]) != int:
                    pushtext(str(enemyaction[0]))
                    if enemyaction[1] == 1:
                        print(self.enemy.drops[0])
                        self.enemy.drops[0].consume(self.enemy)
                        pushtext("goblin hopefully consumed apple")
                        del self.enemy.drops[0]
                    if enemyaction[1] == 2:
                        print("goblin rolled a 2")
            else:
                pushtext("You defeated " + self.enemy.name + "!")
                return
        if self.enemy.speed > self.player.speed: 
            if type(enemyaction[0]) == int:
                if enemyaction[1] == 0:
                    pushtext("The enemy misses!")
                if enemyaction[1] == 10:
                    pushtext("The enemy lands a critical strike!")                          
                    pushtext("the enemy does " + str(enemyaction[0]) + " damage")
                    self.player.health -= enemyaction[0]
            
                if type(enemyaction[0]) != int:
                    print(str(enemyaction[0]))
                    if enemyaction[1] == 1:
                        print(self.enemy.drops[0])
                        self.enemy.drops[0].consume(self.enemy)
                        pushtext("goblin hopefully consumed apple")
                        del self.enemy.drops[0]
                    if enemyaction[1] == 2:
                        print("goblin rolled a 2")
            if self.player.health >0:
                if playeraction[1] == 0:
                    pushtext("Your attack misses!")
                if playeraction[1] == 10:
                    pushtext("Critical strike!") 
                pushtext("you do " + str(playeraction[0]) + " damage") 
                self.enemy.health -= playeraction[0]
            else:
                pushtext("You died")
                return
         