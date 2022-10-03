from room import *
import quests
import items

r1 = Room(1, "at the Construction Site", )

r2 = Room(2, "in a Grassy Field", 
firstenter = "You walk south towards where Frank told you the wood planks would be, and meet up with other people helping with the project." )

r3 = Room(3, "at the Flour Mill", 
access = 0,
lockdesc = "You probably should listen to your boss and get those planks from the pile over there to the south.", 
lockreq = quests.firstquest, 
firstenter = ["As the flour mill comes into your view, you notice roots rising up and wrapping around the unfinished structure.",
"As you get closer, you can see multiple workers who lay in front of it.", 
"They seem to be knocked out cold."])

r4 = Room(4, "at Tempest Lake",
)

r5 = Room(5, "outside Lily's house.", 
firstenter= ["You follow the direction Lily headed, just as you think you caught up to her, you see her head inside the house to the west."],
)

r6 = Room(6, "in Lily's house.",
firstenter= ["As you approach the front of Lily's house, you consider knocking on the slightly open door,", 
"But you're not sure if would knocking would be the polite thing to do. After all, you just saw Lily go in...",
"But it would be rude just to barge in...",
f"You grab the handle of the door, so that you can pull a smooth \"Knock and enter\" maneuver.",
"Your knocks seem to go unheard, but you've already started to walk in.",
"Oh well."],
)

r7 = Room(7, "at the edge of Frank's property.",
itemlockreq = items.key1,
access = False,
lockdesc = "You're going to need a key to get past the gate in this direction.",
firstenter = ["You take the key from your pockets, and insert it into the giant lock on the gate.", 
"The screech of the gate opening seems to have garnered the attention of a stray goblin."])

r8 = Room(8, "in West Galawyn Plains.", access = False, lockdesc = "A mysterious force stops you from exploring north. Maybe you'll be able to go here in future releases of the game!")

r9 = Room(9, "in the unfinished trap room", )

r10 = Room(10, "in Galawyn Plains", )

r11 = Room(11, "in East Galawyn Plains", ) #make sure to include obvious scenery differences

r12 = Room(12, "at the goblin campsite", )

r13 = Room(13, "at North Galawyn Plains", access = False, lockreq = quests.secondquest, 
lockdesc = "You're going to need a key to get past the gate in this direction.",
firstenter = ["You take the key from your pockets, and insert it into the giant lock on the gate.", "The door screeches open."])

r14 = Room(14, "in the city of Galawyn",
access = False,
lockreq = quests.thirdquest,    #doesn't exist yet >:) heh heh
lockdesc = "It seems somebody hasn't coded the city of Galawyn yet... stay tuned!" )
r1.setNeighbors(nroom=r3, sroom=r2)
r2.setNeighbors(nroom=r1)
r3.setNeighbors(sroom=r1)
r4.setNeighbors(nroom=r5)
r5.setNeighbors(nroom=r7, sroom = r4, wroom=r6)
r6.setNeighbors(eroom=r5)
r7.setNeighbors(nroom=r8, sroom=r5)
r8.setNeighbors(nroom=r9,eroom=r10,sroom=r7)
r9.setNeighbors(sroom=r8)
r10.setNeighbors(eroom=r11,wroom=r8)
r11.setNeighbors(nroom=r13,eroom=r12,wroom=r10)
r12.setNeighbors(wroom=r11)
r13.setNeighbors(sroom=r11, nroom=r14)
r14.setNeighbors(sroom=r13)