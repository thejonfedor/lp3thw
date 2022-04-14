# The goal here is to write my own walk-through game
# Zed says to "spend a week making it as interesting
# as possible." Probably won't. But I'll make something'

from sys import exit
import random

def dead(reason):
    print(reason, "Oy vey. \n")
    exit(0)

def window():
    fate = random.randint(0,2)

    if fate == 0:
        print("\nThe window breaks as you open it.")
        print("You fall to your death")
        dead("\nBad luck.")
    elif fate == 1:
        print("\nYou open the window and climb down the ladder")
    elif fate == 2:
        print("Jump out of the window and land on an angry elf.")

def start():
    print("You wake up in a warm, soft bed.")
    print("There are two doors in the room and a window.")
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
        print("Shortly, a wizard enters the room and casts a spell on you.")
        print("You fall asleep very deep and never wake again.")
        dead("You just got hosed by a puny Wizard. Dead.")

start()

'''
Exercise Notes for ex36: Designing and Debugging
1. 

'''