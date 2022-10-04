import os
import time
import sys
from tkinter import StringVar
from tokenize import String
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
    

def checkmax(n, min, max):
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n
   
def pushtext(text, speaker = None, speed = 0, cutscenemode = False):
    """
    This function processes strings to make the text "animate" and appear slowly, text speed can be edited by editing speed
    cutscenemode makes text automatically advance for you.
    speed:
    0.015 = excited crazy
    0.02 = faster
    0.025 = default speed
    0.07 = agonizingly slow
    """
    if type(text) == str:   #if the input is a string, display string
        textlist = []
        textlist.append(text)
    if type(text) == list or type(text) == tuple:  #if the input is a list, display multiple lines of each string in the list.
        textlist = []
        for t in text:
            textlist.append(t)
    if text == None:
        return

    if cutscenemode == True:    #cutscene mode is for auto text
        if speaker == None:
            for text in textlist:               
                for char in text:   #display characters one  at a time
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(speed)
                time.sleep(0.5)
        if speaker:
            sys.stdout.write(speaker + ": ")       
            for text in textlist:                                             
                if text.startswith("@") == True:    #if the input text starts with @
                    text = text.lstrip("@")

                    for char in text:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(speed)
                    time.sleep(0.5)
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(speed)
                time.sleep(0.5)

                
    if cutscenemode == False:
        if speaker == None:
            for text in textlist:
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(speed)
                input()
        else:                 
            for text in textlist:                                             
                if text.startswith("@") == True:    #if the input text starts as @
                    text = text.lstrip("@")
                    for char in text:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(speed)
                    time.sleep(0.2)
                    input()
                else:
                    sys.stdout.write(speaker + ": ")
                    for char in text:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(speed)
                    time.sleep(0.2)
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