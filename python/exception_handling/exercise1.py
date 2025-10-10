fruits=["apple","banana","cherry"]
try:
    index=int(input("Enter the index : "))
    print(fruits[index])
except IndexError:
    print("Out of range!")