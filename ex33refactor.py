# I needed the randint() function so I imported random
# not actually sure if I needed to or not
import random

# create empty list
numbers = []
# get number from user for size of list we'll create
num = input("What size should the list be? >> ")
# convert that str into type int
listSize = int(num)

# helps the user follow along
print("The max number is :", listSize)

# refactored the previous while-loop into a function
# function has one parameter: integer 'size'
# 'size' is defined by the user from the command line
def main(size):
    for i in range(0, size):
        val = random.randint(1,100)
        numbers.append(val)

# call the new function I wrote
main(listSize)

print("The numbers: ")

# modified this too so you can see the val of each 
# index in the list
for num in numbers:
    print(numbers.index(num), "Value: ", num)

# view entire list
print(f"Here are all the list values: ", numbers)

'''
Exercise Notes for ex33refactor: While Loops
1. Refactoring this ex33 app to replace the while-loop with
   a function that can be called and reused as needed
'''