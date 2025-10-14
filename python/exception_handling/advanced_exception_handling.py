try:
    num1=int(input("Enter numerator : "))
    num2=int(input("Enter denominator : "))
    result=num1/num2
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
else:
    print(f"The result is {result}")