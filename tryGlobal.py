
def myfunc(x):
  print("x's value is", x)
  x = x - 1
  anotherFunc(x)

def anotherFunc(x):
  print("x's value is", x)
  x = x - 1
  start(x)

x = 3

print("start with x =", x)

def start(x):
    if x >= 0:
        myfunc(x)
    else:
        print("END. Value of x =", x)

start(x)
