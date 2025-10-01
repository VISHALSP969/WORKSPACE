# sumusing recursiom

def sum(n):
    if n!=0:
        return n+sum(n-1)
    else:
        return 0
    
print(sum(5))
print(sum(10))