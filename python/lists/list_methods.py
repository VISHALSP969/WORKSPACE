fruits=["apple","banana"]
print(fruits)
fruits.append("cherry")
print(fruits)
print("////////////////////////////")

fruits=["apple","banana","cherry"]
print(fruits)
fruits.insert(1,"mango")
print(fruits)
print("////////////////////////////")

numbers=[1,2,3,2,4]
print(numbers)
numbers.remove(2)
print(numbers)
# numbers.remove(9)     # value error
print("////////////////////////////")

fruits=["apple","banana","cherry"]
print(fruits)
print(fruits.pop())
print(fruits)
print(fruits.pop(0))
print(fruits)
# fruits.pop(10)    # index error
print("////////////////////////////")

nums=[5,2,9,1,7]
print(nums)
print(nums.sort())
print(nums)

nums=[5,2,9,1,7]
print(nums)
nums.sort(reverse=True)
print(nums)

fruits=["mango","orange","apple","cherry"]
print(fruits)
fruits.sort()
print(fruits)
print("////////////////////////////")

nums=[1,2,3,4]
print(nums)
nums.reverse()
print(nums)
print("////////////////////////////")

a=[1,2,3]
b=[4,5,6]
print(a)
print(b)
a.extend(b)
print(a)
print(b)
b.extend("abc")
print(b)
b.append("abc")
print(b)
print("////////////////////////////")

letters=["a","b","c","b"]
print(letters)
print(letters.index("b"))
# print(letters.index("z")) # value error
print("////////////////////////////")

nums=[1,2,2,3,2]
print(nums)
print(nums.count(2))
print(nums.count(7))
print("////////////////////////////")

a=[1,2,3]
b=a.copy()
print(a)
print(b)
print(id(a),id(b))
b.append(4)
print(a)
print(b)
print("////////////////////////////")

nums=[1,2,3]
print(nums)
nums.clear()
print(nums)
print("////////////////////////////")