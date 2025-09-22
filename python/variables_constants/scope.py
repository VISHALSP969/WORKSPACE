x=10    # global

def foo():
    x=5     # local - different from global x
    print(x)

foo()       # prints 5
print(x)    # prints 10