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

Frank2= NPC("Frank", 
greeting = None,
examine = "He seems a lot friendlier when he's not bossing you around.", 
dialogue = (f"...","Make sure to check up on my men at the infirmary when you get there.", 
"If they're not there when you get there, they probably got better and went home.", 
"No need to investigate it further.")
)

worker1 = NPC("Stonemason", 
greeting = None,
examine = "This guy seems to be having a good time carving out a giant millstone from a rock.", 
dialogue = ["Hey there buddy.", "I saw you fall asleep over there an hour or two ago.", "I figured you needed your rest.", 
"Did you know that the flour mill we're building is actually called a grist mill?", 
"It seems the only way the it got funded was by telling people it was a flour mill.",
"They're essentially the same thing, but I guess flour mill was an easier sell to the public than grist mill was."]
)

Lily1 = NPC("Lily", 
greeting = None,
examine = "Lily turns away to avoid your awkward attempt to analyze her.", 
dialogue= ((f"Hey {player.name}!","Did you know you can examine anything or anyone just by thinking to yourself \"examine ____\"", "Try examining that boulder over there!", "But first you'll have to \"look around\" to see it!"))
)

Lily2 = NPC("Lily", 
greeting = None,
examine = "Lily seems to have prepared for bed, sporting a nightgown and her hair in a bun.", 
dialogue= ((f"Hey {player.name}!",
"I'm actually headed to Galawyn tomorrow morning to sell some fresh vegetables, so maybe I'll meet you there!"))
)

worker2 = NPC("Angry worker", 
greeting = None,
examine = "An angry man who seems to be annoyed with life", 
dialogue = ("...",f"Are you {player.name}?", "...", "I've been waiting hours for you to show up.", "@The man turns around - ignoring your presence.")
)
Hubert1 = NPC("David",
greeting = None,
examine = "He is definitely not from around here.", 
dialogue =("psssst", "pssssssssssssssst!!", "Hey! I'm David!", 
"I travel the world to give advice to young'ns like you!", 
"Here's a tip!", "You can pick up any items you see around you if you say \"pick up ____\"",
"Hey, and since this is our first encounter, I'll give you a bonus tip! here you go:", 
"Make sure to listen closely to my tips closely! As it would be a real shame if I - ", 
"@A cloud of smoke appears in front of you, blocking your vision.", 
"@Once the cloud dissipates, it's clear to see, the man is gone."),
action="teleport"
)

worker3 = NPC("Unconscious worker",
examine = ("You lean in closer to take a look.", "He seems to be alright, he's still breathing." ), 
greeting = None,
dialogue =("...", "@The man doesn't look like he's intersted in talking right now.")
)

worker4 = NPC("Entangled worker", 
examine = "He seems securely anchored into place by large plant roots.",
greeting = None,
dialogue = ["I've never seen sentient roots like these before!", 
"A monster went into the flour mill, he's the one who caused all this ruckus!",
"Go on, take my axe! I dropped it on the ground over there, go teach that monster a lesson!", 
"Don't forget to equip it when the time comes!"])


Peggy = NPC("Peggy", 
greeting = None,
examine = "A gentle woman who seems to be content life", 
dialogue = (f"Good luck on your journey ahead {player.name}!", 
"Make sure to grab that key before you leave!")
)

Bill = NPC("Bill", 
examine = "You recognize Bill from ", 
dialogue = ("test",)
)

Hubert2 = NPC("David",
greeting = None,
examine = "He is definitely not from around here.", 
dialogue =("psssst", "pssssssssssssssst!!", "Hey! I'm Davi-", 
f"Oh, - I remember you! You're {player.name}!",  
"Here's a tip!", 
"You can open your inventory simply by saying \"inventory\"!",
"Now you don't have to spend a turn in combat equipping a weapon, or putting on armor!",
"Not that it would have made a difference in that fight between you and the forest spirit heh heh.",
"Anyway, see you around!",
"@A cloud of smoke appears in front of you, blocking your vision.", 
"@Once the cloud dissipates, it's clear to see, the man is gone."),
action="teleport"
)

