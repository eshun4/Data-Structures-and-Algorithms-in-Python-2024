"""
Question:
Given an array of integers, determine if there exists an element in the array such that the sum of all the other elements in the array is equal to that element.
Inputs:
- arr (List[int]): A list of integers.
Outputs:
- bool: Returns True if such an element exists, otherwise False.
Example:
Input: arr = [1, 2, 3, 6]
Output: True
Explanation: The sum of the remaining elements (1 + 2 + 3) equals 6.
Input: arr = [1, 2, 3, 4]
Output: False
Explanation: No element in the array satisfies the condition.

"""

def isPossible(nums):
    # Helper function to recursively check if an element equals the sum of the remaining elements
    def is_helper(index, total_sum, nums):
        # Base case: If index is out of bounds, return False
        if index < 0:
            return False
        
        # Current element
        curr_element = nums[index]
        
        # Check if the current element equals the sum of the remaining elements
        if curr_element == total_sum - curr_element:
            return True
        
        # Recur for the next element
        return is_helper(index - 1, total_sum, nums)
    
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Start the recursion from the last index
    return is_helper(len(nums) - 1, total_sum, nums)


def main():
    # Example 1
    arr1 = [1, 2, 3, 6]
    result = isPossible(arr1)
    print(result)  # Output: True

    # Example 2
    arr2 = [1, 2, 3, 4]
    result = isPossible(arr2)
    print(result)  # Output: False


if __name__ == "__main__":
    main()