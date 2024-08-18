def edit_distance(word1, word2):
    """Dynamic Programming approach to find the Edit Distance."""
    m, n = len(word1), len(word2)
    
    # Create a table to store results of subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from word1 to match empty word2
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters into empty word1 to match word2
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # Characters are the same, no additional cost
            else:
                dp[i][j] = min(dp[i-1][j] + 1,  # Deletion
                               dp[i][j-1] + 1,  # Insertion
                               dp[i-1][j-1] + 1)  # Substitution
    
    return dp[m][n]

# Example usage:
word1 = "intention"
word2 = "execution"
print(f"Edit distance between '{word1}' and '{word2}': {edit_distance(word1, word2)}")  # Output: 5
