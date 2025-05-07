"""
Minimum number of jumps to reach the end of the array

Given an array of integers where each element represents the maximum number of jumps that can be made from that position, the task is to find the minimum number of jumps to reach the end of the array.
If it is not possible to reach the end, return -1.

Input: arr = [2, 3, 1, 1, 4]
Output: 2

Explanation: The minimum number of jumps to reach the end is 2 (2 -> 4).

"""

def min_jumps(arr, n, dp, i=0):
    # Base case: if we are at the last index, no jumps are needed
    if i == n - 1:
        return 0
    # If the current index is out of bounds or the value is 0, return infinity
    if i >= n or arr[i] == 0:
        return float('inf')
    # recursive case: check if the result is already in the dp array
    if dp[i] != 0:
        return dp[i]
    # Assume the number of jumps needed is infinity
    steps = float('inf')
    max_jump = arr[i]
    # Loop through the range of jumps from the current index
    for jump in range(1, max_jump + 1):
        # Calculate the number of jumps needed from the next index
        next_index = i + jump
        sup_prob = min_jumps(arr, n, dp, next_index)
        # If the next index is within bounds, update the number of steps
        if next_index < n and sup_prob != float('inf'):
            steps = min(steps, sup_prob + 1)
    
    # Store the result in the dp array
    dp[i] = steps
    # return
    return dp[i]
    
    

def main():
    # Example usage of the function
    arr = [2, 3, 1, 1, 4]
    n = len(arr)
    dp = [0] * n
    result = min_jumps(arr, n, dp)
    print(f"Minimum number of jumps to reach the end: {result}")  # Output: 2


if __name__ == "__main__":
    main()