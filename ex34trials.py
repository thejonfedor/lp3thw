# wrote this to screw around with the example in the
# first paragraph of the lesson description

animals = ['bear', 'tiger', 'penguin', 'zebra']

show = input("What animal do you want to see? (0-3) >> ")
# need to convert user input (str) into an int
showInt = int(show)

print("Var 'show' is ", showInt)

print("Position [", showInt, "] contains", animals[showInt])

print(f"Here's the entire list: ", animals)

'''
Exercise Notes for ex34trials: Accessing Elements of Lists
1. This lesson covered ordinal vs cardinal numbers
2. Cardinal = "first, second, third" where the number line
   starts with '1'
3. Ordinal = number line that starts with zero, (0)
   0,1,2,3,4
4. Lists use ordinal numbers to address each element.
   Therefore, the first value in the list is at element[0]
'''