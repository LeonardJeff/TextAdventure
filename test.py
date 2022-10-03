import players
from os import system
from fullscreen import *
from utils import *
import player
import combat
import monsters
import rooms
from items import *
from weapons import *
import scenerys
from equippables import *

p = player.Player(rooms.r5, name = "jeff")
p.health = 10
p.inventory.extend([mushroom,key1,apple,wildturnip,wildturnip,wildturnip,apple,wildturnip,wildturnip,wildturnip,
apple,mushroom,mushroom,axe,rustySword,ironSword,ironSword,ironSword,axe,steelSword,ironSword,axe,axe,axe, ironHelmet, testHelmet])

import rooms
import npcs
import quests
import combat
import scenerys
import items
import weapons
import equippables
rooms.r1.addnpc(npcs.Frank1)
rooms.r1.addnpc(npcs.worker1)
rooms.r1.additem(items.mushroom1)
rooms.r1.additem(equippables.ironHelmet)

rooms.r2.addnpc(npcs.Lily1)
rooms.r2.addnpc(npcs.Hubert1)
rooms.r2.addnpc(npcs.worker2)
rooms.r2.additem(items.woodenplanks)
rooms.r2.additem(items.woodenplanks)
rooms.r2.addscenery(scenerys.firstrock)


rooms.r3.addnpc(npcs.worker3) #unconcious man
rooms.r3.addnpc(npcs.worker4) #entangled worker
rooms.r3.additem(weapons.axe)

rooms.r4.addnpc(npcs.Hubert2)
rooms.r4.addscenery(scenerys.skidmarks)
rooms.r4.addscenery(scenerys.tempestlake)

rooms.r5.additem(items.key1)

rooms.r5.addscenery(scenerys.radishcroprow)
rooms.r5.addscenery(scenerys.cucumbercroprow)
rooms.r5.addscenery(scenerys.carrotcroprow)
rooms.r8.addnpc(npcs.Hunter)
rooms.r10.addscenery(scenerys.animalden)

rooms.r8.addnpc(npcs.tempend)
quests.secondquest.addquest(npcs.Hunter, p) 
rooms.r8.addscenery(scenerys.foresttreeline)

while rooms.r7.entered == False:        #Spawn wandering goblin once player enters room 7
    p.location.displayroom(p)
pushtext("You get in the way of me picking my color plants!", "Wandering Goblin", 0.03)
pushtext("Rude human must pay!", "Wandering Goblin", 0.03)
pushtext("It seems like you've interrupted this goblin's day out flower picking.")
pushtext("The goblin hobbles closer to you, before he starts throwing small stones in your general direction.")
goblinencounter = combat.Combat(p, monsters.wanderinggoblin)
goblinencounter.startcombat()

if monsters.wanderinggoblin.health <= 0:
    pushtext("\nAs you begin to reach for the flowers, you begin to feel a weird tingling coming from the palm of your hand.")
    pushtext("You unlocked Magic!", speaker = "Game")
    rooms.r7.addnpc(npcs.Eve1)
if monsters.wanderinggoblin.health >0:
    pushtext("As you flee the scene, you can see the goblin begin to lose interest, before it goes back to picking more flowers.")
    rooms.r7.addnpc(npcs.Eve2)
    rooms.r7.addnpc(npcs.wanderinggoblin)
while quests.thirdquest.complete == 0:
    p.location.displayroom(p)

