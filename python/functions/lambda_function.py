# named function
def add(a,b):
    return a+b

# lambda
add_lambda=lambda a,b:a+b
print(add_lambda(2,3))
print(add_lambda(10,7))

# inline with sorted
names=["alice","Bob","charlie"]
print(sorted(names,key=lambda s:s.lower()))