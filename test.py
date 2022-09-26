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

p = player.Player(rooms.r6, name = "jeff")
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
rooms.r8.addnpc(npcs.tempend)

while rooms.r7.entered == False:        #Spawn wandering goblin once player enters room 7
    p.location.displayroom(p)
pushtext("You get in the way of me picking my color plants!", "Wandering Goblin", 0.03)
pushtext("Rude humans must pay!", "Wandering Goblin", 0.03)
pushtext("It seems like you've interrupted this goblin's day out flower picking.")
pushtext("The goblin hobbles closer to you, before he starts throwing small stones in your general direction.")
goblinencounter = combat.Combat(p, monsters.wanderinggoblin,bound = True)
goblinencounter.startcombat()

while quests.secondquest.complete == 0:
    p.location.displayroom(players.player)

