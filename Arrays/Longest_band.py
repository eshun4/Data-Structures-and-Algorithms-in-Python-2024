"""
Longest Band

Guven an array containg N integers, find the length of the longest band.

A band is defined as a subsequence which can be reordered in a such a manner that all
elements appear consecutive (i.e. with absolute fidderence of 1 between neighboring elements)

A longest band is the band (subsequence) which contains maximum
integers.

Example:
# Input: [1, 9, 3, 0, 18, 5, 2, 4, 10, 7, 12, 6]
# Output: 8

Explanation:
# The longest band is [0, 1, 2, 3, 4, 5, 6, 7] or [1, 2, 3, 4, 5, 6, 7, 8] or [9, 10, 11, 12]
# The length of the longest band is 8.
"""

def longest_band(numbers):
    """
    Given an array containing N integers, find the length of the longest band.
    
    A band is defined as a subsequence which can be reordered in such a manner that all
    elements appear consecutively (i.e. with absolute difference of 1 between neighboring elements).
    
    A longest band is the band (subsequence) which contains maximum integers.
    
    Parameters:
    numbers (list): List of integers.
    
    Returns:
    int: Length of the longest band.
    """
    # Create a set for quick lookup
    unordered_set = set(numbers)
    
    # Variable to store the largest band length
    largest_length = 0
    
    # Iterate over all elements in the set
    for element in unordered_set:
        # Check if the current element is the start of a band
        if element - 1 not in unordered_set:
            # Start counting the length of the band
            next_no = element
            count = 0
            
            # Count consecutive numbers in the band
            while next_no in unordered_set:
                count += 1
                next_no += 1
            
            # Update the largest length if the current band is longer
            largest_length = max(largest_length, count)
    
    return largest_length


def main():
    # Example usage of the function
    numbers = [1, 9, 3, 0, 18, 5, 2, 4, 10, 7, 12, 6]
    result = longest_band(numbers)
    print(result)  # Output: 8

if __name__ == "__main__":
    main()
