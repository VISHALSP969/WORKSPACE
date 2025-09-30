from functools import reduce
import operator

def factorial(n):
    if n<2:
        return 1
    return reduce(operator.mul,(range(1,n+1)))

print(factorial(5))