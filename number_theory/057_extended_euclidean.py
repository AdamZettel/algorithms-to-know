def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find the GCD and coefficients for Bézout's identity."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Example usage:
a = 56
b = 15
gcd, x, y = extended_gcd(a, b)
print(f"The GCD of {a} and {b} is {gcd}")
print(f"Coefficients x and y are: {x}, {y}")
print(f"Verification: {a} * {x} + {b} * {y} = {gcd}")
