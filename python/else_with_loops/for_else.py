for i in range(5):
    print(i)
else:
    print("Loop finished without break!")

for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("Loop finished without break!")