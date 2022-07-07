class Item:
    def __init__(self, name, examine, sellprice = None,tooltip = None):
        
        if tooltip == None:
            tooltip = []
        self.name = name 
        self.examine = examine
        self.sellprice = sellprice
        

    def __repr__(self):
        return f"{self.name}"