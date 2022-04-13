# This is a var
types_of_people = 10
# Define var, x with f string
x = f"There are {types_of_people} types of people."

# Define var
binary = "binary"
#Define var
do_not = "don't"
# Define var using above vars in a sentent print f
y = f"Those who know {binary} and those who {do_not}."

# two print statements
print(x)
print(y)

# two print f strings using above vars
print(f"I said: {x}")
print(f"I also said: '{y}'")

# define more vars
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# print statement. Places val of hilarious var in curly brackets of
# joke_evaluation...I think. Yes, it does.
print(joke_evaluation.format(hilarious))

# define two vars containing strings
w = "This is the left side of..."
e = "a string with a right side."

# concatenate strings in this print statement
print(w + e)

# Drills / Lessons
# 1. Added comments to above all lines to describe what they do
# 2. There are five places in this exercise where strings are inside of strings
# 3. Introducing the Break It exercise: ask other people to break my code
#    so I can try to find and fix the breaks.
