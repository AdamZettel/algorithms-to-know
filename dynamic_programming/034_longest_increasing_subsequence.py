import bisect

def lis_dp(arr):
    """Dynamic Programming approach with O(n^2) complexity."""
    n = len(arr)
    
    # Initialize dp array where dp[i] stores the length of LIS ending at index i
    dp = [1] * n
    
    # Compute the LIS for each element in arr
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The length of the longest increasing subsequence is the maximum value in dp
    return max(dp)

def lis_optimized(arr):
    """Optimized approach with O(n log n) complexity using binary search."""
    n = len(arr)
    
    # Initialize an empty list to keep track of the smallest possible tail
    lis_tails = []
    
    for num in arr:
        # Find the position where 'num' can replace the current element
        pos = bisect.bisect_left(lis_tails, num)
        
        # If 'num' is larger than any element in lis_tails, it extends the LIS
        if pos == len(lis_tails):
            lis_tails.append(num)
        else:
            lis_tails[pos] = num
    
    # The length of lis_tails is the length of the longest increasing subsequence
    return len(lis_tails)

# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

# Calculate LIS using Dynamic Programming approach
lis_length_dp = lis_dp(arr)
print(f"LIS length using DP approach: {lis_length_dp}")  # Output: 6

# Calculate LIS using Optimized approach
lis_length_optimized = lis_optimized(arr)
print(f"LIS length using Optimized approach: {lis_length_optimized}")  # Output: 6
