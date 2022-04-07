# Import the argv library or module from sys
from sys import argv

# Define the vars for argv (NEED to be defined by user when running script)
script, filename = argv

# define var text to open the file to read
txt = open(filename)

# print out the message to user detailing which file will be opened and read
print(f"Here's your file {filename}: ")
# print out the contents of the filename
print(txt.read())

# print instructions for the user
print("Type the filename again: ")
# Prompt the user to write out the name of the file they want to open and read
file_again = input("> ")

# Open the file the user defined
txt_again = open(file_again)

# print out the contents of the file the user wanted to open
print(txt_again.read())

'''
Exercise Notes:
1. Was especially valuable to go through and comment each line of this script
2. Commands = funtions = methods. This is important. For instance, when I see
   open(), I hear in my head, "the open function". It's also the open method.
   Lingo, man.
3.
'''
