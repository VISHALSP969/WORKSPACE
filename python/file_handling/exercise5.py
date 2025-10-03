with open("notes.txt","w") as file:
    file.write("Day 1: learned Python basics.\n")

with open("notes.txt","a") as file:
    file.write("Day 2: Learned file handling in Python.\n")
    file.write("Day 3: Practiced appending with context manageer.\n")

with open("notes.txt","r") as file:
    content=file.read()

print("My Notes:\n",content)