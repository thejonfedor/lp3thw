people = 30
cars = 40
trucks = 40


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars or cars == trucks:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

'''
Exercise Notes for ex30: Else and If
1. Really complex if statements are generally bad style
   Keep them tight and crisp
2. elif and else are "else if" and "else" statments
   that provide alternative statements to the first
   boolean if-statement
'''