import item
import npcs
from utils import *
import os
import combat

def changerooms(player, room1, room2):
	if room2.access == True:        
		player.location = room2
		if room2.entered == False:
			os.system('cls' if os.name == 'nt' else 'clear')
			pushtext(room2.firstenter, speed = 0.03)
			room2.entered = True
		return
	else: 
		if room2.itemlockreq:			#if room has an item requirment to access
			if room2.itemlockreq in player.inventory:	#if player has room item lock req in their inventory
				os.system('cls' if os.name == 'nt' else 'clear')
				room2.access = True
				player.inventory.remove(room2.itemlockreq)
				player.location = room2
				pushtext(room2.firstenter, speed = 0.03)
				room2.entered = True
				return
			else:
				pushtext(room2.lockdesc)
				return

		if room2.lockreq.complete == 1:	#if room2's quest requirement's complete varible == 1
			player.location = room2
			room2.entered = True
			room2.access = True
			os.system('cls' if os.name == 'nt' else 'clear')
			pushtext(room2.firstenter, speed = 0.03)
			return
	player.location = room1
	pushtext(room2.lockdesc)

def talkto(player, npc):
	pushtext(npc.greeting, npc.name, speed = 0.04,)
	if len(npc.quests) == 0:
		pushtext(npc.dialogue, npc.name, 0.03)
		return							
							#this system of handling quests is terrible, and I plan to essentially rewrite all of this.
	for quest in npc.quests:					#this code block removes items one by one if it's a quest item in your inventory
		if quest in player.quests:
			pushtext(npc.quest1, npc.name, 0.03)
			
			if quest.item in player.inventory:	#if player has quest item, display quest2 dialogue
				pushtext(npc.quest2, npc.name, 0.03)
				invcopy = player.inventory.copy()		#make a copy of the list for iterative purposes
				for item in invcopy:			
					if quest.progress == quest.goalamount: #if questprogress is met, break loop of giving over items
						break 
					if item == quest.item:
						player.inventory.remove(quest.item)		#if item is a quest item, remove it from original list, progress++
						quest.progress += 1																			

		if quest.progress < quest.goalamount:		#if quest is not finished after talking
			pushtext(npc.questunfinished, npc.name, 0.03 )
			pushtext((questunf(npc.quests[0])), npc.name, 0.03)				
		
		if quest.progress >= quest.goalamount:
			quest.complete = True
			pushtext(f"You've completed the \'{quest.name}\' quest!", "Game")	
			pushtext(npc.questcompleted, npc.name, 0.03)
			npc.quests.remove(quest)
			player.quests.remove(quest)					
				

				
					
