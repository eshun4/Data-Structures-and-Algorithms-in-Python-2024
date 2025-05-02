"""
Maximum Subarray Sum
Implement a function that takes an input a vector of integers, and prints the maximum subarray sum that can be formed. A subarray is defined as consecutive segment of the array. If all numbers are negative, then return 0.

Input

{-1,2,3,4,-2,6,-8,3}
Output

13



Hint

Expected Time Complexity
O(N)


Space Complexity
O(1)


"""


def max_sub_array(arr):
    """
    Given an array of integers, find the maximum subarray sum that can be formed.
    A subarray is defined as a consecutive segment of the array.
    If all numbers are negative, return 0.

    Args:
    arr (list): The input array.

    Returns:
    int: The maximum subarray sum.
    """
    max_sum = 0  # Initialize the maximum sum to 0
    current_sum = 0  # Initialize the current sum to 0

    for num in arr:
        current_sum += num  # Add the current number to the current sum
        if current_sum < 0:  # If the current sum becomes negative, reset it to 0
            current_sum = 0
        max_sum = max(max_sum, current_sum)  # Update the maximum sum if needed

    return max_sum


def main():
    arr = [-1, 2, 3, 4, -2, 6, -8, 3]
    result = max_sub_array(arr)
    print("Maximum Subarray Sum:", result)  # Output: Maximum Subarray Sum: 13
# Example usage
if __name__ == "__main__":
    main()
    
    
    
# OPTIMIZED DYNAMIC PROGRAMMING SOLUTION
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         # get the length of nums
#         n = len(nums)
#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]
#         # create dp table 
#         dp = [0] * n
#         # Check base cases 
#         dp[0] = nums[0]
#         dp[1] = max(nums[0] + nums[1], nums[1])

#         # fill in dp table
#         for i in range(2, n):
#             dp[i] = max(dp[i - 1] + nums[i], nums[i])
        
#         return max(dp)
        


# BELOW IS THE RECURSIVE SOLUTION

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         # get the length of nums
#         n = len(nums)
#         memo = {}
        
#         def rec_sub_array(index):
#             # check for base cases
#             if index == 0:
#                 memo[0] = nums[0]
#                 return nums[0]
#             # check if index is in memo
#             if index in memo:
#                 return memo[index]
            
#             result =  max(rec_sub_array(index - 1) + nums[index], nums[index])
#             memo[index] = result
#             return memo[index]

        
#         rec_sub_array(n - 1)
#         return max(memo.values())
        


