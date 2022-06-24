class Quest:
    def __init__(self, item, goalamount, name, hint, reward = None ):
        self.item = item
        self.goalamount = goalamount
        self.name = name
        self.hint = hint
        self.progress = 0
        self.complete = 0
        self.reward = reward
        
    
    
    def addquest(self, npc, player):
        npc.quests.append(self)
        player.quests.append(self)
    
    def __repr__(self):
        return f"#<quest: name {self.name} amount {self.goalamount} progress {self.progress} item {self.item} hint {self.hint}"
        
        