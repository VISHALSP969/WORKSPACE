pi=3.14159265
print(f"{pi}")          # 3.1459265
print(f"{pi:.2f}")      # 3.14
print(f"{12345:,}")     # 12,345

n=7
print(f"{n}")           # 7
print(f"{n:.3f}")       # 7.000
print(f"{n:5.2f}")      #  7.00
print(f"{n:>3} x {8:>2} = {n*8:>3}")    # aligned multiplication snippet
print(f"{255:#x} = {255:#X}")           # # includes 0x prefix if used in format with #

# conversion example
obj="a\nb"
print(f"{obj!r}")