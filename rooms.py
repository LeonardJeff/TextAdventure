from room import *
import items
import quests
from scenerys import *
r1 = Room(1, "at the Construction Site", )

r2 = Room(2, "in a Grassy Field", 
firstenter = "You walk south towards where frank told you the wood planks would be." )

r3 = Room(3, "in the Deep woods", 
access = 0,
lockdesc = "You probably should listen to your boss and get those planks from the pile over there to the south.", 
lockreq = quests.firstquest, 
firstenter = "As you enter into the deep woods, you notice multiple workers who seem to have been knocked out.")

r4 = Room(4, "in the Grassy Outskirts", )
r5 = Room(5, "in the Grassy Outskirts" )
r6 = Room(6, "at Lily's house", )

#Room 1 (Construction Site Flour Mill)
#Room 2 (Grassy Field next to dirt road)
#Room 3 (Deep Woods)
