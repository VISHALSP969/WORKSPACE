with open("notes.txt","w") as f:
    f.write("Python is fun.\n")
    f.write("File handling is important.\n")
    f.write("We are counting lines!\n")

with open("notes.txt","r") as f:
    lines=f.readlines()
    count=len(lines)

print("File has",count,"lines.")