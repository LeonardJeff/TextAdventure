class NPC:
    def __init__(self, name, dialogue, inventory=None):

        if inventory is None:
            inventory = []
        self.inventory = inventory       
        self.dialogue = dialogue
        self.name = name