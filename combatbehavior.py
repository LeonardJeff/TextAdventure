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
    if enemy.name == "Wandering Goblin" or enemy.name == "Goblin":
        chance = random.randint(1,10)
        #pushtext("Debug Enemy rolled a " + str(chance) + " to determine ai")

        if enemy.health < (enemy.maxhealth/2):       #if monster health is lower than half of its max, 60% chance monster will consume an item if they have one.        
            if chance <= 6:
                if enemy.inventory:
                    if enemy.inventory[0] != None and enemy.inventory[0].consumable == True:
                        action = [1, f"The enemy consumes its {enemy.inventory[0].name}."]
                        return action
                else:
                    subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                    action = [4, subaction[0], subaction[1]]
                    return action
            if chance >6 and chance <= 8:
                action =[2,"The Goblin growls menacingly at you", 2]
                enemy.attack += 2
                return action
            if chance >8:
                subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                action = [4, subaction[0], subaction[1]]
                return action

       # if player.level - enemy.level >= 3:  #if player is 3 levels higher, monster has 10% chance of runaway, and 70% chance to do damage, 10% to growl
       #     if chance <= 1:                   remains unimplemented as levels don't really exist yet.  
       #         action = [3, "The goblin flees from battle!"]
       #         return action
       #     if chance > 1 and chance <= 8:
       #         subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
       #         action = [4, subaction[0], subaction[1]]
       #         return action
       #     if chance > 8:
       #         action = [2, "The Goblin growls menacingly at you", 2]
       #         enemy.attack += 2
       #         return action

        if player.health < enemy.attack:        #if player health is less than an enemy's attack stat
            if chance <= 2:
                subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                action = [4, subaction[0], subaction[1]]
                return action 
            if chance > 2 and chance <=8:
                action = [2, "The Goblin growls menacingly at you", 1]
                enemy.attack += 1
                return action
            if chance > 8:
                if enemy.inventory:
                    if enemy.inventory[0] != None and enemy.inventory[0].consumable == True:
                        action = [1, f"The enemy consumes its {enemy.inventory[0].name}."]
                else:
                    action = [3, "Instead of attacking you, the goblin decides to torment you.", "Goblin: Heh heh, stupid human!", "The goblin points and laughs"]
                return action

        #if enemy.level > player.level:  #if monster level is greater than player's level, 70% chance of attack, 30% growl
        #    if chance <= 3:              remains unimplemented as levels don't really exist yet.  
         #       action = [2, "The Goblin growls menacingly at you", 2]
          #      return action
           # if chance >= 4:
            #    subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
             #   action = [4, subaction[0], subaction[1]]
              #  return action
       # else:                           #default 70% chance of attack
        #    if chance <= 3:
         #       action = [2, "The Goblin growls menacingly at you", 2]
          #      return action
           # if chance > 3:
            #    subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
             #   action = [4, subaction[0], subaction[1]]
              #  return action
        else:                           #default 70% chance of attack
            if chance <= 3:
                action = [2, "The goblin growls menacingly at you", 2]
                enemy.attack += 2
                return action
            if chance > 3:
                subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                action = [4, subaction[0], subaction[1]]
                return action    
    
    if enemy.name == "Bee":
        chance = random.randint(1,10)

        if player.health < enemy.attack:        #if player health is less than an enemy's attack stat
            if chance <= 3:
                subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                action = [4, subaction[0], subaction[1]]
                return action 
            if chance > 3 and chance < 7:
                action = [2, "The Bee buzzes menacingly at you", 1]
                enemy.attack += 1
                return action
            if chance >= 7:
                action = [3, "The Bee circles around you aggresively, accomplishing nothing.", "But it looks pretty scary doing it."]
                enemy.attack += 2
                return action

        if enemy.health < (enemy.maxhealth/2):       #if monster health is lower than half of its max, 60% chance monster will consume an item if they have one.        
            if chance <= 6:
                subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                action = [4, subaction[0], subaction[1]]
                return action
            if chance > 6:
                action =[2,"The Bee buzzes nervously at you", 1]
                enemy.attack += 1
                return action
        else:                           #default 70% chance of attack
            if chance <= 3:
                action = [2, "The Bee buzzes menacingly at you", 1]
                enemy.attack += 1
                return action
            if chance > 3:
                subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                action = [4, subaction[0], subaction[1]]
                return action    
    
    if enemy.name == "Plains Coyote":
        chance = random.randint(1,10)
        #pushtext("Debug Enemy rolled a " + str(chance) + " to determine ai")

        if player.health < enemy.attack:        #if player health is less than an enemy's attack stat
            if chance <= 3:
                subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                action = [4, subaction[0], subaction[1]]
                return action 
            if chance > 3 and chance < 7:
                action = [2, "The Coyote growls menacingly at you", 2]
                enemy.attack += 2
                return action
            if chance >= 7:
                action = [3, "The Coyote circles around you, accomplishing nothing.", "But it looks pretty scary doing it."]
                enemy.attack += 2
                return action

        if enemy.health < (enemy.maxhealth/2):       #if monster health is lower than half of its max, 60% chance monster will consume an item if they have one.        
            if chance <= 6:
                subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                action = [4, subaction[0], subaction[1]]
                return action
            if chance > 6:
                action =[2,"The Coyote nervously growls at you", 1]
                enemy.attack += 1
                return action
        else:                           #default 70% chance of attack
            if chance <= 3:
                action = [2, "The Coyote growls menacingly at you", 2]
                enemy.attack += 2
                return action
            if chance > 3:
                subaction = enemy.calcdamage(player.getArmorRating(), player.speed)
                action = [4, subaction[0], subaction[1]]
                return action    
    
    
    
    if enemy.name == "Woods Demon":       
        if turn == 0:
            action = [5, "The creature shrieks - summoning roots around your body making it impossible to escape.",
            "The Woods Demon has prevented you from being able to run away."]    
            return action
        if turn == 1:
            action = [2, "The Woods Demon screeches -", 2]
            return action
        if turn == 2:
            action = [3, "The Woods Demon looks up to the sky and raises its hands - it seems to be charging up... something.", "The Woods Demon is charging up!"]
            return action
        if turn == 3:
            action = [6, "The Woods Demon looks down at you. The demon forms both his hands into fists and points his arms towards you.", "You begin to feel rumbling beneath your feet.", "Large vines begin to encircle you, you see one begin to wind up and -", "THWACK!", "..."]
            return action