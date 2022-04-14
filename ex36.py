# The goal here is to write my own walk-through game
# Zed says to "spend a week making it as interesting
# as possible." Probably won't. But I'll make something'

from sys import exit

def dead(reason):
    print(reason, "Oy vey. \n")
    exit(0)

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
        # link to still other different function
        i = 3
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