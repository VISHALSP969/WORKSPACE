# check perfect square
n=int(input("Enter a number : "))
for i in range(1,n+1):
    if i*i==n:
        print(f"{n} is a Perfect Square({i}x{i})")
        break
else:
    print(f"{n} is not a Perfect Square")