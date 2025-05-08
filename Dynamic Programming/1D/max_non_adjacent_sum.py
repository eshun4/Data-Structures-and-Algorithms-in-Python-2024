"""
Max Non- Adjacent Sum

Given an array of integers, find the maximum sum of non-adjacent elements in the array.

Input: 
[6, 10, 12, 7, 9, 14]
Output:
Max sum of non-adjacent elements: 32
"""

def max_non_adjacent_sum(arr):
    # get the length of the array
    n = len(arr)
    if n == 1:
        return max(arr[0], 0)
    if n == 2:
        return max(arr[0], arr[1])
    # create a dp array and initialize everything to zero
    dp = [0] * n
    # base case, the first element is the maximum sum of non-adjacent elements
    dp[0] = max(arr[0], 0)
    # the second element is the maximum of the first two elements
    dp[1] = max(0, arr[0], arr[1])
    # Bottom up logic
    for i in range(2, n):
        include = arr[i] + dp[i - 2]
        exclude = dp[i - 1]
        dp[i] = max(include, exclude)
    # return the last element of the dp array, which is the maximum sum of non-adjacent elements
    return dp[n - 1]
    

def main():
    # Example 1:
    arr = [6, 10, 12, 7, 9, 14]
    print(f"Max sum of non-adjacent elements: {max_non_adjacent_sum(arr)}")

    # Example 2:
    arr = [5, 1, 1, 5]
    print(f"Max sum of non-adjacent elements: {max_non_adjacent_sum(arr)}")

    # Example 3:
    arr = [3, 2, 5, 10, 7]
    print(f"Max sum of non-adjacent elements: {max_non_adjacent_sum(arr)}")

if __name__ == "__main__":
    main()