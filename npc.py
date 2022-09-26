class NPC:
    def __init__(self, name, examine, dialogue=[], greeting="greetings, i am error", inventory=None, questcompleted =None, questunfinished=None, quest1=None, quest2=None, action = None):

        if inventory == None:
            inventory = []
        self.inventory = inventory       
        self.greeting = greeting
        self.name = name
        self.examine = examine
        self.quests = []
        self.questcompleted = questcompleted
        self.questunfinished = questunfinished
        self.quest1 = quest1
        self.quest2 = quest2
        self.dialogue = dialogue
        self.action = action

    
