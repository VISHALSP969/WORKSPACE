lst=[1,2,3,4,5]
print(lst)
print(id(lst))
lst.append(6)   # modifies the same list object
print(lst)
print(id(lst))

s="hello"
print(s)
s.upper()   # creates a new string; original "hello" unchanged
print(s)