import players
from os import system
from fullscreen import *
from utils import *

tempvar = 0
system('mode con: cols=150 lines=100')
maximize_console()
time.sleep(0.4)
print("    ______       ___       __            ___   ____    __    ____  ____    ____  __   __ ")
print("   /  ____|     /   \     |  |          /   \  \   \  /  \  /   /  \   \  /   / |  \ |  |")   
print("  |  |  __     /  /\ \    |  |         /  /\ \  \   \/    \/   /    \   \/   /  |   \|  |")  
print("  |  | |_ |   /  /__\ \   |  |        /  /__\ \  \            /      \_    _/   |    `  |")
print("  |  \__| |  /  _____  \  |  |____   /  _____  \  \    /\    /         |  |     |  |\   |")   
print("   \______| /__/     \__\ |_______| /__/     \__\  \__/  \__/          |__|     |__| \__|") 
print("")
print("")
print("   By Jeff Leonard                                                           Version 1.1")       
#print("     _       _                 _                  _                     _                      ")
#print("    /_\     | |_   ___  __ __ | |_      __ _   __| | __ __  ___   _ _  | |_   _  _   _ _   ___ ")
#print("   / _ \    |  _| / -_) \ \ / |  _|    / _` | / _` | \ V / / -_) | ' \ |  _| | || | | '_| / -_)")
#print("  /_/ \_\    \__| \___| /_\_\  \__|    \__,_| \__,_|  \_/  \___| |_||_| \__|  \_,_| |_|   \___|")                                                                                  
print("")
print("")
input("                                 Press Enter to continue")
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)

pushtext("...", speed = 0.3, cutscenemode= True)
pushtext("... Hey. Buddy.","\n???",0.03)
pushtext("... Hey, BUDDY.", "???",0.03)
pushtext("You begin to open your eyes. It probably wasn't smart to take a nap on the first day of your new job.")
pushtext("You stand up from your restful slumber in the tall grass.")
pushtext("What's your name. I can't be having new-hires sleeping on the job.", "???", 0.035)
print("Enter your name:")
name = input()
if name == "":
    name = "Gabe"
    players.player.setName("Gabe")
    pushtext("... So you're the silent type?","???", 0.035)
    pushtext("The man looks down at his clipboard.")
    pushtext("...well bud, the only name I don't recognize on here is Gabe. So you must be Gabe.","???", 0.03)
players.player.setName(name)

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


rooms.r3.addnpc(npcs.worker3) #unconcsious man
rooms.r3.addnpc(npcs.worker4) #entangled worker
rooms.r3.additem(weapons.axe)

rooms.r4.addnpc(npcs.Hubert2)
rooms.r4.addscenery(scenerys.skidmarks)
rooms.r4.addscenery(scenerys.tempestlake)



players.player.location = (rooms.r1)

rooms.r6.additem(items.key1)

pushtext(f"{players.player.name}? {players.player.name}... I think I've heard my daughter mention your name before.","???", 0.03)
pushtext("Anyway, my name is Frank, but you can call me sir. I've been working construction for 12 years and I've never had a worse first impression for a new-hire of mine.","Frank", 0.03)
pushtext(f"Well {players.player.name}, If you actually want to get paid for helpin us with the flour-mill today, start by fetching me some planks from the drop-off point to the south of here.","Frank", 0.03)
quests.firstquest.addquest(npcs.Frank1, players.player) 
while quests.firstquest.complete == 0:
    players.player.location.displayroom(players.player)
   
pushtext("Ahhhhhhhh!!!!", speed=0.035, cutscenemode = True) 
time.sleep(1)
pushtext("\nYou hear screams from the windmill north of you.", speed=0.035, cutscenemode = True)
time.sleep(1)

import monsters
rooms.r3.addscenery(scenerys.flourmill)

while tempvar == 0:
    players.player.location.displayroom(players.player)
    if scenerys.flourmill.inspected == True:
        tempvar = 1
        break
          
players.player.location = (rooms.r4)
tempvar = 0

rooms.r5.addscenery(scenerys.radishcroprow)
rooms.r5.addscenery(scenerys.cucumbercroprow)
rooms.r5.addscenery(scenerys.carrotcroprow)
rooms.r5.addscenery(scenerys.bearcrow)
rooms.r5.addscenery(scenerys.gate1)

time.sleep(1)
pushtext(f"...", speed = 0.1, cutscenemode = True)
time.sleep(1)
pushtext(f"\n...", speed = 0.1, cutscenemode = True)
time.sleep(1)
pushtext(f"\n...", speed = 0.1, cutscenemode = True)
time.sleep(1)
pushtext(f"{players.player.name}?","\n???", 0.03, cutscenemode = True)
time.sleep(1)
pushtext(f"\n...", speed = 0.03, cutscenemode = True)
time.sleep(1.5)
pushtext(f"{players.player.name}?!","\nLily", 0.02, cutscenemode = True)
time.sleep(1)
pushtext(f"\nYou recognize the voice as Lily's as she frantically heads towards you")
pushtext(f"{players.player.name}! Wake up!","Lily", 0.02, cutscenemode = True)
time.sleep(1)
pushtext(f"\nYou begin to shiver as Lily pulls you out of what you now realize is a body water.")
pushtext(f"Lily shakes you vigorously.")
pushtext(f"...", speed = 0.1, cutscenemode = True)
time.sleep(1)
pushtext(f"\nAs you begin to wake up, you open your eyes to see Lily's troubled expression.", speed = 0.03)
pushtext(f"You feel butterflies in your stomach as she pulls you further onto land.", speed = 0.03)
pushtext(f"{players.player.name}! I thought you were a goner! That forest spirit sent you flying!","Lily", 0.03)
pushtext(f"As Lily lays you on your side, you cough up a small minnow.", speed = 0.03)
pushtext(f"Despite coughing up a live fish, you still feel a weird sensation from deep within your stomach.", speed = 0.03)
pushtext(f"Lily waits for you to say something - but quickly remembers that you're not much of a talker.", speed = 0.03)
pushtext(f"You know, it was a pretty dumb idea to attack that forest spirit. When they get angry, there's not much that can calm them down.","Lily", 0.03)
pushtext(f"... What? You think it was a demon? Nonsense, what would a demon be doing at a construction site?","Lily", 0.03)
pushtext(f"Well, you seem to be in good shape despite being flung this far away from the flour mill.","Lily", 0.03)
pushtext(f"The sun is going to set soon, if you'd like a place to stay tonight, I'm sure my parents wouldn't mind if you stayed at our house for the night.","Lily", 0.03)
pushtext(f"Our house is a little bit north of here. Lets get going before goblins and other animals start to come out.","Lily", 0.03)
pushtext(f"I'll meet you there!","Lily", 0.03)
pushtext(f"Lily runs off - leaving you to fend for yourself.")

