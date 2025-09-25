# Reverse a given number
num=int(input("Enter a number : "))
rev=0
n=num

while n:
    rev=rev*10+n%10
    n//=10

print(f"Reverse of {num} is {rev}")