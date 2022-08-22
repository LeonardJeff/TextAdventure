import player
import combat
import monsters
import rooms

p = player.Player(rooms.r1, name = "jeff")
c= combat.Combat(p, monsters.firstgoblin)
c.startcombat()