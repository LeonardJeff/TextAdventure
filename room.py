from item import *
from npcs import *
from utils import *
from quest import *
import os

def changerooms(player, room1, room2):
	if room2.access == None:        
		player.location = room2		
	else: 
		if room2.lockreq.complete == 1:
			player.location = room2
			room2.lockreq.complete = 2
			pushtext(room2.firstenter)
			input
		elif room2.lockreq.complete == 2:
			player.location = room2
		else:
			player.location = room1
			pushtext(room2.lockdesc)

def talkto(player, npc):
	pushtext(npc.greeting, npc.name, speed = 0.04, cutscenemode = True)
	if len(npc.quests) == 0:
		for text in npc.dialogue:
					pushtext(text, npc.name)				
	else:		
		for quest in npc.quests:
			if quest in player.quests:
				pushtext(npc.quest1, npc.name)    #did you get me my x?
				if quest.item in player.inventory:
					for item in player.inventory:
						if item == quest.item:
							player.inventory.remove(quest.item)
							quest.progress += 1
							pushtext(npc.quest2, npc.name)										
					if quest.progress < quest.goalamount:
						pushtext(npc.quest2, npc.name)
						pushtext(npc.questunfinished + (questunf(quest), npc.name))					
					if quest.progress == quest.goalamount:
						quest.complete = 1
						pushtext(npc.questcompleted, npc.name)
						npc.quests.remove(quest)
						player.quests.remove(quest)
						pushtext("Quest Complete!", "Game")						
				else:
					pushtext(npc.questunfinished + (questunf(npc.quests[0])))
				
					
class Room:
	def __init__(self, roomid, desc, access = None, lockdesc = None, lockreq = None, firstenter = None, entered = None):
		self.roomid = roomid
		self.desc = desc
		self.neighbors = {"north":None,"east":None,"south":None,"west":None}
		self.npcs = []
		self.items = [] 
		self.scenerys = []
		self.access = access
		self.lockdesc = lockdesc
		self.lockreq = lockreq
		self.firstenter = firstenter
		self.entered = entered

	def setNeighbors(self, nroom=None, eroom=None, sroom=None, wroom=None):
		self.neighbors = {
			"north":nroom,
			"east":eroom,
			"south":sroom,
			"west":wroom
		}

	def getPrettyNeighbors(self):
		neighbors = []
		for direction in ["north", "east", "south", "west"]:
			room = self.neighbors.get(direction)
			if self.access == False:
				continue                        #continue ends current iteration and goes to next iteration
			if room is None:
				continue
			neighbors.append({"direction":direction,"room":room})
		return neighbors


	def __repr__(self) -> str:
		return f"#<room: id={self.roomid} action ={self.action}>"  
	
	def addnpc(self, npc):
		self.npcs.append(npc)
	
	def additem(self, *items):
		for item in items:
			self.items.append(item) 
	
	def addscenery(self, *scenerys):
		for scenery in scenerys:
			self.scenerys.append(scenery)

	
	def displayroom(self, player):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("HP: " + str(player.health) + "  Gold: " + str(player.gold))
		print("You are " + self.desc + " What would you like to do?" )
		print("Look around")
		
		if self.npcs:
			for npc in self.npcs:
				name = npc.name
				print("Talk to " + name.capitalize())
		for room in self.getPrettyNeighbors():
			print(f"Explore {room.get('direction')}")
		
		playerinput = getLowerInput()
		
		if playerinput.startswith("explore"):
			parts = playerinput.split(" ")
			if len(parts) != 2:
				pushtext("Invalid input, please retype your command")
				return
			else: 
				if self.getroomfordirection(parts[1]) == None:
					pushtext("Invalid input, please retype your command")
					return
			changerooms(player, self, self.getroomfordirection(parts[1]))		
		if playerinput.startswith("talk"): 
			parts = playerinput.split(" ")
			if len(parts) < 3:
				pushtext("Invalid input")				            
				return	
			
			inputname = "".join(parts[2:]).lower()
			comparename = compareblename(inputname)	
                                                                           
			for npc in self.npcs:
				if compareblename(npc.name) == comparename:                       
					talkto(player, npc) 
					return                      
				else:
					continue
					
			pushtext("It seems noone here goes by the name " + (inputname))     
		if playerinput.startswith("examine"):
			parts = playerinput.split(" ")			
			inputname = "".join(parts[1:]).lower()
			comparename = compareblename(inputname)																							
			
			for item in self.items:
				if compareblename(item.name).startswith(comparename):                       
					x = item.name
					thisitem = x.capitalize()
					pushtext("You examined the " + thisitem + ". " + item.examine)
					return
				else:
					continue                
			
			for npc in self.npcs:
				if compareblename(npc.name).startswith(comparename): 
					pushtext("You examine " + npc.name + ". ")
					for text in npc.examine:
						pushtext(text)					
					return       
				else:
					continue			
			
			for scenery in self.scenerys:
				if compareblename(scenery.name).startswith(comparename):                       
					x = scenery.name
					thisscenery = x.capitalize()
					pushtext("You examined the " + thisscenery + ".\n" + scenery.examine)
					return
				else:
					continue
		
			print("there is no " + inputname + ".")
			return	
		if playerinput.startswith("look"):
			counter = False
			pushtext("You take a look around the area", speed = 0.04, cutscenemode = True, cutscenemodeendspeed = 0.1) 
			pushtext("...", speed = 0.5, cutscenemode = True) 
			if self.items:
				counter = True
				pushtext("\nand you're able to see:", speed = 0.04, cutscenemode = True)
				for item in self.items:                
					pushtext("\n" + item.name.capitalize(), cutscenemode = True)
					time.sleep(0.3)
				input("\nPress enter to continue")
				return
			if self.scenerys:
				counter = True
				for item in self.scenerys:
					print(item.name.capitalize())
				input("Press enter to continue")                              
			if counter == False:
				pushtext("and find nothing...")
		if playerinput.startswith("pick"):
			parts = playerinput.split(" ")
			if len(parts) > 4:
				print("Invalid input (too many words)")              
				return
			if len(parts) < 3:
				print("Invalid input (too little words)")              
				return
			for item in self.items:
				if item.name.startswith(parts[2]):
					player.inventory.append(item)
					self.items.remove(item)
					pushtext("Picked up " + str(item))
					return
																			  
	def parse_examine(argument):
		switcher = {
			0:"item",
			1:"npc",
			2:"scenery"
		}
		return switcher.get(argument, 0)
				  
	def getroomfordirection(self, direction):
		return self.neighbors.get(direction)

	def opennewroom(self, room):
		room.access = 1
	def openroom(self, room):
		room.access = 2
	def closeroom(self, room):
		room.access = 0