class Scenery:
    def __init__(self, name, examine, container = None):

        self.name = name 
        self.examine = examine  
        self.container = container    

    def __repr__(self):
        return f"#<item:name= {self.name}>"