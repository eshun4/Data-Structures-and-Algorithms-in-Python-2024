"""
Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.
"""





def power_of_two(n):
    """
    Check if a number is a power of two.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is a power of two, False otherwise.
    """
    # A number is a power of two if it is greater than 0 and the bitwise AND of the number and its predecessor is 0.
    
    return n > 0 and (n & (n - 1)) == 0


def main():
    # Example usage of the function
    print(power_of_two(1))  # Output: True (2^0)
    print(power_of_two(2))  # Output: True (2^1)
    print(power_of_two(3))  # Output: False
    print(power_of_two(4))  # Output: True (2^2)
    print(power_of_two(5))  # Output: False
    print(power_of_two(8))  # Output: True (2^3)
    print(power_of_two(16))  # Output: True (2^4)
    print(power_of_two(18))  # Output: False
    
    
if __name__ == "__main__":
    main()

    