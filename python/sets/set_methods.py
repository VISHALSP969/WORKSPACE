fruits={"apple","banana"}
print(fruits)

# add an element
fruits.add("cherry")
print(fruits)

# add multiple element
fruits.update(["grapes","mango"])
print(fruits)

# remove element
fruits.remove("banana")
print(fruits)

# fruits.remove("banana")   # key error

fruits.discard("grapes")
print(fruits)

fruits.discard("grapes")    # no error

# remove random element
item=fruits.pop()
print(item)
print(fruits)

# remove all elements
fruits.clear()
print(fruits)

