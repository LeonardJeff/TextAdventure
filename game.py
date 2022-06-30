import players
from os import system
from fullscreen import *
from utils import *


system('mode con: cols=150 lines=100')
maximize_console()

pushtext("...", "???: ")
pushtext(" ... Hey. Buddy", "???")
pushtext("... Hey, BUDDY", "???")
pushtext("You begin to open your eyes. It probably wasn't smart to take a nap on the first day of your new job.")
pushtext("You stand up from your restful slumber in the tall grass.")
pushtext("Son what's your name. I can't be having new-hires sleeping on the job.", "???")
print("Enter your name:")
name = input()
if name == "":
    name = "Gabe"
    players.player.setName("Gabe")
    pushtext("... So you're the silent type?","???: ")
    print("The man looks down at his clipboard.")
    pushtext("...well bud, the only name I don't recognize on here is Gabe. So you must be Gabe.","???")
    players.player.setName(name)

import rooms
import npcs
import quests
import combat
import scenerys
import items
rooms.r1.addnpc(npcs.Frank1)
rooms.r2.addnpc(npcs.Lily1)
rooms.r2.addnpc(npcs.Peggy)

rooms.r1.additem(items.axe)
rooms.r1.additem(items.woodenplanks)
rooms.r2.additem(items.woodenplanks)
rooms.r2.additem(items.woodenplanks)
rooms.r3.additem(items.axe)

rooms.r3.addnpc(npcs.Man1) #unconcious man

rooms.r2.addscenery(scenerys.firstrock) 

rooms.r1.setNeighbors(nroom=rooms.r3, sroom=rooms.r2)
rooms.r2.setNeighbors(nroom=rooms.r1)
rooms.r3.setNeighbors(sroom=rooms.r1)
rooms.r4.setNeighbors(nroom=rooms.r5)

players.player.location = (rooms.r1)

pushtext(f"{players.player.name}? {players.player.name}... I think I've heard my daughter mention your name before.","???")
pushtext("Anyway, my name is Frank, but you can call me sir. I've been working construction for 12 years and I've never had a worse first impression for a new-hire of mine.","Frank")
pushtext(f"Well {players.player.name}, If you want to get paid for your time here today, start by fetching me some planks from the drop-off point to the south of here.","Frank")
quests.firstquest.addquest(npcs.Frank1, players.player) 
while quests.firstquest.complete == 0:
    players.player.location.displayroom(players.player)
   
pushtext("Ahhhhhh!!!!") #, speed=0.035, cutscenemode = True
time.sleep(1)
pushtext("\nYou hear screams from the windmill north of you.") #, speed=0.035, cutscenemode = True
time.sleep(1)
import monsters
Combattest = combat.Combat(players.player, monsters.goblin)
Combattest.startcombat(players.player,monsters.goblin)
while players.player.health > 0:
    Combattest.displaycombat(players.player,monsters.goblin)
    

#while p.health>0: ##& combat == False:
    #p.location.displayroom(p)
    