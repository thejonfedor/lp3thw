print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everwhere that Mary went.")
print("." * 10) #what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# Testing lesson 2 from below
print("val","val2",sep='--',end=' <3')

# Drills / Lessons
# 1. I removed the ' ' value of the end var in the second to last print.
#    it's just a space BUT when I changed 'end' to 'f', I got an error.
#    Not sure why we need 'end' as the last argument in the print statement
#    in order for the string to work.
# 2. Figured it out. The print() function has a number of args including 'end'
#    as well as 'sep' which allows you to insert a separation val between two
#    strings you want to print. Ex: print("val","val2",sep='--')
