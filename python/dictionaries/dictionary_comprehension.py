# simple dictionary from a list
fruits=["apple","banana","cherry"]

fruit_dict={fruit:len(fruit) for fruit in fruits}
print(fruit_dict)

# using range()
squares={x:x**2 for x in range(1,6)}
print(squares)
cubes={x:x**3 for x in range(1,6)}
print(cubes)

# with condition
even_squares={x:x**2 for x in range(1,11) if x%2==0}
print(even_squares)
odd_squares={x:x**2 for x in range(1,11) if x%2==1}
print(odd_squares)

# swapping keys and values
students={"A":100,"B":200,"C":300}
print(students)
swapped={v:k for k,v in students.items()}
print(swapped)

s={x:x**2 for x in range(1,11)}
print(s)
