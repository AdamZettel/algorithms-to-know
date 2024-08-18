def euclidean_algorithm(a, b):
    """Compute the GCD of two integers a and b using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

# Example usage:
a = 48
b = 18
gcd = euclidean_algorithm(a, b)
print(f"The GCD of {a} and {b} is {gcd}")
