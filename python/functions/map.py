nums=[1,2,3,4,5]
def square(x): 
    return x*x

# using named function
print(list(map(square,nums)))

# using lambda
print(list(map(lambda x:x*x,nums)))

# map with multiple iterables
a=[1,2,3]
b=[10,20,30]
print(list(map(lambda x,y: x+y,a,b)))

# map to transform types
strs=["1","2","3"]
print(list(map(int,strs)))