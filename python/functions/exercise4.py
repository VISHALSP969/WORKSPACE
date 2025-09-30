def student_info(**kwargs):
    print(f"name : {kwargs["name"]}")
    print(f"age : {kwargs["age"]}")
    print(f"grade : {kwargs["grade"]}")

student_info(name="Alice",age=21,grade="A")