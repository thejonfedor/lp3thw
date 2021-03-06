from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    # ADDED an error-catching while loop to ensure the player
    # is entering an integer number for the amount of
    # gold to take

    while True:
        try:
            choice = input("> ")
            choiceInt = int(choice)
            break
        except ValueError:
            print(f"Enter an integer number, fool.")
 
    if choiceInt < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means. Try again.")
    

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
    

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# program starts running here. Important to know for debug
start()


'''
Exercise Notes for ex35: Branches and Functions
1. Made a few typing errors.
   - left off a couple of colons at the end of boolean conditions
   - had a big problem with definining functions
     ended up incorrectly tabbing the 'def's such that the
     functions didn't end up intializing correctly
2. SOLVED: I can't seem to get the gold_room() function to trip
   the 'Nice person' condition
3. For debugging and error handling I literally just
   ripped off the python.org code from the link below:
   https://docs.python.org/3/tutorial/errors.html#handling-exceptions
4. Also, I used the debugger in VS Code *extensively* while
   working through the Study Drills. SUPER. HELPFUL. DANG.
   Works very similarly to the script debugger packaged with
   Filemaker Pro (RIP).
'''