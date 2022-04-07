import random

# def a new funtion with two params
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print contents of cheese_count
    print(f"You have {cheese_count} cheeses!")
    #print contents of boxes_of_crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # print text
    print("Man that's enough for a party!")
    #print more text
    print("Get a blanket.\n")

#def new function to be called 10+ ways
def charStats(valA, valB):
    lenA = len(str(valA))
    lenB = len(str(valB))
    print(f'''
    What are we workin' with?
    valA = {str(valA).upper()} and is {lenA} chars long
    valB = {str(valB).upper()} and is {lenB} chars long
    Are the values identical? {valA == valB}
    Ok - but are they the same length? {lenA == lenB}
    ''')

# print text so user can follow along
print("We can just give the function numbers directly:")
# pass 20 and 30 to the new function, cheese_and_crackers
cheese_and_crackers(20, 30)

# print text so user can follow along
print("OR, we can use variables from our script")
# def var
amount_of_cheese = 10
# def var
amount_of_crackers = 50

#pass vars to cheese_and_crackers function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print text so user can follow along
print("We can even do math inside too:")
# pass params to cheese_and_crackers() including math calcs
cheese_and_crackers(10 + 20, 5 + 6)

# print text so user can follow along
print("And we can combine the two, variables and math:")
# pass params to cheese_and_crackers including vars and maths
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("Function Call 1")
charStats(input("Type me something > "), input("Type me something else > "))

print("Function Call 2")
charStats("Seventy one", "One hundred")

print("Function Call 3")
charStats(351, "One hundred")

print("Function Call 4")
charStats(20, 30)

print("Function Call 5")
charStats(len(open('ex18b.py', "r").read()),len(open('ex19b.py', "r").read()) )

print("Function Call 6")
charStats(len(open('ex18b.py', "r").read()),len(open('ex18b.py', "r").read()) )

print("Function Call 7")
charStats(input("Give me a number 0 - 9 > "), random.randint(0,9))

print("Function Call 8")
charStats(input("Give me another number 0 - 99 > "), random.randint(0,99))

print("Function Call 9")
charStats(34 + 56, 2 + 2)

print("Function Call 10")
charStats("This is the end", "Or is it?" + "Another one")


'''
Exercise Notes for Functions and Variables
1. The variables in your functions are NOT connected to the variables
   in your script.
2. Well now...THAT was interesting. Good experience. A bit painful. But good.
   Glad I took the time to write that new function and 10 new calls.
3. Man I learned all KINDS of new things in this one trying to create all those
   new function calls.
   - Including importing the random module and calling randint() to get a random
   integer. FUN
   - Leveraging input prompts as function params
   - working more with the len() and str() functions (there are a number of
   limitations including that len() only works for strings, apparently).
'''
