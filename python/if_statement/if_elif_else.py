marks=int(input("Enter your mark : "))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Grade F")

num=int(input("Enter a number : "))
if num>0:
    print("Positive")
elif num==0:
    print("Zero")
else:
    print("Negative")

signal=input("Enter traffic light color (red/yellow/green):").lower()
if signal=="red":
    print("Stop!")
elif signal=="yellow":
    print("Get Ready!")
elif signal=="green":
    print("Go!")
else:
    print("Invalid signal color")