from item import *

woodenplanks = Item(
"wooden planks", 
"Quest item. Multiple bundles of planks lay on top of each other, the planks aren’t particularly long. A label nailed to one side of each bundle reads “J.H. Lumber Yard”")

flowers = Item(
"Bundle of Flowers", 
"They seem to be haphazardly picked by hand. Even so, they're very colorful and would make for a nice bouquet.",
tooltip = "Dropped by Wandering Goblin",
consumable = True,                              #Yes you can eat the flowers hehe
healvalue = 2,
sellprice = 3,)

key1 = Item(
"shiny key", 
"A key to the gate by Lily's house. ")

mushroom = Item(
"mushroom", 
"Hopefully it's not poisonous...",
tooltip = "+5 Health",
consumable = True,
sellprice = 2,
healvalue = 5)

mushroom1 = Item(
"brownish mushroom", 
"Hopefully it's not poisonous...",
tooltip = "+3 Health",
consumable = True,
sellprice = 1,
healvalue = 3)

mushroom2 = Item(
"purplish mushroom", 
"Probably poisonous.",
consumable = True,
tooltip = "-2 Health",
healvalue = -2)

apple = Item(
"apple", 
"A fresh shiny red apple. Probably of the fuji variety.",
tooltip = "+5 Health",
consumable = True,
sellprice = 3,
healvalue = 5)

cucumber = Item(
"cucumber", 
"A waxy cucumber. It would probably be nice a salad.",
tooltip = "+3 Health",
consumable = True,
sellprice = 4,
healvalue = 3)

carrot = Item(
"carrot", 
"You should probably wash all the dirt off. Nahhhhhhh",
tooltip = "+5 Health",
consumable = True,
sellprice = 3,
healvalue = 5)

radish = Item(
"radish", 
"Apparently, these only take a few days to grow from seed.",
tooltip = "+3 Health",
consumable = True,
sellprice = 3,
healvalue = 3)

wildturnip = Item(
"wild turnip", 
"The non-wild variety is a staple of Galawynian cuisine.",
tooltip = "+5 Health",
consumable = True,
healvalue = 5,
sellprice = 2)

pillbug = Item(
name ="pillbug",
examine ="It seems to be happy with its home being in your pockets!",
sellprice = 13)

coyotebones = Item(
name ="coyote bones",
examine ="A pile of bones. Most notably, only the cool big ones.",
sellprice = 13)
