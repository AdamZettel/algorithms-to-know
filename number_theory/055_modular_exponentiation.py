def modular_exponentiation(base, exponent, modulus):
    """Compute (base^exponent) % modulus using modular exponentiation."""
    result = 1
    base = base % modulus  # In case base is larger than modulus

    while exponent > 0:
        # If exponent is odd, multiply the current base with result
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        
        # Exponent must be even now
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % modulus  # Square the base

    return result

# Example usage:
base = 3
exponent = 200
modulus = 13
result = modular_exponentiation(base, exponent, modulus)
print(f"({base}^{exponent}) % {modulus} = {result}")
