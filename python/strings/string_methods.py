s="hello world"
print(s.upper())
print(s.capitalize())
print(s.title())

s="PYthon"
print(s.lower())

s="     hello     "
print(s)
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s="----hello----"
print(s)
print(s.strip("-"))
s="----hello----eee"
print(s)
print(s.strip('e'))

s="I like Java"
print(s)
print(s.replace('Java','python'))

s="apple,banana,cherry"
print(s)
print(s.split(','))

words=["I","love","Python"]
print(words)
print("".join(words))
print(" ".join(words))
print("-".join(words))

s="hello world"
print(s)
print(s.find("world"))
print(s.find("hello"))
print(s.find("Hello"))

s="banana"
print(s)
print(s.count("a"))
print(s.count("q"))

s="hello.py"
print(s)
print(s.startswith("hello"))
print(s.endswith(".py"))
print(s.endswith(".java"))
