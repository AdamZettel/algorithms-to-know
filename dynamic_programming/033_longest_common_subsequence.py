def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D array to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp array from bottom up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # dp[m][n] contains the length of LCS for X[0..m-1] & Y[0..n-1]
    return dp[m][n]

# Example usage:
X = "ABCBDAB"
Y = "BDCAB"
print(lcs(X, Y))  # Output: 4 (The LCS is "BCAB" or "BDAB")
