x=1
def f():
    x=2
    def g():
        nonlocal x
        x=3
    g()
    print("f:",x)
f()
print("global x :",x)