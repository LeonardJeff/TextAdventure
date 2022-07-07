import item
from enum import Enum

class ArmorType(Enum):
    HELMET = 1
    BODY = 2
    BOOTS = 3
    RING = 4

class Armor(item.Item):
    
    def __init__ (self, name, examine, armortype, armorrating, tooltip=None):
        super().__init__(self, name, examine)
        self.armortype = armortype
        self.armorrating = armorrating
        self.tooltip = tooltip