def sieve_of_eratosthenes(n):
    """Return a list of all prime numbers up to n using the Sieve of Eratosthenes."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, n + 1, start):
                is_prime[multiple] = False

    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

# Example usage:
n = 30
primes = sieve_of_eratosthenes(n)
print(f"Prime numbers up to {n} are: {primes}")
