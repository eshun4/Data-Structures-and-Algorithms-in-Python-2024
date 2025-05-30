from functools import lru_cache

"""
Problem Statement:
Given the sum and an array of non-negative numbers. Determine if subset of array exists with sum equal SUM.

Examples:
Sum = 12
array = [2, 7, 4, 5, 19]

Hint: f(x, y) -> whether sum of y can be formed by using array[x.....].

"""


def subsetSum(index, sum1, array):
    # No elements left for sum
    if index == -1:
        return (sum1 == 0)
    ans = False
    # Include array[index] in sum
    if sum1 >= array[index]:
        ans |= subsetSum(index - 1, sum1 - array[index], array)
    # Exclude[index]
    ans |= subsetSum(index - 1, sum1, array)
    return ans



def possible_subsets(index, sum1, array, res=None, sol=None):
    if res is None:
        res = []
    if sol is None:
        sol = []
    if index == -1:
        if sum1 == 0:
            res.append(sol[:])
        return
    if sum1 >= array[index]:
        sol.append(array[index])
        possible_subsets(index - 1, sum1 - array[index], array, res, sol)
        sol.pop()
    possible_subsets(index - 1, sum1, array, res, sol)
    return res



def subsetSumTabulation(index, sum1, array):
    # Get the length of the array
    n = len(array)
    
    # Create the dp table with dimensions (n+1) x (sum1+1)
    # dp[i][j] will be True if a subset of array[0...i-1] has a sum equal to j
    dp = [[False] * (sum1 + 1) for _ in range(n + 1)]
    
    # Base case: A sum of 0 is always achievable (empty subset)
    dp[0][0] = True
    
    # Initialize the first row for sums greater than 0 (not achievable with no elements)
    for j in range(1, sum1 + 1):
        dp[0][j] = False
        
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(0, sum1 + 1):
            # Exclude the current element (carry forward the value from the previous row)
            dp[i][j] = dp[i - 1][j]
            
            # Include the current element if it does not exceed the current sum
            if j - array[i - 1] >= 0:
                dp[i][j] |= dp[i - 1][j - array[i - 1]]
    
    # Return whether the target sum is achievable using all elements
    return dp[n][sum1]

def subsetSumTabulationOptimized(sum1, array):
    """
    Determines if a subset of the array sums to sum1 using a space-optimized DP approach.
    This implementation uses only two rows to reduce memory usage.
    Memory Complexity: O(2 * sum) = O(sum)
    Time Complexity: O(n * sum)
    """
    # Get the length of the array
    n = len(array)
    
    # Create the dp table with two rows
    dp = [[False] * (sum1 + 1) for _ in range(2)]
    
    # Base case: A sum of 0 is always achievable (empty subset)
    dp[0][0] = True
    
    # Initialize the first row for sums greater than 0 (not achievable with no elements)
    for j in range(1, sum1 + 1):
        dp[0][j] = False
    
    # Fill the dp table row by row
    for i in range(1, n + 1):
        for j in range(0, sum1 + 1):
            # Carry forward the value from the previous row (exclude the current element)
            dp[1][j] = dp[0][j]
            
            # Include the current element if it does not exceed the current sum
            if j - array[i - 1] >= 0: 
                dp[1][j] |= dp[0][j - array[i - 1]]
        
        # Copy the second row to the first row for the next iteration
        for j in range(0, sum1 + 1):
            dp[0][j] = dp[1][j]
    
    # Return whether the target sum is achievable
    return dp[1][sum1]


def subsetSumTabulationSuperOptimized(sum1, array):
    """
    Determines if a subset of the array sums to sum1 using space-optimized DP.
    Memory Complexity: O(sum)
    Time Complexity: O(n * sum)
    """
    # Get the length of the array
    n = len(array)
    
    # Create a 1D dp array for optimization
    dp = [False] * (sum1 + 1)
    
    # Base case: A sum of 0 is always achievable (empty subset)
    dp[0] = True
    
    # Iterate over each element in the array
    for i in range(n):
        # Traverse the dp array backward to avoid overwriting results
        for j in range(sum1, array[i] - 1, -1):
            dp[j] |= dp[j - array[i]]
    
    # Return whether the target sum is achievable
    return dp[sum1]



def subsetSumMultiple(index, sum1, array):
    # No elements left for sum
    if index == -1:
        return (sum1 == 0)
    ans = False
    # Include array[index] in sum
    if sum1 >= array[index]:
        ans |= subsetSumMultiple(index, sum1 - array[index], array)
    # Exclude[index]
    ans |= subsetSumMultiple(index - 1, sum1, array)
    return ans


def subsetSumMemoized(index, sum1, array, memo={}):
    # Memoization key
    key = (index, sum1)
    if key in memo:
        return memo[key]
    # No elements left for sum
    if index == -1:
        return (sum1 == 0)
    ans = False
    # Include array[index] in sum
    if sum1 >= array[index]:
        ans |= subsetSumMemoized(index - 1, sum1 - array[index], array, memo)
    # Exclude[index]
    ans |= subsetSumMemoized(index - 1, sum1, array, memo)
    # Store result in memo
    memo[key] = ans
    return ans
    


def main():
    # Test case
    array = [2, 7, 4, 5, 19]
    sum1 = 12
    print(subsetSum(len(array) - 1, sum1, array))
    print(subsetSumTabulation(len(array) - 1, sum1, array))
    print(subsetSumMemoized(len(array) - 1, sum1, array))
    print(subsetSumTabulationOptimized(sum1, array))
    print(subsetSumTabulationSuperOptimized(sum1, array))
    print(possible_subsets(len(array) - 1, sum1, array))
    

if __name__ == "__main__":
    main()