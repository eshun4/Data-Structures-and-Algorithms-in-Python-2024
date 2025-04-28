"""
Mountain

Write a function that takes input as an array of distict integers,
and returns the length of the highest mountain.

-- A mountain is defined as adjacent integers that are strictly increasing 
until they reach a peak, at which the become strictly decreasing.

-- At least 3 numbers are required to form a mountain.

Example:

Input: [5, 6, 1, 2, 3, 4, 5, 4, 3, 2, 0, 1, 2, 3, -2, 4] 
Output: 9

"""
def mountain(numbers):
    """
    Given an array of distinct integers, return the length of the highest mountain.
    
    A mountain is defined as adjacent integers that are strictly increasing until they reach a peak,
    at which they become strictly decreasing. At least 3 numbers are required to form a mountain.
    
    Parameters:
    numbers (list): List of distinct integers.
    
    Returns:
    int: Length of the highest mountain.
    """
    # get the length of the numbers array
    n = len(numbers)
    largest = 0
    # iterate through the numbers array
    for i in range(1, n - 1):
        # Check if numbers[i] is a peak
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            # Do some work here
            count = 1
            j = i
            # count backwards (left) from the peak
            while j >= 1 and numbers[j] > numbers[j - 1]:
                j -= 1
                count += 1
            # Count forward (right) from the peak
            while i < n - 1 and numbers[i] > numbers[i + 1]:
                i += 1
                count += 1
            # Update the largest mountain length if the current count is greater
            largest = max(largest, count)
        else:
            i += 1
    # Return the length of the largest mountain found
    return largest 
            
            
            
    

def main():
    numbers = [5, 6, 1, 2, 3, 4, 5, 4, 3, 2, 0, 1, 2, 3, -2, 4] 
    result = mountain(numbers)
    print(result)
    

if __name__ == "__main__":
    main()