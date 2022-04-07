# Calculate F temps in C and K

# input temp in F
F = 41 # deg Fahrenheit
C = round((F - 32) * 5 / 9, 2) # WRT F
K = round((F - 32) * 5 / 9 + 273.15, 2) # WRT F

print("Start with temp in F")

print(f"Temp is {F} degrees Fahrenheit")

print(f"Temp in C is {C} degrees")

print(f"Temp in K is {K} degrees")
