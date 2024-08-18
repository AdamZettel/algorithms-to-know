def rabin_karp_search(text, pattern):
    """Perform Rabin-Karp search for the pattern in the text."""
    # Parameters
    d = 256  # Number of characters in the input alphabet (assuming ASCII)
    q = 101  # A prime number for hashing

    # Lengths of pattern and text
    m = len(pattern)
    n = len(text)

    # Calculate the hash value of the pattern and the first window of text
    p_hash = 0
    t_hash = 0
    h = 1

    # Calculate the value of h = d^(m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value of the pattern and the first window of text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Search for the pattern
    for i in range(n - m + 1):
        # Check if the hash values match
        if p_hash == t_hash:
            # If hash values match, check for actual substring match
            if text[i:i + m] == pattern:
                print(f"Pattern found at index {i}")

        # Calculate hash value for the next window
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            # We might get negative value of t_hash, converting it to positive
            if t_hash < 0:
                t_hash += q

# Example usage:
text = "ABCCBAABCCBA"
pattern = "ABCC"
rabin_karp_search(text, pattern)  # Output: Pattern found at index 0, Pattern found at index 8