class Room:
	def __init__(self, roomid, desc, access = True, lockdesc = None, lockreq = None, itemlockreq = None, firstenter = None, entered = False):
		self.roomid = roomid			#integer corresponding to room number
		self.desc = desc				#"in the, at the, at a, _____" to let player know what room the just entered.
		self.neighbors = {"north":None,"east":None,"south":None,"west":None}	#what rooms border this room
		self.npcs = []					#list of npcs in the room
		self.items = [] 				#list of items laying on the ground in the room
		self.scenerys = []				#list scenery objects in a room
		self.access = access			#determines whether the player can enter the room or not.
		self.lockdesc = lockdesc		#what to tell player if the room is locked.
		self.lockreq = lockreq			#lock requirement, takes in quest.
		self.itemlockreq = itemlockreq 	#lock requirement, takes in an item.		
		self.firstenter = firstenter	#first enter text
		self.entered = entered			#tells if the room has been entered yet.

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
	
	def addnpc(self, npc):		#add an NPC to a room
		self.npcs.append(npc)
	
	def removenpc(self, npc):	#remove an NPC to a room
		self.npcs.remove(npc)
	
	def additem(self, *items):	#add item(s) to a room
		for item in items:
			self.items.append(item) 
	
	def addscenery(self, *scenerys):	#add scenery(s) to the room
		for scenery in scenerys:
			self.scenerys.append(scenery)

	
	def displayroom(self, player):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("HP: " + str(player.health) + "  Gold: " + str(player.gold))
		print("You are " + self.desc + " What would you like to do?" )
		print("--------------------------------------------------------")
		print("Look around")
		
		for room in self.getPrettyNeighbors():
			print(f"Explore {room.get('direction')}")
		print()	
		if self.npcs:
			for npc in self.npcs:
				name = npc.name
				print("Talk to " + name.capitalize())
		
		for scenery in self.scenerys:
			if scenery.visible == True:
				print("Search " + scenery.name)
		
		
		
		playerinput = getLowerInput()
		if playerinput == "":
			return
			
		if playerinput == "north" or playerinput == "east" or playerinput == "south" or playerinput == "west":
			if self.getroomfordirection(playerinput) == None:
					pushtext(f"The path {playerinput} leads you nowhere. You decide to head back.", speed = 0.03)
					return
			changerooms(player, self, self.getroomfordirection(playerinput))

		
		if playerinput.startswith("explore"):
			parts = playerinput.split(" ")		#split playinput and use second word as input to direction change
			if len(parts) != 2:
				pushtext("Invalid input, please retype your action")
				return
			else: 
				if self.getroomfordirection(parts[1]) == None:
					pushtext(f"The path {parts[1]} leads you nowhere. You decide to head back.", speed = 0.03)
					return
			changerooms(player, self, self.getroomfordirection(parts[1]))		
		
		if playerinput.startswith("inventory"): 
			player.openinv(overworld = True)
			
			return
		if playerinput.startswith("talk"): 
			parts = playerinput.split(" ")
			if len(parts) < 3:
				pushtext("Invalid input, please retype your action")				            
				return	
			
			inputname = "".join(parts[2:]).lower()
			comparename = compareblename(inputname)	
                                                                           
			for npc in self.npcs:
				if compareblename(npc.name) == comparename:                       
					talkto(player, npc)
					if npc.action == "teleport":
						self.removenpc(npc) 
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
					thisitem = item.name.capitalize()
					pushtext("You examined the " + thisitem + ".")
					pushtext(item.examine)
					return
				else:
					continue                
			
			for npc in self.npcs:
				if compareblename(npc.name).startswith(comparename): 
					pushtext("You examine " + npc.name + ". ")
					pushtext(npc.examine)					
					return       
				else:
					continue			
			
			for scenery in self.scenerys:
				if compareblename(scenery.name).startswith(comparename):                       
					thisscenery = scenery.name.capitalize()
					pushtext("You examined the " + thisscenery + ".")
					pushtext(scenery.examine)
					return
				else:
					continue
		
			pushtext(f"invalid command:\"{inputname}\". please retype your action")
			return	
		
		if playerinput.startswith("search"): 
			parts = playerinput.split(" ")
			if len(parts) < 2:
				pushtext("Invalid input, please retype your action")
				return
			for scenery in self.scenerys:
				if parts[1] in compareblename(scenery.name):
					pushtext(f"You search the {scenery.name}.")					
					if scenery.container != None:			#if scenery.container contains an item
						pushtext(scenery.itemtext)	
						player.inventory.append(scenery.container)
						pushtext("Picked up " + str(scenery.container))
						scenery.container = None			#empty the scenery container
					else:	
						pushtext(scenery.inspecttext)	#if there is no item, display default search text	
					if scenery.enemyspawn:					#if scenery has an enemy spawner, initiate combat
						enemyinstance = scenery.enemyspawn()
						sceneryCombat = combat.Combat(player, enemyinstance)
						sceneryCombat.startcombat()
					scenery.inspected = True				#unused atm
					return
			else:
				pushtext(f"It seems that can't be searched.")
			return
		
		if playerinput.startswith("look"):
			counter = False
			pushtext("You take a look around the area", speed = 0.04, cutscenemode = True) 
			pushtext("...", speed = 0.3, cutscenemode = True) 
			if self.items or self.scenerys:	#if either items or scenerys exist in self
				counter = True
				pushtext("\nand you're able to see:", speed = 0.04, cutscenemode = True)
				for item in self.items:                
					pushtext("\n" + item.name.capitalize(), cutscenemode = True)
					time.sleep(0.3)				
				for scenery in self.scenerys:
					pushtext("\n" + scenery.name.capitalize(), cutscenemode = True)
					scenery.visible = True
					time.sleep(0.3)	  
			if counter == False:		#if there are no items in self
				pushtext("\nand find nothing...")
			pushtext("\nPress enter to continue")

		if playerinput.startswith("pick"):
			parts = playerinput.split(" ")
                                                                           
			if len(parts) > 4:
				print("Invalid input (too many words)")              
				return
			if len(parts) < 3:
				print("Invalid input (too little words)")              
				return
			for item in self.items:
				if compareblename(item.name).startswith(parts[2]):
					player.inventory.append(item)
					self.items.remove(item)
					pushtext("Picked up " + str(item))
					return
			pushtext(f"Can't pick up {parts[2:]}")
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