vals = [False, True]

print("A     B     A and B  A or B  not A  A ^ B")
for A in vals:
    for B in vals:
        print(f"{A!s:5} {B!s:5} { (A and B)!s:8} { (A or B)!s:7} { (not A)!s:6} { (A ^ B)!s }")
