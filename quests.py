from quest import Quest
from items import *

firstquest = Quest(
    item = woodenplanks, 
    goalamount = 2,
    name="Frank's Menial Labor",
    hint="Bring two bundles of planks back to Frank.")

secondquest = Quest(
    item = coyotebones, 
    goalamount= 3,
    name = "Hunter's Quest",
    hint = "Find this man 3 coyote bones.")

thirdquest = Quest(
    item = woodenplanks, 
    goalamount = 5,
    name="Magician's Secrets",
    hint="Hubert says he needs help finding ingredients for his secret... plan.")

fourthquest = Quest(                        #This is the last quest... for now.
    item = woodenplanks, 
    goalamount = 1,
    name="Tail's End",
    hint="Take down Garg the Goblin King, the hunter claims he is located at the goblin encampment to the east.")