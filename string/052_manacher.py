def manacher(s):
    """Manacher's algorithm to find the longest palindromic substring in linear time."""
    # Transform the string to handle even length palindromes.
    transformed = '#'.join(f"^{s}$")
    n = len(transformed)
    P = [0] * n
    C = R = 0  # Center and Right boundary of the current rightmost palindrome

    for i in range(1, n - 1):
        mirr = 2 * C - i  # Mirror of i with respect to center C
        if i < R:
            P[i] = min(R - i, P[mirr])  # Use the mirrored palindrome's value

        # Expand the palindrome centered at i
        while transformed[i + (1 + P[i])] == transformed[i - (1 + P[i])]:
            P[i] += 1

        # Update the center and right boundary if expanded beyond R
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum value in P
    max_len, center_index = max((n, i) for i, n in enumerate(P))
    start = (center_index - max_len) // 2  # Compute the start index of the longest palindrome
    return s[start:start + max_len]

# Example usage:
text = "babad"
longest_palindrome = manacher(text)
print(f"Longest palindromic substring is: '{longest_palindrome}'")
