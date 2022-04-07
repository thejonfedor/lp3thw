tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
ranString = '''
I'm a \"little\" teapot \t\r*short* \t\r*and* \t\r*stout*
this is my handle, this is my spout
'''


fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print(ranString)
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

'''
Exercise notes
1. When creating long strings in the editor inside vars, use triple quotes
   to make them fit into the 80-char range default
2. Re: Carriage returns from StackOverflow: "\r takes the cursor to the
   beginning of the line. It is the same effect as in a physical typewriter
   when you move your carriage to the beginning and overwrite whatever
   is there."
'''
