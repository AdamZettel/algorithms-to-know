import random

def is_prime(n, k=5):
    """Miller-Rabin Primality Test to check if n is a prime number with k iterations."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Perform k iterations of the test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

# Example usage:
n = 37
print(f"{n} is prime: {is_prime(n)}")

n = 100
print(f"{n} is prime: {is_prime(n)}")
