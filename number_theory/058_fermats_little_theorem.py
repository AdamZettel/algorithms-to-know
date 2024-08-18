def fermat_little_theorem(a, p):
    """Verify Fermat's Little Theorem: a^(p-1) % p == 1 for a prime p."""
    if p <= 1 or not is_prime(p):
        raise ValueError("p must be a prime number.")
    
    return pow(a, p - 1, p) == 1

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
a = 2
p = 7
result = fermat_little_theorem(a, p)
print(f"{a}^{p-1} % {p} == 1: {result}")
