try:
    f=open("data.txt","r")
    content=f.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed - closing the file(if open).")