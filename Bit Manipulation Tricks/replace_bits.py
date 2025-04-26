"""
Replace Bits.

Problem:

You are given two 32-bit numbers, N and M, and two positions i and j.
Write a method to set all bits between i and j in N equal to M.
M (becomes a substring of N located at i and j).

Example:
N = 10000000000 (1024)
M = 10101 (21)
i = 2
j = 6
Output: N = 10001010100 (1084)
"""


def clear_bits_in_range(n, i, j):
    """Clear bits from i to j in a number."""
    a = (~0) << (j + 1) # Clear bits from j+1 to 31
    b = (1 << i) - 1 # Clear bits from 0 to i-1
    mask = a | b # Combine the two masks
    return n & mask # Clear bits from i to j

def replace_bits(n, m, i, j):
    """
    Replace bits in n with bits from m from index i to j.
    
    Parameters:
    n (int): The number in which bits will be replaced.
    m (int): The number whose bits will be used for replacement.
    i (int): The starting index for replacement.
    j (int): The ending index for replacement.

    Returns:
    int: The modified number after replacing bits.
    """
    # Clear bits from range of j to i
    clear_bits_in_range(n, i, j)
    mask = (m << i)
    n |= mask
    return n

def main():
    # Example usage of the function
    n = 1024  # 10000000000
    m = 21    # 00000000010101
    i = 2
    j = 6
    result = replace_bits(n, m, i, j)
    print(f"Modified N: {result}")  # Output: 1108 (10001010100)



if __name__ == "__main__":
    main()
