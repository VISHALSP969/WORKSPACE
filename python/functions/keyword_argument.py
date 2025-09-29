def introduce(name,age,city):
    print(f"My name is {name}, I am {age} years old, from {city}.")

# positional argument
introduce("Bob",25,"Delhi")

# keyword arguments (order does not matter)
introduce(age=20,city='Mumbai',name="Alice")