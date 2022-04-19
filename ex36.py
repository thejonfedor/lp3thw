# The goal here is to write my own walk-through game
# Zed says to "spend a week making it as interesting
# as possible." Probably won't. But I'll make something'

from sys import exit
import random, time

def msg (write):
    print("***************************************************")
    print(write)
    print("***************************************************")
    return

def bigDarkPlace():
    print("\nYou land in a dark, dank dungeon.")
    dead("You have no hope of surviving. Goodbye.")

def cloudCity():
    print("\nThis is the cloud function.")
    print("You have no hope of surviving. Goodbye.")
    dead("Because cloud city probz.")

def dead(reason):
    print(reason, "Oy vey. \n")
    exit(0)

def front():
    print("\nYou arrive at the front of the building.")
    print("An armed and angry-looking minotaur stands guard.")
    dead("The minotaur strikes you. Instant death.")

def grass(landing,dreaming,injured):
    
    if landing == "elf": 
        print("\nThe elf is angry and injured.")
        print("It points at you, snaps its fingers, and you land")
        print("back in the room you started, asleep, in bed...")
        time.sleep(2)
        angryElf = True
        dreaming = 0
        start(dreaming,injured)
    elif landing == "hard":
        injured = True
        print("\nAs you land you hear something snap. Much pain.")
        print("Do you call for help or crawl for a while?")
        injuredChoice = input("> ")
        
        if injuredChoice == "crawl":
            print("\nYou crawl through the grass for a while.")
            print("You eventually find a shiny crystal laying in the grass.")
        elif injuredChoice == "call for help":
            print("\nYou call for help and alert enemies nearby to your presence.")
            print("Restless group of scurvy dwarves carries you away to a dungeon.")
            bigDarkPlace()
    else:
        print("\nThere's a shiny crytal laying in the grass.")
    
    i = 0

    while True:
        crystalChoice = input("> ")

        if "pick" and "up" in crystalChoice and not injured:
            print("\nPower courses through your hands and arms.")
            print("You begin rising into the air toward a floating cloud.")
            cloudCity()
        elif "pick" and "up" in crystalChoice and injured:
            print("\nPower courses through your arms.")
            print("You ask the crystal to heal your injured legs.")
            time.sleep(2)
            print("You're healed! Such wow. Much amaze.")
            print("You start walking.")
            injured = False
            front()
        elif "kick it" in crystalChoice and not injured:
            print("\nThe crytal turns blood red.")
            time.sleep(2)
            print("It starts to vibrate violently. Then disappears.")
            time.sleep(2)
            print("A trap door opens under your feet.")
            bigDarkPlace()
        elif "kick it" in crystalChoice and injured:
            print("\nThe crytal turns blood red.")
            time.sleep(2)
            print("It starts to vibrate violently. Then disappears.")
            time.sleep(2)
            print("A trap door opens under you. You fall into the dark.")
            bigDarkPlace()
        elif i == 3:
            print("\nYou should probably kick it or pick it up.")
        else:
            i = i + 1        

def window(dreaming,injured):
    if dreaming == 0:
        # if player already fell in the dreams, that doesn't happen again
        fate = random.randint(0,1)
    else:
        fate = random.randint(0,3)

    if fate == 0:
        print("\nThe window breaks as you open it.")
        print("You fall to the ground below.")
        grass("hard", dreaming,injured)
    elif fate == 1:
        print("\nYou open the window and climb down the ladder")
        grass("soft", dreaming,injured)
    elif fate == 2:
        print("\nJump out of the window and land on an angry elf.")
        grass("elf", dreaming,injured)
    elif fate == 3:
        print("\nThe window breaks as you open it.")
        print("You fall to your death...in your DREAMS")
        time.sleep(2)
        print("\nWhew - Good luck!")
        time.sleep(2)
        start(0,injured)
    else:
        print("Something went wrong and you wake up back in bed.")
        start(0,injured)

def start(dreaming,injured):
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
        window(dreaming,injured)
    else:
        print("\nREALLY? ", choice, "? Okay, well... \n")
        print("You lay back down in the bed.")
        time.sleep(4) # suspense
        print("Shortly, a wizard enters the room and casts a spell on you.")
        print("You fall into a very deep sleep and never wake again.")
        time.sleep(4) # more suspense
        dead("\nYou just got hosed by a puny Wizard. Dead.")

start(1,False)

'''
Exercise Notes for ex36: Designing and Debugging
1. 

'''