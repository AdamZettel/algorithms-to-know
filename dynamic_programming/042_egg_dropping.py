def egg_dropping(k, n):
    """Dynamic Programming approach to solve the Egg Dropping Problem."""
    # Create a table to store results of subproblems
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # If we have only one egg, we need n attempts for n floors
    for i in range(1, n + 1):
        dp[1][i] = i
    
    # If we have zero floors, we need zero attempts
    # If we have one floor, we need one attempt
    for i in range(1, k + 1):
        dp[i][0] = 0
        dp[i][1] = 1
    
    # Fill the dp table for all eggs and floors
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = float('inf')
            for x in range(1, j + 1):
                worst_case = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(dp[i][j], worst_case)
    
    return dp[k][n]

# Example usage:
k = 2  # Number of eggs
n = 10 # Number of floors
print(f"Minimum number of attempts needed: {egg_dropping(k, n)}")  # Output: 4
