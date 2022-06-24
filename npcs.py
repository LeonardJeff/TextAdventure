from npc import *
from quests import *
from utils import *
from players import player


Frank1 = NPC("Frank", 
greeting = None,
examine = "Lily's Father. Doesn't look like he's in a good mood. Probably best not to start a conversation with him.", 
dialogue = ("I haven't got all day. Go south towards the dirt road and grab me those planks.", "test"), 
questunfinished = "You're not done yet. ",
quest1 = "You're still getting me those wood planks aren't you?",
quest2 = "Oh. I see you've got some with you. Thanks.",
questcompleted = "Now go get me that last wooden plank i asked f-"
)

Lily1 = NPC("Lily", 
greeting = f"Hey {player.name}!",
examine = "Lily turns away to avoid your awkward attempt to analyze her.", 
dialogue= (("Did you know you can examine anything just by thinking to yourself \"examine ____\"", "Try it on that rock over there!"))
)

Peggy = NPC("Peggy", 
examine = "A gentle woman who seems to be content life", 
dialogue = ("test",)
)

Henry = NPC("Henry", 
examine = "An angry man who seems to be annoyed with life", 
dialogue = ("test",)
)

Bill = NPC("Bill", 
examine = "You recognize Bill from ", 
dialogue = ("test",)
)

Hubert1 = NPC("Hubert",
examine = "He is definitely not from around here.", 
dialogue =("psssst", "pssssssssssssssst!!", "Hey! I'm Hubert," )
)

Man1 = NPC("Unconcious Man",
examine = ("You lean in closer to take a look", "He seems to be alright, he's still breathing." ), 
dialogue =("..." )
)