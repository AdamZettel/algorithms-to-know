def bad_character_rule(pattern):
    """Preprocess the pattern to create the bad character table."""
    m = len(pattern)
    bad_char = {chr(i): -1 for i in range(256)}  # Initialize for all ASCII characters

    for i in range(m):
        bad_char[pattern[i]] = i
    
    return bad_char

def boyer_moore_search(text, pattern):
    """Perform Boyer-Moore search for the pattern in the text using the bad character rule."""
    n = len(text)
    m = len(pattern)
    
    bad_char = bad_character_rule(pattern)
    
    s = 0  # Shift of the pattern
    while s <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            print(f"Pattern found at index {s}")
            s += (m - bad_char[text[s + m]] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[text[s + j]])
            
# Example usage:
text = "ABAAABCD"
pattern = "ABCD"
boyer_moore_search(text, pattern)  # Output: Pattern found at index 4
