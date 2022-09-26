import item

class Weapon(item.Item):
    """Weapon class inherits from item class, but adds attackbonus, speedbonus, and armorbonus."""
    
    def __init__ (self, name, examine, attackbonus, sellprice = None, tooltip = None, speedbonus = None, armorbonus = None):
        super().__init__(name,examine,sellprice,tooltip)
        self.attackbonus = attackbonus
        self.speedbonus = speedbonus
        self.armorbonus = armorbonus
        