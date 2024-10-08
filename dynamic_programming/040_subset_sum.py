def subset_sum(arr, target):
    """Dynamic Programming approach to solve the Subset Sum Problem."""
    n = len(arr)
    
    # Initialize dp table
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # A sum of 0 can always be achieved with an empty subset
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][target]

# Example usage:
arr = [3, 34, 4, 12, 5, 2]
target = 9
print(f"Is there a subset with sum {target}? {subset_sum(arr, target)}")  # Output: True
