# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes on argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no argument
def print_none():
    print("I got nothin'.")

print_two("Jon", "Fedor")
print_two_again("Jay", "Fed")
print_one("First!")
print_none()


'''
Exercise Note for Names, Variables, Code, Functions
1. NOW we're making our own functions. HELL YEAH.
2. These were very straight forward as described by Zed.
3. I guess we'll probably be passing values to these methods via input()
   pretty soon (maybe next lesson?)
4. Use this syntax for creating a function (or method)
def nameOf_Function(PARAM1,PARAM2):
    print("Do stuff in this function")
5. To 'run', 'call', or 'use' a function ALL mean the SAME thing.

'''
