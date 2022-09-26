import item
from enum import Enum

class ArmorType(Enum):
    HELMET = 1
    BODY = 2
    BOOTS = 3
    RING = 4

class Armor(item.Item):
    
    def __init__ (self, name, examine, armortype, armorrating, sellprice = None, tooltip = None):
        super().__init__(name, examine, sellprice, tooltip) #I think this stops me from having to do name = name, examine = examine, etc.
        self.armortype = armortype
        self.armorrating = armorrating
