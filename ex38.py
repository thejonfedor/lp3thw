from io import StringIO
import sys

# initial string to work with and use as a source for the list
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# output for the user
print("Wait there are not 10 things in that list. Let's fix that.")

# define a new list 'stuff' comprised of the contents of ten_things
stuff = ten_things.split(' ')

# showing the newly-created list to the user in the command line
print("This is stuff: ", stuff)

# function to get the length of the stdout-printed list, 'stuff'
def listLength(list):
    # capture stdout output in variable. This removes it from the view of
    # the user. So the printing etc happens in the background
    old_stdout = sys.stdout
    # var to capture output from the StringIO() method
    result = StringIO()
    # set output equal to the value of result, StringIO()
    sys.stdout = result
    # print the list whose character size we want to measure
    # print as IF it's on the cmd line but it's actually in background
    print(list)
    # set listLen equal to the string printed "on screen"
    # VERSUS just using len() to measure the chars of the values in the list
    listLen = result.getvalue()
    # "turn back on" printing output to the user-visible cmd line
    sys.stdout = old_stdout
    # print listLen - user will see it now
    print("This is listLen: ", listLen)
    # NOW measure the character count of the listLen
    newListLen = len(listLen)
    # send value of function back to script where it was called
    return newListLen

# set value of listLen2 var to the output of the listLength() function
listLen2 = listLength(stuff)
# print out character-length of the PRINTED list
print("listLen is this many chars long: ", listLen2)
# create a string of dashes equal to the length of the printed list
# use for separation in the cmd line
dashes = "-" * listLen2
# print carriage return for separation
print("\n")
# tell the user what they're seeing
print("These are the contents of list, stuff:")
# print the separation line of dashes
print(dashes)
# print the contents of the list (SHEESH...finally)
print(stuff)
# print more dashes for separation
print(dashes)
# one more carriage return for "whitespace"
print("\n")
# create a new source list we'll use further below
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# intiate while loop - while length of stuff list is NOT equal to 10
while len(stuff) != 10:
    # grab the value from the end of the more_stuff list
    next_one = more_stuff.pop()
    # tell user what we're adding to list, stuff
    print("Adding: ", next_one)
    # add the item to list, stuff
    stuff.append(next_one)
    # tell the user how many items are NOW in list, stuff
    print(f"There are {len(stuff)} items now.")

# print out final value of list, stuff
print("There we go, here's list, stuff: ", stuff)
print("Here's list, more_stuff: ", more_stuff)

# tell the user we're doing more cool stuff
print("Let's do some things with stuff.\n")

# print the second item in list, stuff
print(stuff[1])
# will ALSO print the LAST item in list, stuff
print(stuff[-1]) # whoa! fancy
# remove the last item off the end of list, stuff
print(stuff.pop())

print("\nUpdated contents of list, stuff: ", stuff)
# prints list of items without the list syntax (brackets, commas, etc)
print(' '.join(stuff)) # what the... Cool!
# prints list items 3 and 4 with asterisk in between
# the range [3:5] does NOT include element 5
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