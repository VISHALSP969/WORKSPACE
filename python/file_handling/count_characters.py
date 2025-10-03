with open("story.txt", "w") as f:
    f.write("Python is powerful.\n")
    f.write("It is easy to learn.\n")
    f.write("We are learning file handling.\n")

with open("story.txt","r") as f:
    content=f.read()
    char_count=len(content)

print("Total characters in file:",char_count)