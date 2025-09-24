# Simple Calculator CLI App
print("----- Simple Calculator -----")

# Taking input from the user
num1,num2=map(float,input("Enter two numbers : ").split())

print("Choose operation :")
print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
print("5.Modulus(%)")
print("6.Power(**)")

# Taking choice input
choice=input("Enter operation symbol (+,-,*,/,%,**) : ")

# Performing operations
if choice=='+':
    print(f"Result : {num1}+{num2}={num1+num2}")
elif choice=='-':
    print(f"Result : {num1}-{num2}={num1-num2}")
elif choice=='*':
    print(f"Result : {num1}*{num2}={num1*num2}")
elif choice=='/':
    if num2!=0:
        print(f"Result : {num1}/{num2}={num1/num2}")
    else:
        print("Error:Division by zero is not allowed.")
elif choice=='%':
    if num2!=0:
        print(f"Result : {num1}%{num2}={num1%num2}")
    else:
        print("Error:Division by zero is not allowed.")
elif choice=='**':
    print(f"Result : {num1}**{num2}={num1**num2}")
else:
    print("Invalid choice! Please enter valid operator.")