# a string var that also defines a format for printing other information
formatter = "{} {} {} {}"

# print 1,2,3,4 using the format() and formatter var
print(formatter.format(1, 2, 3, 4))
# print the strings using the format() and formatter var
print(formatter.format("one", "two", "three", "four"))
# print boolean values using the format() and formatter
print(formatter.format(True, False, False, True))
# print the formatter var four times using the format() and formatter var
print(formatter.format(formatter, formatter, formatter, formatter))
# print four strings using format() and formatter var
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
