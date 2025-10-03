with open("sentences.txt","w") as f:
    f.write("Python is a powerful programming language.\n")
    f.write("It is easy to learn and use.\n")
    f.write("Python is used in web development, data science, and AI.\n")
    f.write("Many developers love Python for its simplicity.\n")
    f.write("File handling is an important concept in Python.\n")

with open("sentences.txt","r") as f:
    content=f.read()

words=content.split()
word_count=len(words)

print("File content:\n",content)
print("\nTotal numer of words:",word_count)