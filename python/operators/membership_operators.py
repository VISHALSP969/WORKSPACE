print('c' in "cat")
print(3 in [1,2,3])
print('key' in {'key':10})
print(4 not in {1,2,3})

d={"name":"John","age":22,"city":"Delhi"}
print("name" in d)
print("age" in d)
print("hobby" not in d)

print("John" in d)      # False
print("John" in d.values()) # True