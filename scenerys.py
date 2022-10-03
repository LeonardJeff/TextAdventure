from scenery import *
from monsters import getcoyote, getgoblin, getdemon
import items
import equippables
import weapons
dirtroad = Scenery("dirt road", 
"As you get closer, you begin to realize, it is definitely a dirt road.")

tree1 = Scenery("tree", 
"A tree :)")

firstrock = Scenery("Boulder", 
examine = "A very unassuming large boulder. Probably has been there for millennia", 
inspecttext= "You fail to find anything remotely noteworthy about the large boulder.",
itemtext= ["At the base of the boulder you find a cute little bug!", 
"Upon closer inspection, it looks like a pillbug!", 
"You pick up the bug and safely stash it away into you pockets."],
container = items.pillbug)

carrotcroprow = Scenery("Carrot Crop Row", 
examine = "A row of carrot crops. Maybe nobody would notice if you took one...", 
inspecttext= "You should probably leave the rest for whoever planted these...",
itemtext= ["You look around to make sure noone is looking -", 
"You kneel down and tightly grab the base of the carrot plant and pull -", 
"After a little bit of tugging, you successfully unearth a large orange carrot."],
container = items.carrot)

cucumbercroprow = Scenery("Cucumber Crop Row", 
examine = "A row of multiple cucumber plants neatly wrapped around trellises. Maybe nobody would notice if you took one...", 
inspecttext= "You should probably leave the rest of the cucumbers for whoever planted them...",
itemtext= ["You look around to make sure noone is looking -", 
"You kneel down towards the bottom of one of the trellises, where hopefully nobody will notice if you snag a cucumber.", 
"You scan the bottom of the vine for a ripe cucumber."],
container = items.cucumber)

radishcroprow = Scenery("Radish Crop Row", 
examine = "A crop row covered in green from the many radishs that are planted here. Maybe nobody would notice if you took one...", 
inspecttext= "You should probably leave the rest of the radishs for whoever planted them...",
itemtext= ["You look around to make sure noone is looking -", 
"You kneel down and tug lightly at a radish plant.", 
],
container = items.radish)

flourmill = Scenery("Flour Mill",
"An unfinished construction project. Probably would be further along in its construction if you hadn't been sleeping on the job.",
["You approach the flour mill. You can hear a creature growling inside.", 
"You carefully begin to approach the front doorway.", 
"!!!",
"A towering creature breaks through the front of the stone building!",
"You hear someone yelling from behind - ",
"???: Wait!!!",
"The demonic looking creature steps towards you -"], 
enemyspawn= getdemon())

skidmarks = Scenery("Skid marks", 
examine = "Roughly you sized, they lead directly into a bunch of knocked-over cattails leading into the lake.", 
inspecttext= "Nothing interesting happens.", visible = True, inspected = True)

tempestlake = Scenery("Lake",
examine= "An ecologically bustling lake, its amazing that you're generally unscathed from your journey into the lake.",
inspecttext= ["You can see a beaver soaking up the sun while he floats across the water on his back.", "Nice."],
itemtext= ["It's probably best if you stay out of the lake.",
"But, from a distance, you can see birds soaring, fish flopping,", "And what's this?", 
"You move closer to find a stubby sword stuck in the muddy dirt."],
container= weapons.rustySword,
visible = True
)

bearcrow = Scenery("Bearcrow", 
examine = "Shouldn't it be called a scarebear?",
inspecttext = ["You approach the rotund figure hung up by a tree branch thats been stuck vertically into the ground.",
"Upon closer inspection, you can tell it is indeed bear shaped, but not really.", 
"Its burlap torso has many large holes in it, with decaying straw poking out."],
visible = True
)

farmersalmanac = Scenery("Farmers' Almanac",
examine = "You can see a thin film of dust covering the open pages of the book.",
inspecttext = ["The book must be years old - it looks like it is a few page turns away from degrading to dust.", 
"The book has been left open to the \"Garden Pest Management\" section.", 
"You skim a few lines of text until you come across something familiar:",
"\nBearcrows: You may be familiar with scarecrows to keep away the birds, but how is one to keep away the pesky goblins?\nNo matter how many of them you exterminate, these pests will always keep coming back. If you're growing cabbage this season, a bearcrow is a must. \nWe all know goblins have a natural affinity to cabbage, but did you know goblins will run at the sight of a bear? \nIt's unfortunate that bears aren't native to the lands around Galawyn, but that may change in upcoming seasons as bears have been slowly finding their way west of Acra Forest.",
"On the next page is a crudely drawn image of a bear."],
)

gate1 = Scenery("Iron Gate",
examine = "The gate to the north looks secure. Definitely no way of getting through without a key.",
inspecttext = ["You approach the gate to the north.", "It seems securely shut by a lock on the front."],
visible = True
)

gate2 = Scenery("Iron Gate",            #unused right now
examine = "The gate to the north looks secure. Definitely no way of getting through without a key.",
inspecttext = ["You approach the gate to the north.", "It seems securely shut by a lock on the front."],
visible = True
)

flourmill = Scenery("Flour Mill",
"An unfinished construction project. Probably would be further along in its construction if you hadn't been sleeping on the job.",
inspecttext = ["You approach the flour mill. You can hear a creature growling inside.", 
"You carefully begin to approach the front doorway.", 
"!!!",
"The towering creature breaks through the front of the stone building!",
"You hear someone yelling from behind - ",
"???: Wait!!!",
"The demonic looking creature steps towards you -"], 
enemyspawn= getdemon)

foresttreeline = Scenery("Forest outcrop",
examine = "It gets dark quickly, there might be some danger if you search around here...",
inspecttext = ["You approach the forest outcrop. You can hear a creature growling at the treeline ahead...",
"!!!"], 
enemyspawn= getgoblin)

animalden = Scenery("Animal Den",
examine = "It might be dangerous to search in an animals den...",
inspecttext = ["You approach the anial den. You can hear a creature growling from inside...",
"!!!"], 
enemyspawn= getcoyote)