import math
from collections import Counter

def shannon_entropy(password: str) -> float:
    """
    Calculate the Shannon entropy of a given password.
    
    Args:
        password (str): The password string to evaluate.
    
    Returns:
        float: Shannon entropy value in bits.
    """
    if not password:
        return 0.0
    
    # Count frequency of each character
    char_counts = Counter(password)
    length = len(password)
    
    # Shannon entropy formula: H = -Σ p(x) * log2(p(x))
    entropy = 0.0
    for count in char_counts.values():
        p_x = count / length
        entropy -= p_x * math.log2(p_x) #log2(p_x) is negative so we are technically adding the entropy values
    
    # Multiply by length to get total entropy in bits
    return round(entropy * length,2)


