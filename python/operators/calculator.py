# calculator.py
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
def floordiv(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a // b
def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b
def power(a, b): return a ** b

OPERATIONS = {
    "+": ("add", add),
    "-": ("subtract", sub),
    "*": ("multiply", mul),
    "/": ("divide", div),
    "//": ("floor divide", floordiv),
    "%": ("modulo", mod),
    "**": ("power", power)
}

def read_number(prompt):
    """Read a number (int or float) from user; supports 'q' to quit."""
    while True:
        s = input(prompt).strip()
        if s.lower() in ("q", "quit", "exit"):
            return None
        try:
            # try integer first (keeps integers when possible)
            if "." in s or "e" in s or "E" in s:
                return float(s)
            return int(s)
        except ValueError:
            print("Invalid number. Type a number or 'q' to quit.")

def calculator():
    print("Simple calculator. Type 'q' at any prompt to quit.")
    print("Supported operators:", ", ".join(OPERATIONS.keys()))
    while True:
        a = read_number("Enter first number: ")
        if a is None:
            print("Goodbye!")
            break
        op = input("Enter operator (+, -, *, /, //, %, **): ").strip()
        if op.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        if op not in OPERATIONS:
            print("Unknown operator. Try again.")
            continue
        b = read_number("Enter second number: ")
        if b is None:
            print("Goodbye!")
            break

        try:
            result = OPERATIONS[op][1](a, b)
            # Use f-string for neat output
            print(f"{a} {op} {b} = {result}")
        except ZeroDivisionError as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()
