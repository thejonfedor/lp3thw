from sys import argv

script, user_name = argv
p = 'Type answer --> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(p).upper()

print(f"{user_name}, where do you live?")
lives = input(p).upper()

print("What kind of computer to you have?")
computer = input(p).upper()

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

'''
Exercise Notes for ex14 - Prompting and Passing
1. I tried a bunch of things to try and make the variables I collected from
   user to look ok in Terminal. I settled on case caps. And then needed to
   figure out how to make the likes, lives, and computer vars case caps.
   Turns out the easiest way is to append the .upper() function to the end of
   each var as you can see in the code above.
2. ALSO, should have read the damn documentation on the upper() function.
   I was trying to pass parameters to it. WRONG. All I needed to do was
   dot-append it to the end of the input prompts in the vars defined above.
   Easy. Done.

'''
