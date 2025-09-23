name="John"
age=22
print("Hello {},you are {} years old.".format(name,age))
print("Hello {},you are {:d} years old.".format(name,age))
print("Hello {},you are {:f} years old.".format(name,age))

print("Hello {}, you are {:d} years old".format("Thomas", 25))
print("Hello {name}, you are {age:d}".format(name="Thomas", age=25))

print("{0} {1} {0} {1} {2}".format("A","B","C"))

print("{:>10.2f}".format(3.14159))   # right-aligned, width 10, 2 decimals
