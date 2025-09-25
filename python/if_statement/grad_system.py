def grde_from_score(score):
    if score<0 or score>100:
        return None     # Invalid
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
    
# main
try:
    s=float(input("Enter score (0-100):"))
except ValueError:
    print("Invalid input: not a number.")
else:
    letter=grde_from_score(s)
    if letter is None:
        print("Score must be between 0 and 100.")
    else:print(f"Score: {s} ---> Grade: {letter}")