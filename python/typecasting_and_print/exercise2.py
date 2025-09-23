print(int("-42"))
print(int(float("7.9")))
print(1,2,3,sep="|")

def pretty_money(n):
    return f"${n}"

print(pretty_money(1234.56))

lst=["a","bb","ccc"]
print("{:<5} {:<5} {:<5}".format(*lst))

for i in range(1,11):
    print(f"{i:>3} {i:>8b} {i:>5o} {i:>6d} {i:>6x}")