# I'll need to import stuff (argv stuff I think?)

# plan out vars needed
i = 0
numbers = []

# MISSION: refactor while-loop into a function per study drills

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
Exercise Notes for ex33refactor: While Loops
1. Refactoring this ex33 app to replace the while-loop with
   a function that can be called and reused as needed
'''