# The goal here is to write my own walk-through game
# Zed says to "spend a week making it as interesting
# as possible." Probably won't. But I'll make something'

from pickle import TRUE
from sys import exit
import random, time

def dead(reason):
    print(reason, "Oy vey. \n")
    exit(0)

def grass(landing):

    while True:
        
        if landing == "elf":
            print("\nThe elf is angry and injured.")
            print("It points at you, snaps its fingers, and you land")
            print("back in the room you started, asleep, in bed...")
            time.sleep(2)
            angryElf = TRUE
            start()
        else landing == "soft":
            print("There's a shiny crytal laying in the grass.")


def window():
    fate = random.randint(0,3)

    if fate == 0:
        print("\nThe window breaks as you open it.")
        print("You fall to your death...")
        dead("\nBad luck.")
    elif fate == 1:
        print("\nYou open the window and climb down the ladder")
        grass("soft")
    elif fate == 2:
        print("\nJump out of the window and land on an angry elf.")
        grass("elf")
    elif fate == 3:
        print("\nThe window breaks as you open it.")
        print("You fall to your death...in your DREAMS")
        print("\nWhew - Good luck!")
        time.sleep(2)
        start()

def start():
    print("\nYou wake up in a warm, soft bed.")
    print("There are two doors in the room and a window.")
    time.sleep(1)
    print("Go through the left door, right door, or window.")

    choice = input("> ")

    if choice == "left door":
        # link to different function
        i = 1
    elif choice == "right door":
        # link to more different function
        i = 2
    elif choice == "window":
        window()
    else:
        print("\nREALLY? ", choice, "? Okay, well... \n")
        print("You lay back down in the bed.")
        time.sleep(4) # suspense
        print("Shortly, a wizard enters the room and casts a spell on you.")
        print("You fall into a very deep sleep and never wake again.")
        time.sleep(3) # more suspense
        dead("\nYou just got hosed by a puny Wizard. Dead.")

start()

'''
Exercise Notes for ex36: Designing and Debugging
1. 

'''