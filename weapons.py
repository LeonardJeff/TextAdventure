from weapon import Weapon
from weapons import *

#Sword
axe = Weapon(
name ="axe", 
examine="A used and slightly weathered axe. Its not yours but now would probably be a good time to pick it up.",
attackbonus= 2,
speedbonus= 0,
tooltip = "+2 Attack"
)

rustywoodenstick = Weapon(
name ="broken rusty wooden staff", 
examine="How does it even rust?",
attackbonus = 1,
speedbonus = 0,
armorbonus = 0,
tooltip = ["+1 Attack", "+1 Swag"])

rustySword = Weapon(
name ="rusty sword", 
examine="A used and very weathered sword.",
attackbonus= 3,
speedbonus= 0,
tooltip = "+3 Attack")

ironSword = Weapon(
name ="iron sword", 
examine="A basic iron sword, simple and reliable.",
attackbonus = 5,
speedbonus = 0,
armorbonus = 1,
tooltip = ["+5 Attack", "+1 Armor"],
sellprice = 5)

steelSword = Weapon(
name ="steel sword", 
examine="A well crafted steel sword. -\"Proudly made in Galawyn\"",
attackbonus = 8,
speedbonus = 0,
armorbonus = 2,
tooltip = ["+8 Attack", "+2 Armor"],
sellprice = 10)

characterCutlass = Weapon(
name ="character cutlass",        #mini-boss character's sword
examine="Finders keepers!",
attackbonus = 15,
speedbonus = 0,
armorbonus = 0,
tooltip = ["+15 Attack"],
sellprice = 20)

characterRapier = Weapon(
name ="character rapier",        #important character's sword
examine="Your sword swings feel quick and nimble with PLACEHOLDER's rapier. She'll probably want this back.",
attackbonus = 16,
speedbonus = 3,
armorbonus = 0,
tooltip = ["+16 Attack", "+3 Speed"])

characterSword = Weapon(
name ="character sword",        #important character's sword
examine="",
attackbonus = 20,
speedbonus = 3,
armorbonus = 3,
tooltip = ["+20 Attack","+3 Speed","+3 Armor"])

aduriteGreatSword = Weapon(
name ="adurite greatsword", 
examine="A mighty greatsword containing raw earth energy. It's warm to the touch.",
attackbonus= 25,
speedbonus= 5,
tooltip = ["+25 Attack", "+5 Speed"])
