age=int(input("Enter our age : "))

if age<0:
    raise ValueError("Age cannot be negative!")
else:
    print(f"Your age is {age}.")