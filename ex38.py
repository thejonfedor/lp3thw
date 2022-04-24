from io import StringIO
import sys

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
print("This is stuff: ", stuff)

def listLength(list):

    old_stdout = sys.stdout

    result = StringIO()
    sys.stdout = result

    print(list)

    listLen = result.getvalue()

    sys.stdout = old_stdout

    print("This is listLen: ", listLen)
    newListLen = len(listLen)
    return newListLen

listLen2 = listLength(stuff)

print("listLen is this many chars long: ", listLen2)

stars = "-" * listLen2
print("\n")
print("These are the contents of list, stuff:")
print(stars)
print(stuff)
print(stars)
print("\n")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what the... Cool!
print('#'.join(stuff[3:5])) 

'''
Exercise Notes for ex38: Doing Things to Lists
1. Problem: I want to put lines above and below the printed list
   I want to do this by finding the length of the print output
   and using that to write the correct length of the printed list
   Tried to solve this problem with:
        listLen = sum(len(i) for i in stuff)
   this wasn't a bad idea (thank you StackOverflow) 
   BUT it ONLY counts the characters of each element 
   in the list...NOT the total printed output of the list
2. asdf
'''