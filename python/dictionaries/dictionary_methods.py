d={"a":1,"b":2}
keys=d.keys()
print(keys)

d["c"]=3
keys=d.keys()
print(keys)

values=d.values()
print(values)

print(d.items())

for k,v in d.items():
    print(k,v)

d={"a":1}
print(d)
print(d.get("a"))
print(d.get("z"))
print(d.get("z",0))

d={"a":1,"b":2}
print(d)
d.update({"b":20,"c":3})
print(d)
d.update({"d":4,"e":5})
print(d)
d.update([("f",6),("g",7)])
print(d)

# print(d.pop("p"))     # key error
print(d.pop("p",0))
print(d)
print(d.pop("g"))
print(d)

print(d.popitem())
print(d.popitem())
print(d)

d={}
d.setdefault("a",[]).append(1)
print(d)

d={"a":1,"b":2}
d1=d.copy()
print(d)
print(d1)

d.clear()
print(d)