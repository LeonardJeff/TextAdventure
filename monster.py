class Monster:
    def __init__(self, name, examine, dialogue=[], drops=None, attack=1, health=5, speed = 1 ):

        if drops is None:
            drops = []
        self.drops = drops       
        
        self.name = name
        self.examine = examine
        self.dialogue = dialogue
        self.attack = attack
        self.health = health
        self.speed = speed