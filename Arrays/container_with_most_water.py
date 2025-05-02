"""
Container With Most Water

Problem:
Given n non-negative integers a1, a2, ..., an where each represents a point at coordinate (i, ai).
Find two lines, which together with the x-axis forms a container, such that the container contains the most water.
Your task is to find the maximum area of water that can be contained by two lines.

Input:
- n: Number of lines (1 <= n <= 10^5)   
- a: List of integers representing the heights of the lines (0 <= a[i] <= 10^4)

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation: The maximum area is formed between the lines at index 1 and index 8, which have heights 8 and 7 respectively.
"""


def maxArea(height):
    """
    Calculate the maximum area of water that can be contained between two vertical lines.

    This function uses the two-pointer technique to find the maximum area formed by any two lines
    in the input list `height`. The area is determined by the shorter of the two lines and the 
    horizontal distance between them.

    Args:
        height (List[int]): A list of non-negative integers representing the heights of vertical lines.

    Returns:
        int: The maximum area of water that can be contained. Returns 0 if the input list has fewer than 2 elements.

    Example:
        >>> maxArea([1,8,6,2,5,4,8,3,7])
        49

    Approach:
        - Initialize two pointers, one at the beginning (`left`) and one at the end (`right`) of the list.
        - Calculate the area formed by the lines at the two pointers and update the maximum area if necessary.
        - Move the pointer pointing to the shorter line inward to potentially find a larger area.
        - Repeat until the two pointers meet.

    Edge Cases:
        - If the input list has fewer than 2 elements, return 0 as no container can be formed.
    """
    # Get the length of the height list
    n = len(height)
    
    # If there are fewer than 2 lines, no container can be formed, so return 0
    if n < 2:
        return 0

    # Initialize two pointers: one at the beginning (left) and one at the end (right) of the list
    left = 0
    right = len(height) - 1

    # Variable to store the maximum area found so far
    max_area = 0

    # Loop until the two pointers meet
    while left < right:
        # Calculate the area formed by the lines at the current pointers
        # The height of the container is determined by the shorter line
        # The width of the container is the distance between the two pointers
        area = min(height[left], height[right]) * (right - left)

        # Update the maximum area if the current area is larger
        max_area = max(max_area, area)

        # Move the pointer pointing to the shorter line inward
        # This is because moving the shorter line might increase the area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    # Return the maximum area found
    return max_area


def main():
    # Example usage of the function
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = maxArea(height)
    print(result)  # Output: 49
    
if __name__ == "__main__":
    main()