def outer():
    x="outer variable"
    def inner():
        nonlocal x  # refers to x in outer()
        x="modified by inner"
        print("Inside inner :",x)
    
    inner()
    print("Inside outer :",x)

outer()