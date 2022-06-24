from players import *
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
    player.setname("Gabe")
    pushtext("... So you're the silent type?","???: ")
    print("The man looks down at his clipboard.")
    pushtext("...well bud, the only name I don't recognize on here is Gabe. So you must be Gabe.","???")
player.setname(name)

from rooms import *
from npcs import *
from quests import *
from quest import *
from globalvars import *
r1.addnpc(Frank1)
r2.addnpc(Lily1)
r2.addnpc(Peggy)

r1.additem(axe)
r2.additem(woodenplanks)
r2.additem(woodenplanks)
r3.additem(axe)

r3.addnpc(Man1)

r2.addscenery(firstrock)  

r1.setNeighbors(nroom=r3, sroom=r2)
r2.setNeighbors(nroom=r1)
r3.setNeighbors(sroom=r1)
r4.setNeighbors(nroom=r5)

player.location = (r1)

pushtext(f"{player.name}? {player.name}... I think I've heard my daughter mention your name before.","???")
pushtext("Anyway, my name is Frank, but you can call me sir. I've been working construction for 12 years and I've never had a worse first impression for a new-hire of mine.","Frank")
pushtext(f"Well {player.name}, If you want to get paid for your time here today, start by fetching me some planks from the drop-off point to the south of here.","Frank")
firstquest.addquest(Frank1, player) 
while firstquest.complete == 0:
    player.location.displayroom(player)
   
pushtext("Ahhhhhh!!!!", speed=0.035)
#wait 1 seconds
pushtext("\nYou hear screams from the windmill north of you.", speed=0.035)
#wait 1 second
while player.health > 0:
    #if combat == True:
        player.location.displayroom(player) 
    

#while p.health>0: ##& combat == False:
    #p.location.displayroom(p)
    