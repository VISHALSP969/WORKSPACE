def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print("Factorial of 5 :",factorial(5))
print("Facorial of 10 :",factorial(10))