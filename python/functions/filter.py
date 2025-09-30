nums=[1,2,3,4,5,6]

# keep even numbers using lambda
evens=list(filter(lambda x:x%2==0,nums))
print(evens)

# using a named predicate
def is_odd(x): return x%2==1

odds=list(filter(is_odd,nums))
print(odds)

# remove falsy values
vals=["hello","",None,"0",0,[],[1]]
print(list(filter(None,vals)))