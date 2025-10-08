try:
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2:"))
    print("Division:",num1/num2)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter only numbers!")