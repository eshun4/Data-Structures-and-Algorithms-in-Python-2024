"""
Bit Manipulation Tricks
This module contains various bit manipulation tricks and techniques that can be used to solve problems efficiently.

These tricks are particularly useful in competitive programming and algorithm design, where performance is critical.
The tricks include:
1. Checking if a number is even or odd using bitwise AND.
2. Swapping two numbers without using a temporary variable.
3. Counting the number of set bits (1s) in a number using Brian Kernighan's algorithm.
4. Finding the position of the rightmost set bit in a number.
5. Reversing the bits of a number.
6. Checking if a number is a power of two using bitwise AND.
7. Finding the maximum of two numbers using bitwise operations.
8. Finding the minimum of two numbers using bitwise operations. 
9. Clearing the rightmost set bit of a number.
10. Setting the rightmost unset bit of a number.
11. Toggling the rightmost set bit of a number.
12. Checking if two numbers have opposite signs using bitwise XOR.
13. Finding the absolute value of a number using bitwise operations.
14. Rotating bits of a number to the left or right.
15. Converting a number to its binary representation and vice versa.
16. Finding the two's complement of a number.
17. Performing bitwise operations on arrays or lists of numbers.
18. Using bit masks to represent subsets of a set.
19. Using bitwise operations to solve problems related to subsets, permutations, and combinations.
20. Using bit manipulation to optimize mathematical operations, such as multiplication and division by powers of two.
21. Using bit manipulation to solve problems related to prime numbers, such as checking for primality or generating prime numbers.
22. Using bit manipulation to solve problems related to combinatorial mathematics, such as counting combinations or permutations.
23. Using bit manipulation to solve problems related to graph theory, such as finding the shortest path or detecting cycles.
24. Using bit manipulation to solve problems related to number theory, such as finding the greatest common divisor (GCD) or least common multiple (LCM).
"""


def odd_even(n):
    """Check if a number is even or odd using bitwise AND."""
    return n & 1 == 0

def get_ith_bit(n, i):
    """Get the ith bit of a number."""
    mask = (1 << i)
    return 1 if (n & mask) > 0 else 0

def clear_ith_bit(n, i):
    """Clear the ith bit of a number."""
    mask = ~(1 << i)
    return n & mask

def set_ith_bit(n, i):
    """Set the ith bit of a number."""
    mask = (1 << i)
    return (n | mask)

def update_ith_bit(n, i, v):
    """Update the ith bit of a number to v (0 or 1)."""
    n = clear_ith_bit(n, i)
    mask = (v << i)
    n = n | mask
    return n

def clear_last_i_bits(n, i):
    """Clear the last i bits of a number."""
    mask = -1<< i
    return n & mask

def clear_bits_in_range(n, i, j):
    """Clear bits from i to j in a number."""
    a = (~0) << (j + 1) # Clear bits from j+1 to 31
    b = (1 << i) - 1 # Clear bits from 0 to i-1
    mask = a | b # Combine the two masks
    return n & mask # Clear bits from i to j

def main():
    # Example usage of the functions
    print("Is 5 even?", odd_even(5))  # Output: False
    print("Is 4 even?", odd_even(4))  # Output: True

    print("3rd bit of 5:", get_ith_bit(5, 3))  # Output: 0 (binary 101)
    print("2nd bit of 5:", get_ith_bit(5, 2))  # Output: 1 (binary 101)
    
    print("Clearing 2nd bit of 5:", clear_ith_bit(5, 2))  # Output: 1 (binary 101 -> 001)
    print("Clearing 0th bit of 5:", clear_ith_bit(5, 0))  # Output: 4 (binary 101 -> 100)
    
    print("Setting 2nd bit of 5:", set_ith_bit(5, 1))  # Output: 7 (binary 101 -> 111)
    print("Setting 0th bit of 5:", set_ith_bit(5, 0))  # Output: 5 (binary 101 -> 101)
    
    print("Updating 2nd bit of 5 to 0:", update_ith_bit(5, 2, 0))  # Output: 1 (binary 101 -> 001)
    print("Updating 2nd bit of 5 to 1:", update_ith_bit(5, 1, 1))  # Output: 7 (binary 101 -> 111)
    
    print("Clearing last 2 bits of 5:", clear_last_i_bits(5, 1))  # Output: 4 (binary 101 -> 100)
    print("Clearing last 1 bits of 5:", clear_last_i_bits(5, 1))  # Output: 4 (binary 101 -> 100)
    
    print("Clearing bits from 1 to 3 of 15:", clear_bits_in_range(15, 1, 3))  # Output: 1 (binary 1111 -> 0001)
    print("Clearing bits from 0 to 1 of 15:", clear_bits_in_range(15, 0, 1))  # Output: 12 (binary 1111 -> 1100)
    


if __name__ == "__main__":
    main()