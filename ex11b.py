print("How old are you? (years)", end=' ')
age = input()
print("How tall are you? (feet and inches)", end=' ')
height = input()
print("How much do you weigh? (pounds)", end=' ')
weight = input()
newPrompt = input("Please state the nature of your request ---> ")
num1 = int(input("First number to calc: "))
num2 = int(input("Second number to calc: "))

# print statements leveraging the variables above and user input
print(f"So, you're {age} years old, {height} tall, and {weight} pounds heavy.")
print(newPrompt)
print(f"""
The numbers multiplied: {num1 * num2}
The numbers added: {num1 + num2}
The numbers divided: {num1 / num2}
""")

'''
Exercise Notes:
1. Examining the documentation for python's input() we learned:
   -Format is: input(prompt) so we add a message displayed to the user
   BEORE the cursor.
2. Added the newPrompt variable to test the prompt arg in input()
3. We added num1 and num2 vars for receiving int() input and then using
   those values in mathematical operations.
4. Zed doesn't use oxford commas so...adjust accordingly.

'''
