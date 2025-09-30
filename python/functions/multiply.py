def multiply(*args):
    product=1
    for num in args:
        product*=num
    return product

print(multiply(1,2))
print(multiply(1,2,3))
print(multiply(1,2,3,4))