Eve1 = NPC("Eve",
greeting = None,
examine = "She seems to be busy observing the flowers around the area.", 
dialogue =("Hi there, I'm Eve!", 
"I like to come over here to enjoy the nature around here every once in a while.",
 "...", 
 "Were you the one that just slayed that goblin?",
"You know, I saw that goblin from over here, it seemed to be interested in picking flowers, so I let it be.",
"I think you may have spooked him when you opened the gate, and thats why he attacked you.",
"Otherwise, I don't think it meant any harm...",
"Goblins don't run very fast, so you easily could have retreated and left it behind to think about its actions.",
"Not all goblins are nice... especially the ones that come out of the tree-line over there,",
"But maybe we should do all we can to be nice to eachother...",
"It was nice to meet you, but I think I'm going to head home now.",
"@Eve turns away from you and heads off.",
"@(Maybe if you had run from that goblin fight, events would have unfolded differently.)" 
),
action= "teleport"
)

Eve2 = NPC("Eve",
greeting = None,
examine = "She seems to be busy observing the flowers around the area.", 
dialogue =("Hi there, I'm Eve!", 
"I like to come over here to enjoy the nature around here every once in a while.",
"I saw how you ran from that goblin who attacked you.",
"I wish more people were like you.",
"I saw that goblin when I got here. It looked cute picking the flowers, so I let it be.",
"A lot of people get attacked and feel the need to retaliate. But I don't think that goblin knew any better.",
"Not all goblins are nice... especially the ones that come out of the tree-line over there.",
"Thank you for sparing that goblin. Maybe one day goblins and humans can pick flowers together."
),
)

wanderinggoblin = NPC("Wandering Goblin",
greeting = None,
examine = "The goblin seems to have calmed down from the fight between the two of you.", 
dialogue =("...",
"@The goblin grumbles something incoherant.",
"Sorry human...",
"You made me jump. I thought you were bad person.",
"Maybe not all people are scary-evil...",
"Me going home to bring flowers to friend Garg.",
"Bye bye human~",
"@The goblin sticks its flowers into it's tattered tunic and hobbles away."
),
action = "teleport"
)

Hubert3 = NPC("David",
greeting = None,
examine = "He is definitely not from around here.", 
dialogue =("psssst", "pssssssssssssssst!!", "Hey! I'm Davi-", 
"I travel the world to give advice to young'ns like you!",
f"Oh - I remember you! You're {player.name}!",  
"Here's a tip!", "If you're feeling tired typing out \"explore\", instead, just type out the direction you want to go!",
"See you around!",
"@A cloud of smoke appears in front of you, blocking your vision.", 
"@Once the cloud dissipates, it's clear to see, the man is gone."),
action="teleport"
)

Hunter = NPC("Coyote hunter", 
greeting = None,
examine = "He looks busy hunting coyotes. You should go talk to him.", 
dialogue = ["What do I plan to do with the coyote bones you ask?", "...", 
"I'm not really sure. You just really looked like you needed a quest."],
questunfinished = "I'll hand you this cool lookin key if you can get me some.",
quest1 = "Could you help me collect 3 coyote bones?",
quest2 = None,
questcompleted = ["Thank you much. As promised here is the key I promised.", 
"Heh, I don't really know what it goes to though."]
)

boy = NPC("Young lad",
greeting = None,
examine = "He doesn't look lost, but he doesn't seem like he's up to much.",
dialogue = ["Hi!", "My dad brought me here to help him hunt some coyotes, but I decided to look around to see what cool stuff I could find.",
"I haven't really found anything cool though. My dad won't let me go too far, he says its dangerous to be by yourself over here.",
"He won't stop talking about how death is permanent and how I should be careful if anything tries to attack me.",
"Pretty dark stuff, but apparently Galawyn plains is where a lot adventurer's journeys come to an end.",
"Good thing I brought plenty of food to keep me in good health!"])

tempend = NPC("Jeff",
examine = ("This guy seems " ), 
greeting = None,
dialogue =(f"Hi {player.name}! Unfortunately, this is pretty much the end of the game for right now.", 
"Ahead are the gates to Galawyn, maybe one day you'll be able to go in! But for now it's locked in this game demo.", 
"I've left some goodies on the ground for you to mess around with!",
"Thank you so much for playing!!!", "No really", "Thank you :)")
)

#f"hi {player.name}! Unfortunately, this is pretty much the end of the game for right now.",        Old dialogue for tempend
#"You're seeing some exclusive content here, as I only appear in early versions of this game :)", 
#"You're free to explore the rest of the map! But its very likely nothing is up ahead.", 
#"Thank you for playing!!!"