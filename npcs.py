from npc import *
import quests
from utils import *
from players import player


Frank1 = NPC("Frank", 
greeting = None,
examine = "He doesn't look like he's in a good mood. Probably best not to start a conversation with him.", 
dialogue = "Go on now! Go investigate that yelling! Someones gotta do it!", 
questunfinished = "You're not done yet. ",
quest1 = "You're still getting me those wood planks aren't you?",
quest2 = "Oh. I see you've got some with you. Thanks.",
questcompleted = ["Now that you've finally done something of value, maybe I can entrust you with a bigger task.",
"You know, I used to be just like you. Working just because I had to.",
"But once you get to be as experienced as me, you'll get to boss people around just like I do!", "@Frank pats your back and starts cackling.",
"Alright, next, I need you to -"]
)
worker1 = NPC("Stonemason", 
greeting = None,
examine = "This guy seems to be having a good time carving out a giant millstone from a rock.", 
dialogue = ["Hey there buddy.", "I saw you fall asleep over there an hour or two ago.", "I figured you needed your rest.", 
"Did you know that the flour mill we're building is actually called a grist mill?", 
"It seems the only way the it got funded was by telling people it was a flour mill.",
"They're essentially the same thing, but I guess flour mill was an easier sell to the public than grist mill was."])
Lily1 = NPC("Lily", 
greeting = None,
examine = "Lily turns away to avoid your awkward attempt to analyze her.", 
dialogue= ((f"Hey {player.name}!","Did you know you can examine anything just by thinking to yourself \"examine ____\"", "Try examining that boulder over there!", "But first you'll have to \"look around\" to see it!"))
)
worker2 = NPC("Angry worker", 
greeting = None,
examine = "An angry man who seems to be annoyed with life", 
dialogue = ("...",f"Are you {player.name}?", "...", "I've been waiting hours for you to show up.", "@The man turns around - ignoring your presence.")
)
Hubert1 = NPC("Hubert",
greeting = None,
examine = "He is definitely not from around here.", 
dialogue =("psssst", "pssssssssssssssst!!", "Hey! I'm Hubert!", 
"I travel the world to give advice to young'ns like you!", 
"Here's a tip!", "You can pick up any items you see around you if you say \"pick up ____\"",
"Hey, and since this is our first encounter, I'll give you a bonus tip! here you go:", 
"Make sure to listen closely to my tips closely! As it would be a real shame if I - ", 
"@A cloud of smoke appears in front of you, blocking your vision.", 
"@Once the cloud dissipates, it's clear to see, the man is gone."),
action="teleport"
)
worker3 = NPC("Unconcious worker",
examine = ("You lean in closer to take a look", "He seems to be alright, he's still breathing." ), 
greeting = None,
dialogue =("...")
)
worker4 = NPC("Entangled worker", 
examine = "He seems securely anchored into place by large plant roots.",
greeting = None,
dialogue = ["I've never seen sentient roots like these before!", 
"A monster went into the flour mill, he's the one who caused all this ruckus!",
"Go on, take my axe! I dropped it on the ground over there, go teach that monster a lesson!", 
"Don't forget to equip it while in battle!"])


Peggy = NPC("Peggy", 
examine = "A gentle woman who seems to be content life", 
dialogue = (f"You must be {player.name}!",)
)



Bill = NPC("Bill", 
examine = "You recognize Bill from ", 
dialogue = ("test",)
)


Hubert2 = NPC("Hubert",
greeting = None,
examine = "He is definitely not from around here.", 
dialogue =("psssst", "pssssssssssssssst!!", "Hey! I'm Huber -", 
f"Oh, - I remember you! You're {player.name}!",  
"Here's a tip!", 
"You can open your inventory simply by saying \"inventory\"!",
"Now you don't have to spend a turn in combat equipping a weapon, or putting on armor!",
"See you around!",
"@A cloud of smoke appears in front of you, blocking your vision.", 
"@Once the cloud dissipates, it's clear to see, the man is gone."),
action="teleport"
)

Hubert3 = NPC("Hubert",
greeting = None,
examine = "He is definitely not from around here.", 
dialogue =("psssst", "pssssssssssssssst!!", "Hey! I'm Hubert!", 
"I travel the world to give advice to young'ns like you!",
f"Oh - I remember you! You're {player.name}!",  
"Here's a tip!", "If you're feeling tired typing out \"explore\", instead, just type out the direction you wan't to go!",
"See you around!",
"@A cloud of smoke appears in front of you, blocking your vision.", 
"@Once the cloud dissipates, it's clear to see, the man is gone."),
action="teleport"
)



tempend = NPC("Jeff",
examine = ("This guy seems likeable!" ), 
greeting = None,
dialogue =(f"hi {player.name}! Unfortunately, this is pretty much the end of the game for right now.", 
"You're seeing some exclusive content here, as I only appear in early versions of this game :)", 
"You're free to explore the rest of the map! But its very likely nothing is up ahead.", 
"Thank you for playing!!!" )
)