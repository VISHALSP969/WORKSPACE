x=int(input("Enter a number : "))
message="Positive" if x>=0 else "Negative"
print(message)

age=int(input("Enter your age : "))
message="Eligible to vote" if age>=18 else "Not eligible to vote"
print(message)

num=int(input("Enter a number : "))
print("Even" if num%2==0 else "Odd")