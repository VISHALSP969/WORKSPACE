# print all the multiples of given number in between  and 100
n=int(input("Enter a number : "))
print(f"multiple of {n} between  and 100")
for i in range(1,100):
    if i%n==0:
        print(i,end=" ")
print()