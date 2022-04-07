def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for extra credit, type it in anyway
print("Here is a puzzle.")

# guess at the answer: iq = 50, weight = 180, height = 74, age = 35
# so: (35 + (74 - (180 * (50 / 2)))) = -4,391
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")


'''
Exercise Notes for Functions Can Return something
1. "You can return anything you put to the RIGHT of an '+'" ~ Zed
2. One other significant concept here is calling functions as params for
   other functions e.g. add(someNum, multiply(num1, num2)) where the product
   of num1 and num2 is added to someNum.

'''
