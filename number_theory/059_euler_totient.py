def euler_totient(n):
    """Compute Euler's Totient Function φ(n)."""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            # p is a divisor of n, apply the formula
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    # If n is a prime number greater than 1
    if n > 1:
        result -= result // n
    return result

# Example usage:
n = 30
print(f"φ({n}) = {euler_totient(n)}")
