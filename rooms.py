from room import *
import quests

r1 = Room(1, "at the Construction Site", )

r2 = Room(2, "in a Grassy Field", 
firstenter = "You walk south towards where Frank told you the wood planks would be." )

r3 = Room(3, "in the Deep woods", 
access = 0,
lockdesc = "You probably should listen to your boss and get those planks from the pile over there to the south.", 
lockreq = quests.firstquest, 
firstenter = "As you enter into the deep woods, you notice multiple workers who seem to have been knocked out.")

r4 = Room(4, "in the Grassy Outskirts",)

r5 = Room(5, "in an open field." )

r6 = Room(6, "at Lily's parent's house.", )

r7 = Room(7, "at the edge of Frank's property.", )

r8 = Room(8, "in West Galawyn Plains.", )

r9 = Room(9, "in the unfinished trap room", )

r10 = Room(10, "in Galawyn Plains", )

r11 = Room(11, "in Galawyn Plains", ) #make sure to include obvious scenery differences

r12 = Room(12, "at a goblin campsite", )

r13 = Room(13, "at North Galawyn Plains", )

r1.setNeighbors(nroom=r3, sroom=r2)

r2.setNeighbors(nroom=r1)

r3.setNeighbors(sroom=r1)

r4.setNeighbors(nroom=r5)

r5.setNeighbors(wroom=r6)

r6.setNeighbors(eroom=r5)

r7.setNeighbors(nroom=r8, sroom=r5)

r8.setNeighbors(nroom=r9, sroom=r5)