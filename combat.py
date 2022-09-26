import os
import Monster
from equippable import Armor
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
from weapon import Weapon

class CombatOption(Enum):
            attack = 1
            items = 2
            examine = 3
            run = 4
            magic = 5
            jump = 6


class Combat:
    
    def __init__(self,player,enemy, bound = False):
        self.player = player
        self.enemy = enemy
        self.turn = 0
        self.bound = bound
        self.turndesc = ["","","","",""]               
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
            pushtext(f"You were defeated by {self.enemy.name}!")
            pushtext("How unfortunate. You died.")
            sys.exit(0) 
        if self.enemy.health <= 0:
            pushtext("You defeated " + self.enemy.name + "!")
            self.combatEnd = 1
            return True
        if self.combatEnd == 1:
            return True

        
        
    def startcombat(self):      
        if self.combatEnd == 1:
            return
        if monsters.wanderinggoblin.health <= 0:
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
        if monsters.wanderinggoblin.health <= 0:
            print("| [2]    Magic                 |")
            print("| [3]    Items                 |")
            print("| [4]    Examine               |")
            print("| [5]    Run                   |")
        if monsters.wanderinggoblin.health > 0:
            print("| [2]    Items                 |")
            print("| [3]    Examine               |")
            print("| [4]    Run                   |")
            print(">-----------------------------------------------<")
        if self.enemy.dialogue:
            time.sleep(0.3)
            pushtext(self.enemy.dialogue, cutscenemode=True, speed = 0.04, speaker=self.enemy.name)
            self.turndesc.append(f"{self.enemy.name}: {self.enemy.dialogue}")
            input()

        
        while self.combatEnd == 0:
            if self.checkstate():
                break
            else:
                self.displaycombat()
        #       if self.player.health <= 0:
        #        pushtext("!!!")
        #        pushtext(f"You've been defeated by {self.enemy.name}")
        #        return
        #    if self.enemy.health <= 0:
        #        pushtext("You defeated " + self.enemy.name + "!")
        #    if self.combatEnd == 1:
        #        break
        #    self.displaycombat()
        
      
         

    def displaycombat(self):        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(str(self.player.health) + "				" + str(self.enemy.health)) #replace with f strings
        print(str(self.player.name) + "				" + str(self.enemy.name))
        print("_____________________________________________________________")
        print(f"| {self.turndesc[-1]}")
        print(f"| {self.turndesc[-2]}")
        print(f"| {self.turndesc[-3]}")
        print(f"| {self.turndesc[-4]}")
        print(f"| {self.turndesc[-5]}")
        ##print(str(self.turn)) for bug testing the turn system.
        print(">-----------------------------------------------------------<")
        print("| [1]    Attack                |")
        if monsters.wanderinggoblin.health <= 0:
            print("| [2]    Magic                 |")
            print("| [3]    Items                 |")
            print("| [4]    Examine               |")
            print("| [5]    Run                   |")
            print(">-----------------------------------------------------------<")                       
        if monsters.wanderinggoblin.health > 0:
            print("| [2]    Items                 |")
            print("| [3]    Examine               |")
            print("| [4]    Run                   |")
            print(">-----------------------------------------------------------<")                 
         
        playerinput = getLowerInput()           

        if playerinput not in self.OptionNumber:
            pushtext("Invalid input")
            return

        if self.OptionNumber.get(playerinput) == CombatOption.attack:
            pushtext("You choose to attack.")   
            playerdamage = Player.calcdamage(self.player, self.enemy.defense, self.enemy.speed)
            enemydamage = combatbehavior.ai(self.enemy, self.player, self.turn)
            self.combatturnhandler(playerdamage,enemydamage)
        
        if self.OptionNumber.get(playerinput) == CombatOption.magic:
            if self.player.magiclevel <= 5:
                print("You concentrate your unknown energy from within into a concentrated form at your fingertips -")
                playerdamage = Player.calcmagic(self.player, self.enemy.defense, self.enemy.speed)
                enemydamage = combatbehavior.ai(self.enemy, self.player, self.turn)
                self.combatturnhandler(playerdamage,enemydamage)

        if self.OptionNumber.get(playerinput) == CombatOption.items:
            pushtext("You open your bag:")
            playerdamage = None
            while playerdamage == None:
                playerdamage = self.player.openinv()
            if playerdamage[0] == "exit":
                self.displaycombat()
            if playerdamage[0] == "item" or playerdamage[0] == "weapon" or playerdamage[0] == "armor":
                enemydamage = combatbehavior.ai(self.enemy, self.player, self.turn)
                self.combatturnhandler(playerdamage, enemydamage)
            
        if self.OptionNumber.get(playerinput) == CombatOption.examine:
            pushtext(f"You examine the {self.enemy.name}:")
            pushtext(self.enemy.examine)            #include in this stats about the monster
        #import pdb 
        #pdb.set_trace() 
        
        if self.OptionNumber.get(playerinput) == CombatOption.run:                       
            if self.bound == True: #If trapped in battle by the enemy, make it impossible to run
                run = 4
            else:
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
                case 4:
                    pushtext("Your enemy prevents you from escaping!")
                    return

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
                    enemydamage = combatbehavior.ai(self.enemy, self.player, self.turn)
                    if runchance == 2:
                        pushtext("and are unsuccessful in doing so.")
                        self.combatturnhandler("failedrun", enemydamage)
                    if runchance == 3:
                        pushtext("but you don't find an opening for escape.")
                        self.combatturnhandler("failedrun", enemydamage)
                    if runchance > 4:                      
                        pushtext("but you end up tripping over your shoelace.")
                        self.combatturnhandler("failedrun", enemydamage)
                case _:
                    pushtext("error during runaway")

   
    def enemyattack (self, enemyturn):
        if enemyturn[0] == 1:   #uses item
            pushtext(f"The {self.enemy.name} consumed its {self.enemy.inventory[0]}!")
            self.enemy.inventory[0].consume(self.enemy)
            self.turndesc.append(f"The {self.enemy.name} consumed its {self.enemy.inventory[0]}.")
            
        
        if enemyturn[0] == 2:   #Enemy Growl (?)
            pushtext(enemyturn[1])
            self.enemy.attack += enemyturn[2]
            pushtext(f"The {self.enemy.name} raised their attack by {str(enemyturn[2])}!")
            pushtext(f"The {self.enemy.name} now has {self.enemy.attack} attack.")
            self.turndesc.append(f"The {self.enemy.name} raised their attack to {self.enemy.attack}")

        if enemyturn[0] == 3:   #Text only
            for text in enemyturn[1:]:
                pushtext(text)
                self.turndesc.append(text)
        
        if enemyturn[0] == 4:   #normal attack only
            pushtext("The enemy chooses to attack!")
            if enemyturn[2] == 0:
                pushtext(f"The {self.enemy.name} misses!")
            if enemyturn[2] == 10:
                pushtext(f"The {self.enemy.name} lands a critical strike!")                          
            pushtext("the enemy does " + str(enemyturn[1]) + " damage")
            self.player.health -= enemyturn[1]
            self.turndesc.append(f"{self.enemy.name} does {enemyturn[1]} damage to you.")
        
        if enemyturn[0] == 5:   #Bind player to battle
            for text in enemyturn[1:]:
                pushtext(text)
            self.bound = True
            self.turndesc.append(f"{self.enemy.name} traps you into the battle!") 
        
        if enemyturn[0] == 6:   #Kick player out of battle (No winners to battle)
            for text in enemyturn[1:]:
                pushtext(text)
            self.combatEnd = 1
            return
    
    def combatturnhandler (self, playerturn = None, enemyturn = None):
        self.playerturn = playerturn
        self.enemyturn = enemyturn
        os.system('cls' if os.name == 'nt' else 'clear')
        #pushtext("Debug playerturn, roll: " + str(playerturn))      Debug purposes
        #pushtext("Debug enemyturn, roll: " + str(enemyturn))
        
        if playerturn[0] == "failedrun":                     #FIX THIS
            self.turndesc.append(f"{self.player.name}" +"| You fail to run away.")
            self.turn+=1
           
        
        if playerturn[0] == "weapon":
            pushtext(f"You equip your {str(playerturn[1])}.")
            self.turndesc.append(f"{self.player.name}| You equipped: {str(playerturn[1])}")
            self.turn+=1
       
        
        if playerturn[0] == "armor":
            pushtext(f"You equipped the {str(playerturn[1])}.")
            self.turndesc.append(f"{self.player.name}| You equipped: {str(playerturn[1])}")
            self.turn+=1
    

        if playerturn[0] == "item":     
            pushtext(f"You consume your {str(playerturn[1])}.")
            self.turndesc.append(f"{self.player.name}| You used: {str(playerturn[1])}")
            self.turn+=1
        
        if self.player.speed >= self.enemy.speed:  #if player is faster than enemy: player go first 
            if self.combatEnd == 0:
                if playerturn[0] == "physical":                         
                    if playerturn[2] == 0:
                        pushtext("Your attack misses!")
                    if playerturn[2] == 10:
                        pushtext("You land a critical strike!") 
                    pushtext("you do " + str(playerturn[1]) + " damage")
                    self.turndesc.append(f"You do {playerturn[1]} damage towards {self.enemy.name}.") 
                    self.enemy.health -= playerturn[1]
                    self.turn+=1

                if playerturn[0] == "magic":
                    pushtext("You feel the strange power from deep within you intensify.")
                    self.player.magiclevel+=1
                    pushtext("You do " + str(playerturn[1]) + " magic damage.")
                    self.turndesc.append(f"You do {playerturn[1]} magic damage towards {self.enemy.name}.") 
                    self.enemy.health -= playerturn[1]
                    self.turn+=1

                if self.enemy.health >0:    #if enemy survives your attack
                    self.enemyattack(enemyturn)                    
                    return

        if self.enemy.speed > self.player.speed: #if enemy is faster: enemy go first
            self.enemyattack(enemyturn)   #enemy attacks first
            if self.combatEnd == 0:
                if self.player.health >0:
                    if playerturn[0] == "physical":                         
                        if playerturn[2] == 0:
                            pushtext("Your attack misses!")
                        if playerturn[2] == 10:
                            pushtext("You land a critical strike!") 
                        pushtext("You do " + str(playerturn[1]) + " damage.") 
                        self.turndesc.append(f"You do {playerturn[1]} damage towards {self.enemy.name}.")
                        self.enemy.health -= playerturn[1]
                        self.turn+=1

                    if playerturn[0] == "magic":
                        pushtext("You feel the power from deep within you intensify.")
                        self.player.magiclevel+=1
                        pushtext("You do " + str(playerturn[1]) + " magic damage.")
                        self.turndesc.append(f"You do {playerturn[1]} magic damage towards {self.enemy.name}.") 
                        self.enemy.health -= playerturn[1]
                        pushtext(f"Your magic level has increased by 1. Your magic level is now {self.player.magiclevel}.")
                        self.turn+=1
                return
        
         