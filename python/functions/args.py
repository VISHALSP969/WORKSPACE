def add_numbers(*args):
    print("Arguments : ",args)
    return sum(args)

print(add_numbers(1,2))
print(add_numbers(1,2,3))
print(add_numbers(1,2,3,4))