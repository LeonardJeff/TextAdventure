def getDirectionName(directionletter):
    if directionletter == "n":
        return "north"
    if directionletter == "e":
        return "east"
    if directionletter == "s":
        return "south"
    if directionletter == "w":
        return "west"


class Room:
    def __init__(self, roomid, desc):
        self.roomid = roomid
        self.desc = desc
        self.neighbors = {"n":None,"e":None,"s":None,"w":None}
        self.npc = []
        self.items = []      

    def setNeighbors(self, nroom=None, eroom=None, sroom=None, wroom=None):
        self.neighbors = {
            "n":nroom,
            "e":eroom,
            "s":sroom,
            "w":wroom
        }

    def getPrettyNeighbors(self):
        toreturn = []
        for direction in ["n", "e", "s", "w"]:
            room = self.neighbors.get(direction)
            if room is None:
                continue
            toreturn.append({"direction":getDirectionName(direction),"room":room})
        return toreturn


    def __repr__(self) -> str:
        return f"#<room: id={self.roomid} action ={self.action}>"
    
    def addnpc(self, npc):
        self.npc.append(npc)
    
    def additem(self, *items):
        for item in items:
            self.items.append(item)
    
    def displayroom(self):
        print("You are in " + self.desc + " What would you like to do?" )
        print("Look for items (items)")
        if self.npc:
            for npc in self.npc:
                print(f"Talk to {npc.name}")
        for room in self.getPrettyNeighbors():
             print(f"Explore {room.get('direction')}")
        