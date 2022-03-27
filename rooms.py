from room import Room
from npcs import *
from items import *
r1 = Room(1, "A Construction Site")
r2 = Room(2, "Grassy Field")
r3 = Room(3, "Deep woods")
r4 = Room(4, "Grassy Outskirts")

r1.setNeighbors(nroom=r3, sroom=r2) #north room needs to be blocked off at first
r2.setNeighbors(nroom=r1)
r3.setNeighbors(sroom=r1)
r4.setNeighbors(sroom=r2)   #unfinished

r1.addnpc(Frank)
r1.additem(woodenplank, woodenplank)