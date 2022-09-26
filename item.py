class Item:
    def __init__(self, name, examine, sellprice = None, tooltip = None, consumable = False, healvalue = None):
        
        self.name = name 
        self.examine = examine
        self.sellprice = sellprice
        self.consumable = consumable
        self.healvalue = healvalue
        self.tooltip = tooltip

    def __repr__(self):
        return f"{self.name}"
    
    def consume(self,subject):
        if self.healvalue:
            subject.health = subject.health + self.healvalue
            if subject.health > subject.maxhealth:
                subject.health = subject.maxhealth
            subject.inventory.remove(self)
        else:
            pass
