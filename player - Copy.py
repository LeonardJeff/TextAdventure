
class Player:
    def __init__(self, startingroom = None, name = "errorname"):

        self.inventory = []
        self.location = startingroom
        self.gold = 3
        self.quests = []
        self.name = name
        self.level = 1
        self.experience = 0
        self.magiclevel = 1
        self.health = 10 #player health will range from 10-99
        self.maxhealth = 10     
        self.attack = 3 #player attack will range from 1-20
        self.magiclevel = 1 #player magiclevel will range 1-99
        self.speed = 3  #player speed will range from 3-20

        #for equip
        self.headslot = None
        self.bodyslot = None
        self.bootslot = None
        self.ringslot = None
        self.weapon   = None
    
    def equip(self, characteritem):
        if isinstance(characteritem, Item):
            if type(characteritem) == Weapon:           #if weapon
                if self.weapon != None:
                    self.inventory.append(self.weapon)
                self.weapon = characteritem
                self.inventory.remove(characteritem)
            
            if type(characteritem) == ArmorType.HELMET: #if helmet
                if self.headslot != None:
                    self.inventory.append(self.headslot)
                self.headslot = characteritem
                self.inventory.remove(characteritem)
            
            if type(characteritem) == ArmorType.BODY:   #if body armor
                if self.bodyslot != None:
                    self.inventory.append(self.bodyslot)
                self.bodyslot = characteritem
                self.inventory.remove(characteritem)

            if type(characteritem) == ArmorType.BOOTS:  #if boots
                if self.bootslot != None:
                    self.inventory.append(self.bootslot)
                self.bootslot = characteritem
                self.inventory.remove(characteritem)

            if type(characteritem) == ArmorType.RING:   #if ring
                if self.ringslot != None:
                    self.inventory.append(self.ringslot)
                self.ringslot = characteritem
                self.inventory.remove(characteritem)
            
            pushtext(f"Equipped {str(characteritem)}.")
    
    ###def unequip(self, enum):
    #    if isinstance(enum, Weapon):
    #        if type(enum) == Weapon:
    #            self.inventory.append(self.weapon)
    #            self.weapon = None
    #        if enum == ArmorType.HELMET:
    #            self.inventory.append(self.headslot)
    #            self.headslot = None
    #        if enum == ArmorType.BODY:
    #            self.inventory.append(self.bodyslot)
    #            self.bodyslot = None
    #        if enum == ArmorType.BOOTS:
    #            self.inventory.append(self.bootslot)
    #            self.bootslot = None
    #        if enum == ArmorType.RING:
    #            self.inventory.append(self.ringslot)
    #            self.ringslot = None
        
    def getArmorRating(self):
        total = 0
        if self.headslot:
            total += self.headslot.armor
        if self.bodyslot:
            total += self.bodyslot.armor
        if self.bootslot:
            total += self.bootslot.armor
        if self.ringslot:
            total += self.ringslot.armor
        if self.weapon:
            total += self.weapon.armorbonus
        return total

    def openinv(self, overworld = False):
        while playerselect == None:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(">-----------------------------------------------------------<")
            print(f"{self.name} - {self.health}/{self.maxhealth} HP - {self.gold} Gold")
            print(f"Weapon - {self.weapon}")
            print(f"Head - {self.headslot}")
            print(f"Ring - {self.ringslot}")
            print(f"Body - {self.bodyslot}")
            print(f"Boots - {self.bootslot}")
            print(">-----------------------------------------------------------<")
            if overworld == True:
                print("[1]items [2]weapons [3]armor [a]View all items [4]exit ")                
            if overworld == False:           
                print("[1]items [2]weapons [3]armor [4]exit")
            playerselect = input()
            templist = []
                
                        

                        #If I had time, I would rewrite this entire match case, this whole thing is incredibly rough

            
            match playerselect:    
                case "1":
                    for items in self.inventory:
                        if items.consumable == True:
                            templist.append(items)
                    if len(templist) == 0:
                        pushtext("You have no items in your bag")
                    if len(templist) > 8:
                        sublists = [templist[x:x+8] for x in range(0, len(templist), 8)] #every 8 items
                        
                        for i in sublists:                           #iterate over pages of item lists one at a time
                            page = list(enumerate(i[:],1))       #make a list, of enumerated items, now tuples.                     
                            
                            for item in page:                       #for each tuple in templist
                                print(f"[{str(item[0])}] {str(item[1])}")
                            
                            if len(page) >= 8:              #if length of current page >=8 entries, give a "next page" option
                                print("[0] Next Page -->")

                            playerinput = input()                        
                            if playerinput == "":
                                break
                            if playerinput == "0":  
                                continue                    #display next page of items

                            for item in page:               #iterate over templist tuples, if item[x] matches input, consume()
                                if playerinput == str(item[0]):
                                    item[1].consume(self)
                                    return "item", (item[1].name)
     
                    else:                                   #if the player doesn't have more than 9 consumable items
                        page = list(enumerate(templist[:],1))
                        for item in page:
                            print(f"[{str(item[0])}] {str(item[1])}")   #print every available consumable item
                        playerinput = input()    
                        
                        for item in page:          #if player input matches an item position, use that item.
                            if playerinput == str(item[0]):
                                item[1].consume(self)
                                return "item", (item[1].name)
                                                
                case "2":
                    for items in self.inventory:
                        if type(items) == Weapon:
                            templist.append(items)
                    if len(templist) == 0:
                        pushtext("You have no weapons in your bag")
                    if len(templist) > 8:
                        sublists = [templist[x:x+8] for x in range(0, len(templist), 8)] #make lists for every 8 items
                        
                        for i in sublists:                           #iterate over lists in sublists(Pages) 
                            page = list(enumerate(i[:],1))       #make a list, of enumerated items, now tuples, starting at 1.

                            for item in page:                       #for each tuple in firstpage
                                print(f"[{str(item[0])}] {str(item[1])}")
                            
                            if len(page) >= 8:                          #if length of current page >=8 entries
                                print("[0] Next Page -->")
                            playerinput = input()
                            if playerinput == "0":
                                continue
                            if playerinput == "":
                                break
                    
                            for item in page:                #iterate over templist tuples, if item[x] matches input, equip()
                                if playerinput == str(item[0]):
                                    self.equip(item[1])
                                    return "weapon",(item[1].name)
                    
                    else:                                   #if the player doesn't have more than 9 consumable items
                        page = list(enumerate(templist[:],1))
                        for item in page:
                            print(f"[{str(item[0])}] {str(item[1])}")   #print every available consumable item
                        playerinput = input()    
                        if playerinput == "0":
                            continue
                        if playerinput == "":
                            break

                        for item in page:          #iterate over templist2 tuples, if item[0] matches input, consume()
                            if str(item[0]) == playerinput:
                                self.equip(item[1])
                                return "weapon",(item[1].name)

                case "3":
                    for items in self.inventory:
                        if type(items) == Armor:
                            templist.append(items)
                    if len(templist) == 0:
                        pushtext("You have no armor in your bag")
                    if len(templist) > 8:
                        sublists = [templist[x:x+8] for x in range(0, len(templist), 8)] #every 8 items
                        
                        for i in sublists:                           #iterate over pages of item lists one at a time
                            page = list(enumerate(i[:],1))       #make a list, of enumerated items, now tuples.
                            
                            for item in page:                       #for each tuple in templist
                                print(f"[{str(item[0])}] {str(item[1])}")
                            
                            if len(page) >= 8:                          #if length of current page >=8 entries
                                print("[0] Next Page -->")
                            playerinput = input()
                            if playerinput == "":
                                break
                            if playerinput == "0":
                                continue
                            for item in page:                #iterate over templist tuples, if item[x] matches input, equip()
                                if playerinput == str(item[0]):
                                    self.equip(item[1])
                                    return "armor", (item[1].name)
                                
                    else:               #if the player doesn't have more than 9 armor items
                        page = list(enumerate(templist[:],1))
                        for item in page:
                            print(f"[{str(item[0])}] {str(item[1])}")   #print every available consumable item
                        playerinput = input()    
                        for item in page:          #iterate over page's tuples, if item[0] matches input, equip()
                            if str(item[0]) == playerinput:
                                self.equip(item[1])
                                return "armor", (item[1].name)

                case "4":
                    return "exit"

                case "a":
                    if overworld == True:
                        for items in self.inventory:              
                            templist.append(items)
                        if len(templist) == 0:
                            pushtext("You have nothing in your inventory. (nice)")
                        if len(templist) > 8:
                            sublists = [templist[x:x+8] for x in range(0, len(templist), 8)] #make a list for every 8 items

                            for i in sublists:                       #iterate over pages of item lists one at a time
                                page = list(enumerate(i[:],1))       #make a list, of enumerated items, now tuples.

                                for item in page:                       #for each tuple in templist
                                    print(f"[{str(item[0])}] {str(item[1])}")

                                if len(page) >= 8:                          #if length of current page >=8 entries
                                    print("[0] Next Page -->")
                                print("Sorry! Using items from the inventory doesn't work at the moment! Atleast now you know what items you have :)")
                                print("Here's why if you're curious: The inventory was first implemented (correctly) while programming combat mechanics.")
                                print("The game has no idea what to do (yet) if you use any item from this list.")
                                playerinput = input()
                                if playerinput == "":
                                    break
                                if playerinput == "0":
                                    continue



    def calcdamage(self, enemydefense, enemyspeed):
        basedamage = self.attack
        if self.weapon:         #refine logic for this
            basedamage += self.weapon.attackbonus
        diceroll ={
            0 : 0, # missed attack
            1 : .7,
            2 : .75, 
            3 :.8, 
            4 : .9,
            5 : .9,
            6 : 1,
            7 : 1,
            8 : 1,
            9: 1.1,
            10: 1.75
            }
        
        if self.speed >= enemyspeed:
            roll = random.randint(1, 10)
        
        else: 
            roll = random.randint(0, 10)
        scaler = diceroll.get(roll)
        
        attacktype = "physical"
        
        return attacktype, int(max(basedamage - enemydefense, 1) * scaler), roll 
    
    def calcmagic(self, enemydefense, enemyspeed):
        
        diceroll ={
            0 : 0, # missed attack
            1 : .7,
            2 : .75, 
            3 :.8, 
            4 : .9,
            5 : .9,
            6 : 1,
            7 : 1,
            8 : 1,
            9: 1.1,
            10: 1.75
            }
        
        if self.speed >= enemyspeed:
            roll = random.randint(1, 10)
        
        else: 
            roll = random.randint(0, 10)
        scaler = diceroll.get(roll)
        attacktype = "magic"
        
        return  attacktype, int(max(self.magiclevel - enemydefense, 1) * scaler), roll

    def getAttackRating(self):
        total = self.attack
        if self.weapon:         #refine logic for this
            total += self.weapon.power
        return total

    def setName(self, text):
        self.name = text      