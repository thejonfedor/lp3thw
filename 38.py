from io import StringIO
import sys

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
print("This is stuff: ", stuff)
# listLen = sum(len(i) for i in stuff)

old_stdout = sys.stdout

result = StringIO()
sys.stdout = result

print(stuff)

listLen = result.getvalue()

sys.stdout = old_stdout

print("This is listLen: ", listLen)
newListLen = len(listLen)
print("listLen is this many chars long: ", newListLen)

stars = "*" * newListLen
print("\n")
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