import os
class Combat:
    def __init__(self, player, enemy):
        # start with text explain the fight beginning
        while player.health > 0 and enemy.health > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(str(player.health) + "				" + str(player.health))
            print(str(player.name) + "				" + str(player.name))
            print("_________________________________________________")
            print("|")  #mostrecentaction
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print(">-----------------------------------------------<")
            print("| [1]    Attack					|")
            print("| [2]    Items					|")
            print("| [3]    Examine  				|")
            print("| [4]    Run(50%)                |")
            print(">-----------------------------------------------<")
        
            """

            display options
            parse user input
            do action based on user input
            enemy does action

            """