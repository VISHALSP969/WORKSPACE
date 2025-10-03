# math_utils.py
# Simple Math Utility Functions Library
# Uses only basic Python features: functions, loops, recursion, conditionals, *args

def add(*args):
    """Return the sum of all arguments. If no args, returns 0."""
    total = 0
    for x in args:
        total += x
    return total

def subtract(a, b):
    """Return a - b."""
    return a - b

def multiply(*args):
    """Return the product of all arguments. If no args, returns 1."""
    if len(args) == 0:
        return 1
    prod = 1
    for x in args:
        prod *= x
    return prod

def divide(a, b):
    """Return a / b. Caller should ensure b != 0."""
    return a / b

def power(a, b=2):
    """Return a ** b. Default b=2 (square)."""
    return a ** b

def factorial(n):
    """Return n! using recursion. Assumes n >= 0 and integer."""
    if n < 0:
        return None  # Not defined for negative integers in our simple library
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Return True if n is prime (n >= 2). Uses trial division up to sqrt(n)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    # check odd divisors up to sqrt(n)
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def gcd(a, b):
    """Compute greatest common divisor using Euclid's algorithm (iterative)."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least common multiple using gcd. If either is 0, returns 0."""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)

def fibonacci(n):
    """Return the n-th Fibonacci number (0-based). Uses iterative approach.
    fib(0)=0, fib(1)=1.
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def sum_digits(n):
    """Return the sum of decimal digits of integer n (handles negative)."""
    n = abs(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def prime_factors(n):
    """Return a list of prime factors of n (duplicates included).
    Example: prime_factors(12) -> [2, 2, 3]
    """
    n = abs(n)
    factors = []
    # factor out 2
    while n % 2 == 0 and n > 0:
        factors.append(2)
        n //= 2
    # odd factors
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2
    if n > 1:
        factors.append(n)
    return factors

# --- simple self-tests (run when module loaded directly) ---
if __name__ == "__main__":
    # quick asserts to self-check correctness
    assert add() == 0
    assert add(1,2,3) == 6
    assert multiply() == 1
    assert multiply(2,3,4) == 24
    assert subtract(5,2) == 3
    assert power(3) == 9 and power(2,3) == 8
    assert factorial(5) == 120
    assert is_prime(2) and is_prime(13) and not is_prime(15)
    assert gcd(12, 18) == 6
    assert lcm(4,6) == 12
    assert fibonacci(0) == 0 and fibonacci(7) == 13
    assert sum_digits(12345) == 15
    assert prime_factors(84) == [2,2,3,7]

    # small interactive demo
    print("Math Utils Demo — sample outputs")
    print("add(1,2,3) =", add(1,2,3))
    print("multiply(2,3,4) =", multiply(2,3,4))
    print("subtract(10,3) =", subtract(10,3))
    print("divide(10,2) =", divide(10,2))
    print("power(3,3) =", power(3,3))
    print("factorial(6) =", factorial(6))
    print("is_prime(29) =", is_prime(29))
    print("gcd(48,18) =", gcd(48,18))
    print("lcm(12,15) =", lcm(12,15))
    print("fibonacci(10) =", fibonacci(10))
    print("sum_digits(98765) =", sum_digits(98765))
    print("prime_factors(360) =", prime_factors(360))

    # small menu to try functions manually (text menu)
    while True:
        print("\nMini CLI: choose an option")
        print("1) add numbers")
        print("2) multiply numbers")
        print("3) factorial")
        print("4) is_prime")
        print("5) gcd")
        print("6) lcm")
        print("7) fibonacci")
        print("8) prime factors")
        print("9) exit")
        choice = input("Enter choice (1-9): ").strip()
        if choice == "1":
            nums = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Sum =", add(*nums))
        elif choice == "2":
            nums = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Product =", multiply(*nums))
        elif choice == "3":
            n = int(input("Enter non-negative integer: "))
            print("Factorial =", factorial(n))
        elif choice == "4":
            n = int(input("Enter integer: "))
            print("Prime?" , is_prime(n))
        elif choice == "5":
            a = int(input("Enter a: ")); b = int(input("Enter b: "))
            print("GCD =", gcd(a,b))
        elif choice == "6":
            a = int(input("Enter a: ")); b = int(input("Enter b: "))
            print("LCM =", lcm(a,b))
        elif choice == "7":
            n = int(input("Enter n (0-based): "))
            print(f"Fibonacci({n}) =", fibonacci(n))
        elif choice == "8":
            n = int(input("Enter integer: "))
            print("Prime factors:", prime_factors(n))
        elif choice == "9":
            print("Goodbye")
            break
        else:
            print("Invalid choice.")
