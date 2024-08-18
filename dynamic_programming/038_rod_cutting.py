def rod_cutting(prices):
    """Dynamic Programming approach to solve the Rod Cutting problem."""
    n = len(prices)
    
    # Initialize dp array where dp[i] is the maximum revenue for rod of length i
    dp = [0] * (n + 1)
    
    # Compute maximum revenue for each length from 1 to n
    for i in range(1, n + 1):
        max_val = -float('inf')
        for j in range(1, i + 1):
            max_val = max(max_val, prices[j - 1] + dp[i - j])
        dp[i] = max_val
    
    return dp[n]

# Example usage:
prices = [2, 5, 9, 10, 15, 17, 17, 20]
print(f"Maximum revenue: {rod_cutting(prices)}")  # Output: 22
