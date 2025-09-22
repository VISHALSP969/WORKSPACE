# Numeric types
# integers
a=123
print(a)
print(type(a))
print(a.bit_length())   # bits needed to represent a
# floating point
f=3.14
print(f)
print(type(f))
print(f.is_integer())
# complex
z=2+3j
print(z)
print(type(z))
print(z.real)
print(z.imag)

# boolean
print(isinstance(True,int))
x=False
print(type(x))
print(x)

#Strings
s="hello world"
print(type(s))
print(s)
print(s[0])
print(s.upper())
print(s.split())

# Binary sequence
# Bytes
b=b'abc'
print(type(b))
print(b)
# Bytearray
ba=bytearray(b'abc')
print(type(ba))
print(ba)
ba[0]=120
print(ba)

# Sequence containers
# list
lst=[1,2,3]
print(type(lst))
print(lst)
lst.append(4)
print(lst)
print(lst[0])
# tuple
t=(1,2,3)
print(type(t))
print(t)
x,y,z=t     # unpacking
print(x,y,z)
# range
r=(range(1,10,2))
print(type(r))
print(r)
for i in range(1,10,2):
    print(i)

# mapping
# dictionary
d={"name":"John","age":22}
print(type(d))
print(d)
print(d["name"])
d["city"]="Delhi"
print(d)
print(d.get("city"))

# set types
# set
s={1,2,3,3,4}
print(type(s))
print(s)
s.add(5)
print(s)
# frozen set
fs=frozenset({1,2,3})
print(type(fs))
print(fs)

#NoneType
#None
x=None
print(type(x))
print(x)