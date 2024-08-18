import math
import random

def pollard_rho(n, max_iter=10000):
    """Pollard's Rho Algorithm for integer factorization."""
    def f(x, c, n):
        return (x * x + c) % n
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    if n % 2 == 0:
        return 2
    
    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1
    
    for _ in range(max_iter):
        x = f(x, c, n)
        y = f(f(y, c, n), c, n)
        d = gcd(abs(x - y), n)
        
        if d > 1 and d < n:
            return d
    
    return None  # No factor found

# Example usage:
n = 143  # Example composite number
factor = pollard_rho(n)
print(f"A non-trivial factor of {n} is: {factor}")
