import os
import time
import sys
from types import NoneType
def getLowerInput():
    value = input()
    return value.lower()

def compareblename(name:str): 
    """
    This function takes a name in and removes spaces and makes it all lowercase.
    This is for comparing user input to item/npc/scenery/etc... names
    """
    return name.lower().replace(" ","")
    


   
def pushtext(text, speaker = None, speed = 0, cutscenemode = False, cutscenemodeendspeed = 1):
    if cutscenemode == True:
        if speaker == None:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
            time.sleep(1)
        if speaker:
            sys.stdout.write(speaker + ": ")
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
            time.sleep(1)
                
    if cutscenemode == False:
        if speaker == None:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
            input()
        else:
            sys.stdout.write(speaker + ": ")
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)      
            input()
    if text == None:
        return
    else:
        return



def printmultilines(string):
    for char in range(len(string)):
        print(string[char], end="")
        time.sleep(.1/10)
        #for a noticable reduction in output speed
    print("")

def questunf(quest):
        idk = str(quest.item)
        if (quest.goalamount - quest.progress) == 1:       
            if idk.endswith("s"):      
                return("I still need one more " + str(quest.item) + ".")
            else:
                return("I still need one more "+ str(quest.item) + "s.")
        else:
            if idk.endswith("s"):      
                return("I still need " + str(quest.goalamount - quest.progress) + " more " + str(quest.item) + ".")
            else:
                return("I still need " + str(quest.goalamount - quest.progress) + " more " + str(quest.item) + "s.")