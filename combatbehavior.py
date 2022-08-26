import monsters
import players
import random
import item
import combat
from utils import pushtext

# 1 consume item action
# 2 growl action
# 3 text only action
# 4 damage only action
def ai(enemy, player, turn):
    if enemy.name == "Wandering Goblin":       
        chance = random.randint(1,10)
        pushtext("Debug Enemy rolled a " + str(chance) + " to determine ai")

        if enemy.health < (enemy.health/2):       #if monster health is lower than your attack stat, 60% chance monster will consume an item if they have one.        
            if chance <= 6:
                if enemy.drops:
                    if enemy.drops[0].consumable == True:
                        action = [1, "The enemy fake consumes one of its items."]
                        return action
                    else:
                        action = enemy.calcdamage(player.getArmorRating(), player.speed)
                        return action
            if chance >6 and chance <= 8:
                action =[2,"The Goblin growls menacingly at you - increasing its attack by 1."]
                enemy.attack += 1
                return action
            if chance >8:
                action = [4, enemy.calcdamage(player.getArmorRating(), player.speed)[0], enemy.calcdamage(player.getArmorRating(), player.speed)[1]]
                return action

        if player.level - enemy.level >= 3:  #if player is 3 levels higher, monster has 10% chance of runaway, and 70% chance to do damage, 10% to growl
            if chance <= 1:
                action = [3, "The goblin flees from battle!"]
                return action
            if chance > 1 and chance <= 8:
                action = [4, enemy.calcdamage(player.getArmorRating(), player.speed)[0], enemy.calcdamage(player.getArmorRating(), player.speed)[1]]
                return action
            if chance > 8:
                action = [2, "The Goblin growls menacingly at you - increasing its attack by 1."]
                return action

        if player.health < enemy.attack: 
            if chance <= 2:
                action = [4, enemy.calcdamage(player.getArmorRating(), player.speed)[0], enemy.calcdamage(player.getArmorRating(), player.speed)[1]]
                return action 
            if chance > 2 and chance <=8:
                action = [2, "The Goblin growls menacingly at you - increasing its attack by 1."]
                return action
            if chance >8:
                if enemy.drops:
                    if enemy.drops[0].consumable == True:
                        action = [1, "The enemy consumes one of its items"]
                        return action

        if enemy.level > player.level:  #if monster level is greater than player's level, 70% chance of attack, 30% growl
            if chance <= 3:
                action = [2, "The Goblin growls menacingly at you - increasing its attack by 1."]
                return action
            if chance >= 4:
                action = [4, enemy.calcdamage(player.getArmorRating(), player.speed)[0], enemy.calcdamage(player.getArmorRating(), player.speed)[1]]
                return action
        else:                           #default 70% chance of attack
            if chance <= 3:
                action = [2, "The Goblin growls menacingly at you - increasing its attack by 1."]
                return action
            if chance > 3:
                action = [4, enemy.calcdamage(player.getArmorRating(), player.speed)[0], enemy.calcdamage(player.getArmorRating(), player.speed)[1]]
                return action
    
    if enemy.name == "Woods Demon":       
        if turn == 0:
            action = [3, "The creature shrieks - summoning roots around your body making it impossible to escape.",
            "The Woods Demon has prevented you from being able to run away."]
            return action
        if turn == 1:
            action = [3, "The demon screeches -", "The demon raised its attack by 3!"]
            enemy.attack =+8
            pushtext("The enemy now has "+ str(enemy.attack) + " attack.", None, 0.07)
            return action
        if turn == 2:
            action = [3, "The demon 3rd move", "The demon raised itssdsdsdsd"]
            return action