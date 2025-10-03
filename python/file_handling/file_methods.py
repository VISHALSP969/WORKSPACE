with open("sample.txt","w") as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: Python\n")
    f.write("Line 3: File Handling\n")

with open("sample.txt","r") as f:
    print("Full content with read():")
    print(f.read())    # Reads entire file

with open("sample.txt","r") as f:
    print("\nReading line by line with readline():")
    print(f.readline())     # first line 
    print(f.tell())
    print(f.readline())     # Second line
    print(f.tell())
    print(f.readline())     # Third line
    print(f.tell())

with open("sample.txt","r") as f:
    print("\nReading all lines with readlines():")
    print(f.readlines())
    # print(f.seek(0))