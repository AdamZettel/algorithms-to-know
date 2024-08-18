def compute_z_array(s):
    """Compute the Z-array for the string s."""
    n = len(s)
    Z = [0] * n
    L, R, K = 0, 0, 0

    for i in range(1, n):
        if i > R:
            L, R = i, i
            while R < n and s[R] == s[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            K = i - L
            if Z[K] < R - i + 1:
                Z[i] = Z[K]
            else:
                L = i
                while R < n and s[R] == s[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z

def z_algorithm_search(text, pattern):
    """Search for the pattern in the text using the Z algorithm."""
    combined = pattern + "$" + text
    Z = compute_z_array(combined)
    pattern_length = len(pattern)
    matches = []
    
    for i in range(len(pattern) + 1, len(combined)):
        if Z[i] == pattern_length:
            matches.append(i - len(pattern) - 1)
    
    return matches

# Example usage:
text = "ababcababcabc"
pattern = "abc"
matches = z_algorithm_search(text, pattern)

# Display matches
for match in matches:
    print(f"Pattern '{pattern}' found at index {match}")
