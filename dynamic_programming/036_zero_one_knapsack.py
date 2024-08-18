def knapsack_dp(weights, values, capacity):
    """Dynamic Programming approach with O(n * W) complexity."""
    n = len(weights)
    
    # Initialize dp table where dp[i][w] is the maximum value for first i items and capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the dp array from bottom up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # The bottom-right corner of the dp table contains the maximum value
    return dp[n][capacity]

def knapsack_optimized(weights, values, capacity):
    """Optimized approach with O(W) complexity using a 1D dp array."""
    n = len(weights)
    
    # Initialize a 1D dp array with 0s
    dp = [0] * (capacity + 1)
    
    # Build the dp array from bottom up
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    # The last element of dp contains the maximum value
    return dp[capacity]

# Example usage:
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

# Calculate maximum value using Dynamic Programming approach
max_value_dp = knapsack_dp(weights, values, capacity)
print(f"Maximum value using DP approach: {max_value_dp}")  # Output: 9

# Calculate maximum value using Optimized approach
max_value_optimized = knapsack_optimized(weights, values, capacity)
print(f"Maximum value using Optimized approach: {max_value_optimized}")  # Output: 9
