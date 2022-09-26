class Scenery:
    def __init__(self, name, examine, inspecttext = [], inspected = False, 
    container = None, enemyspawn = None, visible = False, itemtext = None):

        self.name = name                #scenery object name
        self.examine = examine          #scenery object examine text
        self.inspecttext = inspecttext  #text to be displayed when player inspects object
        self.inspected = inspected      #tells if a player has inspected the scenery object
        self.enemyspawn = enemyspawn    #determines if this scenery spawns enemies
        self.visible = visible          #determines if scenery is hidden from player action menu
        
        self.itemtext = itemtext        #text for if the scenery has an item in it.
        self.container = container      #what may be inside the scenery object
    def __repr__(self):
        return f"#<item:name= {self.name}>"


        #if scenery has object, display itemtext            #ended off here
        #if scenery has no object, display inspecttext