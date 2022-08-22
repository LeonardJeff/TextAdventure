from item import *

woodenplanks = Item(
"wooden planks", 
"Quest item. Multiple bundles of planks lay on top of each other, the planks aren’t particularly long. Clearly designed to be handled one bundle at a time. A label nailed to one side of each bundle reads “J.H. Lumber Yard”")

key1 = Item(
"shiny key", 
"You ")

mushroom = Item(
"mushroom", 
"Hopefully it's not poisonous...",
tooltip = "+5 Health",
consumable = True,
sellprice = 2)

mushroom1 = Item(
"brownish mushroom", 
"Hopefully it's not poisonous...",
tooltip = "+3 Health",
consumable = True,
sellprice = 1)

mushroom2 = Item(
"purplish mushroom", 
"Probably poisonous.",
consumable = True,
tooltip = "-2 Health")

apple = Item(
"apple", 
"A fresh shiny red apple. Probably of the fuji variety.",
tooltip = "+5 Health",
consumable = True,
sellprice = 3,
healvalue = 5)

wildturnip = Item(
"wild turnip", 
"The none-wild variety is a staple of Galawynian cuisine.",
tooltip = "+5 Health",
consumable = True,
sellprice = 5)