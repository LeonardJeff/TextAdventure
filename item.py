class Item:
    def __init__(self, name, examine):

        self.name = name 
        self.examine = examine      

    def __repr__(self):
        return f"{self.name}"