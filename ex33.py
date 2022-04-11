i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    print("----------") # added for clarity when running


print("The numbers: ")

for num in numbers:
    print(num)

'''
Exercise Notes for ex33: While Loops
1. REAL flow controls. lezzzGOOO
2. While loops are more...risky than for-loops
   e.g. it's easier to write yourself into an infinite loop
   Use for-loops whenever possible unless a
   while-loop is straight up better for the job.
3. Might be good to come up with a generic test for
   while-loops that I can use in every one I write
   that will stop the loop at some point no matter what
   in case I make a mistake. Is this possible?
'''