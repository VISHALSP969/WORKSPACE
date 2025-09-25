marks=int(input("Enter marks : "))
if marks>=50:
    if marks>=90:
        print("Grade A")
    elif marks>=75:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("Grade F")