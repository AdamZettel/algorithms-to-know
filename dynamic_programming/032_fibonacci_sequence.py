def fibonacci(n, optimized=True):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    if optimized:
        # Space-Optimized Approach
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    else:
        # Full List Approach
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

# Example usage:
print(fibonacci(10))  # Output: 55 (optimized by default)
print(fibonacci(10, optimized=False))  # Output: 55 (using full list)
