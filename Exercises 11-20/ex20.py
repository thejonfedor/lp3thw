# import modules to use in script
from sys import argv

# define vars to pass to script when calling from CLI
script, input_file = argv

# new function print_all()
def print_all(f):
    # show opened file to user
    print(f.read())

# new function rewind()
def rewind(f):
    # set the position of the file handler which is reading the opened file
    f.seek(0)

# new function print_a_line()
def print_a_line(line_count, f):
    # printing one, single line out for the user using readline()
    print(line_count, f.readline(), end='')

# new var passes file defined in argv at start of script
current_file = open(input_file)

# prompting the user about the process being used here
print("First let's print the whole file:\n")

# calling print_all to display entire file to user in CLI
print_all(current_file)

# print more instructions to user
print("Now let's rewind, kind of like a tape.")

# calling rewind to send the file handler back to beginning of current_file
rewind(current_file)

# print log for user
print("Let's print three lines:")

# define var current_line for user log
current_line = 1
# call print_a_line to print the first line of current_file
print_a_line(current_line, current_file)

# increment current_line to 2
current_line += 1
# call print_a_line to print the next line of current_file (line 2)
print_a_line(current_line, current_file)
# print(f"var 'current_line' is {current_line}")

# increment current_line to 3
current_line += 1
# call print_a_line to print the next line of current_file (line 3)
print_a_line(current_line, current_file)
# print(f"var 'current_line' is {current_line}")


'''
Exercise Notes for Functions and Files
1. Notes about the python seek() function
   https://www.geeksforgeeks.org/python-seek-function/
2. Notes about the python readline() method
   Returns a single line from the file at the position of the file handler
   https://www.w3schools.com/python/ref_file_readline.asp
3. += adds a number to a var, changing the var value itself in the process.
4. Regarding seek(0), Zed's explanation is actually really good here:
       "How does readline() know where each line is? Inside readline()is code
       that scans each byte of the file until it finds a \n character, then
       stops reading the file to return what it found so far. The file f is
       responsible for maintaining the current position in the file after each
       readline() call, so that it will keep reading each line."
'''
