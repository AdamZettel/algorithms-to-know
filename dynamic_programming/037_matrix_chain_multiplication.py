import sys

def matrix_chain_order(p):
    """Dynamic Programming approach to solve the Matrix Chain Multiplication problem."""
    n = len(p) - 1  # Since p has length n+1
    
    # dp[i][j] will store the minimum number of multiplications needed to compute the matrix A_i to A_j
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # s[i][j] will store the index k at which the optimal split occurs
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # l is the chain length.
    for l in range(2, n + 1):  # l=2 means we are considering chains of length 2
        for i in range(1, n - l + 2):
            j = i + l - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                # q is the cost/scalar multiplications
                q = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < dp[i][j]:
                    dp[i][j] = q
                    s[i][j] = k
    
    return dp, s

def print_optimal_parens(s, i, j):
    """Utility function to print the optimal parenthesization."""
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage:
p = [30, 35, 15, 5, 10, 20, 25]  # Dimensions of matrices
dp, s = matrix_chain_order(p)

# The minimum number of multiplications is stored in dp[1][n]
print(f"Minimum number of multiplications is {dp[1][len(p)-1]}")  # Output: 15125

# Printing the optimal parenthesization
print("Optimal parenthesization is: ", end="")
print_optimal_parens(s, 1, len(p) - 1)  # Output: ((A1(A2A3))((A4A5)A6))
