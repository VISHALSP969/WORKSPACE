try:
    x=int(input("Enter a number : "))
    y=int(input("Enter another number : "))
    print(x/y)
except Exception as e:
    print("Error :",e)