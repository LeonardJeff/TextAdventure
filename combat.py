import os
from player import Player
from utils import getLowerInput
from utils import pushtext
from enum import Enum
import time
import quests

class Combat:
    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 0
        self.turndesc = ["last","3rd","2nd","Mostrecent"]               
        self.OptionNumber = {}
        
    def startcombat(self,player,enemy):
        os.system('cls' if os.name == 'nt' else 'clear')
        #firstpart
        print(str(player.health) + "				" + str(enemy.health))
        print(str(player.name) + "				" + str(enemy.name))
        #second part
        print("_________________________________________________")
        print("|")
        print("|")
        print("|")
        print("|")
        #third part
        print(">-----------------------------------------------<")
        print("| [1]    Attack                |")
        if quests.firstquest.complete == True:
            print("| [2]    Magic                 |")
            print("| [3]    Items                 |")
            print("| [4]    Examine               |")
            print("| [5]    Run(%)                |")
        if quests.firstquest.complete == False:
            print("| [2]    Items                 |")
            print("| [3]    Examine               |")
            print("| [4]    Run(%)                |")
        print(">-----------------------------------------------<")
        if enemy.dialogue:
            time.sleep(0.6)
            pushtext(enemy.dialogue, cutscenemode=True, speed = 0.04, speaker=enemy.name)
            self.turndesc.append(f"{enemy.name}: {enemy.dialogue}")
            input()
        
    def displaycombat(self, player, enemy):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(str(player.health) + "				" + str(enemy.health))
        print(str(player.name) + "				" + str(enemy.name))
        print("_________________________________________________")
        print(f"| {self.turndesc[-1]}")
        print(f"| {self.turndesc[-2]}")
        print(f"| {self.turndesc[-3]}")
        print(f"| {self.turndesc[-4]}")
        print(">-----------------------------------------------<")
        print("| [1]    Attack                |")
        if quests.firstquest.complete == True:
            print("| [2]    Magic                 |")
            print("| [3]    Items                 |")
            print("| [4]    Examine               |")
            print("| [5]    Run(%)                |")
            print(">-----------------------------------------------<")
        if quests.firstquest.complete == False:
            print("| [2]    Items                 |")
            print("| [3]    Examine               |")
            print("| [4]    Run(%)                |")
            print(">-----------------------------------------------<")
        playerinput = getLowerInput()
        
        class CombatOption(Enum):
            attack = "1"
            items = "2"
            examine = "3"
            run = "4"
            magic = "5"
        
    
        OptionNumber ={
            "1" : CombatOption.attack,
            "2" : CombatOption.items, 
            "3" : CombatOption.examine, 
            "4" : CombatOption.run
            }
    
        if quests.firstquest.complete == True:
            OptionNumber["1"] = CombatOption.attack
            OptionNumber["2"] = CombatOption.magic, 
            OptionNumber["3"] = CombatOption.items, 
            OptionNumber["4"] = CombatOption.examine,
            OptionNumber["5"] = CombatOption.run,     
        
        if OptionNumber.get(playerinput) == CombatOption.attack:
                print("you choose to attack")
                input()

        if OptionNumber.get(playerinput) == CombatOption.magic: # = 5
                print("you look perform magic")
                input()
            
        if OptionNumber.get(playerinput) == CombatOption.examine:
                print("you examine the thing")
                input()
                
        if OptionNumber.get(playerinput) == CombatOption.run:
                print("you run")
                input()