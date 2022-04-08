the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,100):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

print(elements)

'''
Exercise Notes for ex32: Loops and Lists
1. Writing a good loop is oh-so satisfying
2. LOVE that he's teaching lists in and along with
   loop structures. Having a place to put things (lists)
   has always been one of my struggles as a programmer.
   I just haven't learned how to work with lists well.
3. Ok, we learned about for loops.
   Syntax is interesting. Looks like it's
   "for <loopVar> in <list>:"
       do this thing using loopVar
    This is probably a bad way of explaining it but I'm
    just processing now.
4. Good learning on creating an empty list with
   var = emptyList[]
   And then filling it with values using a loop and the
   emptyList.append(var) function
   Suuuuper clutch and helpful
'''