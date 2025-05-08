"""
Longest Increasing Sequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Input:
[50, 4, 10, 8, 30, 100]
Output:
4
"""


def longest_increasing_subsequence(sequence):
    # get the length of the array
    n = len(sequence)
    # create a dp array
    dp = [1] * n
    # assume lis is 1
    max_length = 1
    # fill dp table
    for i in range(1, n):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                max_length = max(max_length, dp[i])
    # return the largest length of increasing subsequence
    return max_length

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
# Hint: Use binary search to find the position of the current element in the dp array.
# This will help you to reduce the time complexity to O(n log(n)).
def longest_increasing_subsequence_binary_search(sequence):
    # create a dp array to store the longest increasing subsequence
    dp = []
    for num in sequence:
        # use binary search to find the position of the current element in the dp array
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        # if the position is equal to the length of the dp array, append the current element
        if left == len(dp):
            dp.append(num)
        else:
            # otherwise, replace the element at that position with the current element
            dp[left] = num
    return len(dp)  

        
    
def main():
    # Example 1:
    sequence = [50, 4, 10, 8, 30, 100]
    print(f"Length of longest increasing subsequence: {longest_increasing_subsequence(sequence)}")

    # Example 2:
    sequence = [3, 2, 5, 10, 7]
    print(f"Length of longest increasing subsequence: {longest_increasing_subsequence(sequence)}")

    # Example 3:
    sequence = [1, 3, 6, 7, 9, 4, 10, 5]
    print(f"Length of longest increasing subsequence: {longest_increasing_subsequence(sequence)}")
    
    # Example 4:
    sequence = [50, 4, 10, 8, 30, 100]
    print(f"Length of longest increasing subsequence: {longest_increasing_subsequence_binary_search(sequence)}")
    

if __name__ == "__main__":
    main()
