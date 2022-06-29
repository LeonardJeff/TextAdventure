import os
from player import Player
from utils import getLowerInput
from utils import pushtext
import time

class Combat:
    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 0
        self.turndesc = ["last","3rd","2nd","Mostrecent"]               

    def startcombat(self,player,enemy):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(str(player.health) + "				" + str(enemy.health))
        print(str(player.name) + "				" + str(enemy.name))
        print("\n_________________________________________________")
        print("|")
        print("|")
        print("|")
        print("|")
        print(">-----------------------------------------------<")
        print("| [1]    Attack                |")
        print("| [2]    Items                 |")
        print("| [3]    Examine               |")
        print("| [4]    Run(50%)              |")
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
        print("|")
        print("_________________________________________________")
        print(f"| {self.turndesc[-1]}")
        print(f"| {self.turndesc[-2]}")
        print(f"| {self.turndesc[-3]}")
        print(f"| {self.turndesc[-4]}")
        print(">-----------------------------------------------<")
        print("| [1]    Attack					|")
        print("| [2]    Items					|")
        print("| [3]    Examine  				|")
        print("| [4]    Run(50%)                |")
        print(">-----------------------------------------------<")
        
        playerinput = getLowerInput()

        if playerinput == "1":
            print("you choose to attack")
            input()
            return
        if playerinput == "2":
            print("you look in your bag")
            input()
            return
        if playerinput == "3":
            print("")
            input()
            return
        if playerinput == "4":
            print("4 has been pressed")
            input()
            return
        
    """
    display options
    parse user input
    do action based on user input
    enemy does action
        """