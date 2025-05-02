"""
Trap Rain Water Problem.py

Given n non-negative integers representing an elevation
map where the width of each bar is 1, compute how much water
it can trap after raining.

Sample Input:
[0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

"""                


def rain_two_pointer(numbers):
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.
    
    Parameters:
    numbers (list): List of non-negative integers representing the elevation map.
    
    Returns:
    int: Total amount of water trapped after raining.
    """
    # Get the length of the array
    n = len(numbers)
    # If the array has 2 or fewer elements, no water can be trapped
    if n <= 2:
        return 0

    # Initialize two pointers: one starting from the left and the other from the right
    left, right = 0, n - 1
    # Variables to keep track of the maximum heights encountered so far from the left and right
    left_max, right_max = 0, 0
    # Variable to store the total amount of water trapped
    total = 0

    # Iterate until the two pointers meet
    while left < right:
        # If the height at the left pointer is less than the height at the right pointer
        if numbers[left] < numbers[right]:
            # If the current height at the left pointer is greater than or equal to left_max,
            # update left_max to the current height
            if numbers[left] >= left_max:
                left_max = numbers[left]
            else:
                # Otherwise, calculate the water trapped at the current position
                # as the difference between left_max and the current height
                total += left_max - numbers[left]
            # Move the left pointer one step to the right
            left += 1
        else:
            # If the current height at the right pointer is greater than or equal to right_max,
            # update right_max to the current height
            if numbers[right] >= right_max:
                right_max = numbers[right]
            else:
                # Otherwise, calculate the water trapped at the current position
                # as the difference between right_max and the current height
                total += right_max - numbers[right]
            # Move the right pointer one step to the left
            right -= 1

    # Return the total amount of water trapped
    return total

def rain(numbers):
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.
    
    Parameters:
    numbers (list): List of non-negative integers representing the elevation map.
    
    Returns:
    int: Total amount of water trapped after raining.
    """
    # get the length of the array
    n = len(numbers)
    # check if n is less than or equal to 2
    if n <= 2:
        return 0
    # build 2 array for the left and the right
    left, right = [0] * n, [0] * n
    # Fill in the array with the highest bar to the left of the current bar 
    left[0] = numbers[0]
    # Fill in the right array with the highest bar encounted so far from right
    right[n - 1] = numbers[n - 1]
    # Iterate and complete filling in from left to right and right to left
    for i in range(1, n):
        left[i] = max(left[i - 1], numbers[i])
        right[n - i - 1] = max(right[n - i], numbers[n - i - 1])
        
    # Create a variable to keep track of the sum of the unites encountered so far
    total = 0
    # Calculate the total amount of water trapped by iterating through the array
    for i in range(n):
        # The amount of water is the minimum of the left and right minus the current height
        total += min(left[i], right[i]) - numbers[i]
        
    # Return the total amount of water trapped
    return total
    

def main():
    # Example usage of the function
    numbers = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = rain(numbers)
    print(result)  # Output: 6
    # Example usage of the two-pointer function
    result_two_pointer = rain_two_pointer(numbers)  
    print(result_two_pointer)  # Output: 6

if __name__ == "__main__":
    main()