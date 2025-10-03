m1,m2,m3=input("Enter 3 favorite movies:").split()

with open("data1.txt","w") as file:
    file.write("Favorite Movies\n")
    file.write(m1+"\n")
    file.write(m2+"\n")
    file.write(m3+"\n")

with open("data1.txt","r") as file:
    content=file.read()

print(content)