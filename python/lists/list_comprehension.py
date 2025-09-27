numbers=[x for x in range(1,10)]
print(numbers)

squares=[x*x for x in range(1,10)]
print(squares)

cubes=[x*x*x for x in range(1,10)]
print(cubes)

even=[x for x in range(1,20) if x%2==0]
print(even)

odd=[x for x in range(1,20) if x%2==1]
print(odd)

words=["apple","banana","kiwi"]
upper=[w.upper() for w in words]
print(upper)

nums=[x if x%2==0 else -x for x in range(10)]
print(nums)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
nums=[x for row in matrix for x in row]
print(nums)

nums={x:x*x for x in range(10)}
print(nums)
