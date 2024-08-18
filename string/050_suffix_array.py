def build_suffix_array(s):
    """Build the suffix array for the string s."""
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def build_lcp_array(s, suffix_array):
    """Build the LCP array for the string s using the suffix array."""
    n = len(s)
    rank = [0] * n
    lcp = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

# Example usage:
s = "banana"
suffix_array = build_suffix_array(s)
lcp_array = build_lcp_array(s, suffix_array)

print("Suffix Array:", suffix_array)  # Example output: [5, 3, 1, 0, 4, 2]
print("LCP Array:", lcp_array)  # Example output: [1, 3, 0, 0, 2, 1]
