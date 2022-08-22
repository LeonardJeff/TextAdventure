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
    


   
def pushtext(text, speaker = None, speed = 0, cutscenemode = False):
    """
    This function processes strings to make the text "animate" and appear slowly, text speed can be edited by editing speed
    cutscenemode makes text automatically advance for you.
    speed:
    0.015 = excited crazy
    0.02 = mad at you
    0.03 = default speed
    0.07 = agonizingly slow
    """
    if text == None:
        return
    if cutscenemode == True:    #cutscene mode is for auto text
        if speaker == None:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
            time.sleep(0.3)
        if speaker:
            sys.stdout.write(speaker + ": ")
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
            time.sleep(0.5)
                
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
    else:
        return

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