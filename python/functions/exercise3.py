def make_id(name,prefix="USER"):
    print(f"{prefix}_{name}")

make_id("Alice")
make_id("Alice","Mrs")
make_id("Bob",prefix="Mr")