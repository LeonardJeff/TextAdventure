import item

class Weapon(item.Item):
    
    def __init__ (self, name, examine, attackbonus, speedbonus = 0, armorbonus = 0, sellprice = None, tooltip = None,):
        super().__init__(self, name, examine, sellprice = None, tooltip = None)
        self.attackbonus = attackbonus
        self.speedbonus = speedbonus
        self.armorbonus = armorbonus
        self.sellprice = sellprice
        