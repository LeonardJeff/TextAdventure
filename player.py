from utils import *
class Player:
    def __init__(self, startingroom = None, name = "error4"):

        self.inventory = []
        self.health = 100
        self.location = startingroom
        self.gold = 3
        self.quests = []
        self.name = name

    def setname(self, text):
        self.name = text      