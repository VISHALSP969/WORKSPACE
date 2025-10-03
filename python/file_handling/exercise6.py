with open("myfile.txt", "w") as f:
    f.write("I love Python programming.\n")
    f.write("Python is very powerful.\n")
    f.write("This line does not have the keyword.\n")
    f.write("Learning Python step by step.\n")

count=0
with open("myfile.txt","r") as f:
    for line in f:
        if "Python" in line:
            count+=1

print("Number of lines containing 'Pthon':",count)