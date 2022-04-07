name = 'Zed A. Shaw'
age = 35 # not  a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
# Per Study Drills: below is the conversion from inches to centimeters
cm = 0.393701 # in to 1 cm
# Per Study Drills: below is the conversion from pounds to kilograms
kg = 2.20462 # lbs to 1 kg
# New var to take care of unit conversion math BEFORE priting
height_cm = round(height * cm, 2)
weight_kg = round(weight * kg, 2)

print(f"Let's talk about {name}.")
# added metric measurements per Study Drills section
# print(f"He's {height} inches tall ({round(height * cm, 2)} cm).")
print(f"He's {height} inches tall ({height_cm} cm).")
# added metric measurements per Study Drills section
# print(f"He's {weight} pounds heavy ({round(weight * kg, 2)} kg).")
print(f"He's {weight} pounds heavy ({weight_kg} kg).")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Drill / Lesson notes
# 1. Great practice adding in the weight and height unit conversions
#    Used Google to look up the decimal-value conversions
# 2. Added the conversions into the print statements and the resulting
#    decimals were LONG. First tried the float() function. Obviously, didn't
#    work. Needed to round the decimal so I looked up the round() function.
#    works just like Excel round(value_to_round,num_places). Done.
# 3. I could also have done the math in vars instead of writing out the
#    math in print strings. That would have been more efficient. Going
#    back to do that now.
