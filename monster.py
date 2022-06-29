class Monster:
    def __init__(self, name, examine, dialogue=[], inventory=None, attack=1, health=5 ):

        if inventory is None:
            inventory = []
        self.inventory = inventory       
        
        self.name = name
        self.examine = examine
        self.dialogue = dialogue
        self.attack = attack
        self.health = health