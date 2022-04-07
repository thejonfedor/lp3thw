name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
heightcm = height * 2.54 # inches to cm
heightcmround = round(heightcm, 1) #show this var to user
weight = 180 # lbs
weightkg = weight / 2.205 # lbs to kg
weightkground = round(weightkg, 2) #show this var to user
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print(f"Let's talk about {name}.")
print(f"He's {height} inches ({heightcmround} cm) tall.")
print(f"He's {weight} pounds ({weightkground} kg) heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

'''
Exercise notes
1. The f goes inside the first open parenthesis
2. Vars need to start with a character NOT a number.
3. round(arg) outputs an integer value with nothing to the right of decimal
   Need to add in a 2nd arg to round(arg,digits) to get a specific number of
   digits in the rounded output.
'''
