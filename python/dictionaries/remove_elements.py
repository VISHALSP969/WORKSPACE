student={
    "name":"Alice",
    "age":21,
    "branch":"Electrical",
    "city":"New York",
    "grade":"A"
}
print(student)

# remove the specified item
print(student.pop("age"))
print(student)

# remove last item
print(student.popitem())
print(student)

# delete the specified item
del student["branch"]
print(student)

# remove all elements
student.clear()
print(student)