from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
# in_file = open(from_file)
# DONE...below
indata = open(from_file, "r+").read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()

'''
Exercise Notes for More Files
1. Did some research on using CLI to look at open files and finding files open
   in the process. Great resource here: https://alvinalexander.com/blog/post/linux-unix/linux-lsof-command/
2. I ended up using:
   lsof -p [PIDnum] | head
   to get a list of all the open files running in my Terminal process
   with headers. This works in the linux environment as well.
3.
'''
