# The goal here is to write my own walk-through game
# Zed says to "spend a week making it as interesting
# as possible." Probably won't. But I'll make something'

from sys import exit
import random, time

def bigDarkPlace():
    print("\nYou land in a dark, dank dungeon.")
    print("You have no hope of surviving. Goodbye.")
    dead()

def cloudCity():
    print("\nThis is the cloud function.")
    print("You have no hope of surviving. Goodbye.")
    dead("Because cloud city probz.")

def dead(reason):
    print(reason, "Oy vey. \n")
    exit(0)

def grass(landing):
    
    if landing == "elf":
        print("\nThe elf is angry and injured.")
        print("It points at you, snaps its fingers, and you land")
        print("back in the room you started, asleep, in bed...")
        time.sleep(2)
        angryElf = "yes"
        start()
    else:
        print("\nThere's a shiny crytal laying in the grass.")
    
    i = 0

    while True:
        crystalChoice = input("> ")

        if "pick" and "up" in crystalChoice:
            print("\nPower courses through your hands and arms.")
            print("You begin rising into the air toward a floating cloud.")
            cloudCity()
        elif "kick it" in crystalChoice:
            print("\nThe crytal turns blood red.")
            time.sleep(2)
            print("It starts to vibrate violently. Then disappears.")
            time.sleep(2)
            print("A trap door opens under your feet.")
            bigDarkPlace()
        elif i == 3:
            print("\nYou should probably kick it or pick it up.")
        else:
            i = i + 1        

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