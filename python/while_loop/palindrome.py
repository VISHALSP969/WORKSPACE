# Check given number is palindrome or not
num=int(input("Enter a number : "))
rev=0
n=num

while n:
    rev=rev*10+n%10
    n//=10

if rev==num:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")