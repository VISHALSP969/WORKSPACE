# print table of a number using f-string
n=int(input("Enter a number : "))
print(f"Multiplication table for {n}")
for i in range(1,11):
    print(f"{n:2} x {i:2} = {n*i:3}")