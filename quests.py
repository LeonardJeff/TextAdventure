from quest import Quest
from items import *

firstquest = Quest(
    item = woodenplanks, 
    goalamount = 2,
    name="Frank's Menial Labor",
    hint="Bring two bundles of planks back to Frank.")

secondquest = Quest(
    item = woodenplanks, 
    goalamount= 1,
    name = "Hunter's Quest",
    hint="Take down Garg the Goblin King, the hunter claims he is located at the goblin encampment to the east.")

thirdquest = Quest(
    item = woodenplanks, 
    goalamount = 5,
    name="Magician's Secrets",
    hint="Hubert says he needs help finding ingredients for his secret... plan.")

fourthquest = Quest(                        #This is the last quest... for now.
    item = woodenplanks, 
    goalamount = 1,
    name="Tail's End",
    hint="Deliver tail to guy in galawyn")