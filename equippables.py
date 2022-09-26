from equippable import *

#Helmets
goblinMask = Armor("Goblin mask", "It's a crudely carved plank of wood. Seems to be rotting.", ArmorType.HELMET, 1 )
leatherHood = Armor("Leather hood", "", ArmorType.HELMET, 2)
gargMask = Armor("Garg's mask","Finders keepers!", ArmorType.HELMET, 5)
goldHelmet  = Armor("Ornamental gold helmet ", "", ArmorType.HELMET, 6)
ironHelmet = Armor("Construction helmet","You can tell it's been passed around from person to person. Seems like it could help keep your head safe.", ArmorType.HELMET, armorrating = 2)
testHelmet = Armor("Testhat","You can tell it's been passed around from person to person. Seems like it could help keep your head safe.", armortype = ArmorType.HELMET, armorrating = 2)
ironGreatHelm = Armor("Iron great helm", "Premium protection for a non-premium price.", ArmorType.HELMET, 11)
steelGreatHelm = Armor("Steel great helm", "Premium protection for a Premium Price.", ArmorType.HELMET, 14)
aduriteCrown = Armor("Adurite crown", "A band of pure adurite metal that wraps around the head. It seems to fit your head perfectly.", ArmorType.HELMET, 15)
#Body
cottonGarb = Armor("Cotton garb", "", ArmorType.BODY, 1)
leatherRobe = Armor("Leather robe", "", ArmorType.BODY, 3)
leatherPoncho = Armor("Leather poncho", "Some may mistake it for a cape. It's a poncho.", ArmorType.BODY, 6)
goldArmor = Armor("Gold plate armor", "", ArmorType.BODY, 10)    #tied with ironchainmail for armorvalue, make as a very rare
ironChainMail = Armor("Iron chain mail", "", ArmorType.BODY, 10)
ironArmor = Armor("Iron plate armor", "", ArmorType.BODY, 14)
steelArmor = Armor("Steel plate armor", "", ArmorType.BODY, 19)
aduriteArmor = Armor("Adurite plate armor", "Mythical armor that comes with mythical protection, all in stylish red.", ArmorType.BODY, 25)
#Boots
leathershoes = Armor("Leather shoes","A remarkably ordinary pair of shoes. You can see a hole starting to form at the toe.", ArmorType.BOOTS, 1)
leatherBoots = Armor("Leather boots","You check, and unfortunately, there is no steel toe.", ArmorType.BOOTS, 3)
steelToeBoots = Armor("Steel toe leather boots","You check, and unfortunately, is no steel toe. However, it IS a new pair of boots.", ArmorType.BOOTS, 4)
goldToeBoots = Armor("Gold toe leather boots","You check, and finally, you find some boots with some sort of metal toe.", ArmorType.BOOTS, 7)   #maybe give these to the player to inform them of the rarity of other gold items
dragonSkinBoots = Armor("Dragon-skin boots","Not made of any sort of metal. Doesn't mean you can't look metal wearing them.", ArmorType.BOOTS, 11)
aduriteBoots = Armor("Adurite boots","Boots made from the toughest material around.", ArmorType.BOOTS, 15)