import monsters
import players
import random
import item
import combat
from utils import pushtext

def goblinbehavior(enemy, player):
    chance = random.randint(1,10)
    pushtext("Debug Enemy rolled a " + str(chance) + " to determine ai")
    
    if enemy.health < player.attack:       #if monster health is lower than your attack stat, 60% chance monster will consume an item if they have one.        
        if chance <= 6:
            if enemy.drops:
                if enemy.drops[0].consumable == True:
                    action = "The enemy fake consumes one of its items."
                    return action, 1
                else:
                    action = enemy.calcdamage(player.getArmorRating(), player.speed)
                    return action
        if chance >6 and chance <= 8:
            action ="The Goblin growls menacingly at you - increasing its attack by 1."
            enemy.attack += 1
            return action, 2
        if chance >8:
            action = enemy.calcdamage(player.getArmorRating(), player.speed)
            return action

    if player.level - enemy.level >= 3:  #if player is 3 levels higher, monster has 10% chance of runaway, and 70% chance to do damage, 10% to growl
        if chance <= 1:
            action = "The goblin flees from battle!"
            return action, 3
        if chance > 1 and chance <= 8:
            action = enemy.calcdamage(player.getArmorRating(), player.speed)
        if chance > 8:
            action = "The Goblin growls menacingly at you - increasing its attack by 1."
            return action, 2

    if player.health < enemy.attack: 
        if chance <= 2:
            action = enemy.calcdamage(player.getArmorRating(), player.speed)
            return action 
        if chance > 2 and chance <=8:
            action = "The Goblin growls menacingly at you - increasing its attack by 1."
            return action, 2
        if chance >8:
            if enemy.drops:
                if enemy.drops[0].consumable == True:
                    action = "The enemy consumes one of its items"
                    return action, 1

    if enemy.level > player.level:  #if monster level is greater than player's level, 70% chance of attack, 30% growl
        if chance <= 3:
            action = "The Goblin growls menacingly at you - increasing its attack by 1."
            return action, 2
        if chance > 4:
            action = enemy.calcdamage(player.getArmorRating(), player.speed)
            return action
    else:                           #default 70% chance of attack
        if chance <= 3:
            action = "The Goblin growls menacingly at you - increasing its attack by 1."
            return action, 2
        if chance > 3:
            action = enemy.calcdamage(player.getArmorRating(),player.speed)
            return action