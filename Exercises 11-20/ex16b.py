from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.writelines([line1, "\n", line2,"\n", line3, "\n"])
''' rewriting this section with the line above using writelines()
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
target.close()

# added this section to print the new file contents to the CLI during runtime
print("----This is the new file content you wrote:----")
print(open(filename, "r").read())
print("----line above is end of file----")

print("And finally, we close it.")
target.close()


'''
Exercise Notes for Reading and Writing Files
1. My first answer to rewriting the multiple var.write() statements was to
   collapse each command into a single string and then write that one string.
   toWrite = line1 + "\n" + line2 + "\n" + line3 + "\n"
   target.write(toWrite)
2. Turns out that python's got a writelines() method that I can use instead of
   write(). Here's how it would work:
   target.writelines([line1, "\n", line2,"\n", line3, "\n"])

'''
