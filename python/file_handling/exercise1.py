# Writing to a file
with open("data1.txt","w") as file:
    file.write("Name : John\n")
    file.write("Age : 23\n")
    file.write("City : Mumbai")

print("Data written successfully!")

# Reading from the file
with open("data1.txt","r") as file:
    content=file.read()

print("\nFile Content : ")
print(content)
