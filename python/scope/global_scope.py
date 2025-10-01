x=100   # global variable

def show():
    print("Inside function:",x)

def change_global():
    global x    # tell python to use global x
    x=20

show()
print("Outside function:",x)

change_global()
print("Outside function:",x)