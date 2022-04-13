# assign var value
types_of_people = 10
# f string inside var
x = f"There are {types_of_people} types of people."

# short string
binary = "binary"
# another short string
do_not = "don't"
# another f string stored inside a variable
y = f"Those who know {binary} and those who {do_not}."

# print var x
print(x)
# print var y
print(y)

# print f string including var x
print(f"I said: {x}")
# print f string including var y
print(f"I also said: '{y}'")

# var with boolean value
hilarious = False
# setting up string with empty curly brackets to be filled by .format()
joke_evaluation = "Isn't that joke so funny?! {}"

# print var joke_evaluation with .format()
print(joke_evaluation.format(hilarious))

# define string var w
w = "This is the left side of..."
#define string var e
e = "a string with a right side"

# concatenate w & e
print(w + e) #concatenation

'''
Exercise notes
1. .format() takes another arg or var and adds it to {} in some string.
'''