rooms.r6.addscenery(scenerys.farmersalmanac)
rooms.r6.addnpc(npcs.Peggy)
rooms.r6.addnpc(npcs.Frank2)
rooms.r6.addnpc(npcs.Lily2)

while rooms.r6.entered == False:        #Start lily's house cutscene
    players.player.location.displayroom(players.player)
pushtext(f"You must be {players.player.name}!!", speaker = "Peggy", speed = 0.03)
pushtext("You see your boss Frank do a double-take peek out from the corner of a doorway.")
pushtext(f"Oh uh {players.player.name}. Hi. Glad to see you made it out of that demon fight in one peice.", speaker = "Frank", speed = 0.03)
pushtext(f"Once I heard the screaming from the flour mill, like any good boss would do, I carried two of my men on my back and booked it out of there.", speaker = "Frank", speed = 0.03)
pushtext(f"Oh didja now sweetie?", speaker = "Peggy", speed = 0.03)
pushtext(f"I'm pretty sure you made it back home before I heard that loud crash at the lake. Where'd you bring those two guys??", speaker = "Peggy", speed = 0.03)
pushtext(f"Oh uh, I dropped them off at the infirmary in Galawyn before I came back. They were really hurt, so I made sure to get them there quick. Like any good boss would do.", speaker = "Frank", speed = 0.025)
pushtext(f"I would've come back for you {players.player.name}, but I knew Lily would make sure you made it out safe. She had her eyes on you the whole -", speaker = "Frank", speed = 0.03)
pushtext([f"Frank!", "Shut it!"], speaker = "Peggy", speed = 0.03)
pushtext("Dad!", speaker = "Lily", speed = 0.03)
pushtext(f"Well ah, {players.player.name}, if you'd like your pay for today, I'm afraid you'll need to go to the bank in Galawyn to cash this promissory note in.", speaker = "Frank", speed = 0.03)
pushtext("Frank hands you an official looking peice of paper.")
pushtext([f"You're going to make {players.player.name} go all the way to Galawyn!?", f"The whole city has been on high-alert for the past couple of days, {players.player.name} wouldn't even be able to get past the guards!"], speaker = "Peggy", speed = 0.03)
pushtext(f"Nonesense. All these demon sightings have the city on high alert for demons. Not kids.", speaker = "Frank", speed = 0.03)
pushtext(["...", f"{players.player.name}, there should be a key somewhere near the front door. It will open the gate leading you to Galawyn.", 
"Be careful though sweetie. We have that gate for a reason. All sorts of scary wildlife is out there."], speaker = "Peggy", speed = 0.03)
pushtext("Stay safe sweetie!", speaker = "Peggy", speed = 0.03)


while rooms.r7.entered == False:        #Spawn wandering goblin once player enters room 7
    players.player.location.displayroom(players.player)
pushtext("You get in the way of me picking my color plants!", "Wandering Goblin", 0.03)
pushtext("Rude human must pay!", "Wandering Goblin", 0.03)
pushtext("It seems like you've interrupted this goblin's day out flower picking.")
pushtext("The goblin hobbles closer to you, before he starts throwing small stones in your general direction.")
goblinencounter = combat.Combat(players.player, monsters.wanderinggoblin)
goblinencounter.startcombat()

if monsters.wanderinggoblin.health <= 0:
    pushtext("As you begin to reach for the flowers, you begin to feel a weird tingling coming from the palm of your hand.")
    pushtext("You unlocked Magic!", speaker = "Game")
    rooms.r7.addnpc(npcs.Eve1)
if monsters.wanderinggoblin.health >0:
    pushtext("As you flee the scene, you can see the goblin begin to lose interest, before it goes back to picking more flowers.")
    rooms.r7.addnpc(npcs.Eve2)
    rooms.r7.addnpc(npcs.wanderinggoblin)

quests.secondquest.addquest(npcs.Hunter, players.player)     
rooms.r8.addnpc(npcs.Hunter)
rooms.r7.addscenery(scenerys.foresttreeline)
rooms.r10.addscenery(scenerys.animalden)
rooms.r10.additem(items.wildturnip)
rooms.r11.additem(items.wildturnip)

rooms.r13.addnpc(npcs.tempend)
rooms.r13.additem(weapons.aduriteGreatSword)
rooms.r13.additem(weapons.rustywoodenstick)
rooms.r13.additem(equippables.aduriteArmor)
rooms.r13.additem(equippables.victoryring)
rooms.r13.addnpc(npcs.Hubert3)

while quests.thirdquest.complete == 0:
    players.player.location.displayroom(players.player)

  

    

#while p.health>0: ##& combat == False:
    #p.location.displayroom(p)
    