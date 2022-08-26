import player
import combat
import monsters
import rooms
from items import apple, mushroom, key1,wildturnip

p = player.Player(rooms.r1, name = "jeff")
p.inventory.extend([mushroom,key1,apple,wildturnip])
c= combat.Combat(p, monsters.forestdemon)
c.startcombat()