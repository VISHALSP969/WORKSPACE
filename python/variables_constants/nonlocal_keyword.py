def outer():
    n=1
    print(n)
    def inner():
        nonlocal n
        n=2
    inner()
    print(n)

outer()