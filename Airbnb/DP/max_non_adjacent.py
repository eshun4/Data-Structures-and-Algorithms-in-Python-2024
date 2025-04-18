"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

"""


def max_non_adjacent(numbers):
    """
    Returns the largest sum of non-adjacent numbers.
    Use recursion.
    There are two options;
    1. get max of first element and skip the next one
    2. Get max of 2nd element and skip first
    """
    
    # get length of numbers
    n = len(numbers)
    def recursive(n):
        # Create base cases
        if n < 0:
            return 0
        if n == 0:
            return numbers[0]
        include = numbers[n] + recursive(n - 2)
        exclude = recursive(n - 1)
        return max(include, exclude)

    return recursive(n - 1)

def max_non_adjacent_dp(numbers):
    # get length of numbers
    n = len(numbers)
    # Create base cases
    if n < 0:
        return 0
    if n == 0:
        return numbers[0]
    
    # Create dp table
    dp = [0] * n
    
    # Create base cases
    dp[0] = numbers[0]
    dp[1] = max(dp[0], dp[1])
    
    # iterate through dp table
    for i in range(2, n):
        exclude = dp[i - 1]
        include = numbers[i] + dp[i - 2]
        
        dp[i] = max(include, exclude)
        
    # return dp 
    return dp[n - 1]

    

def main():
    numbers = [2, 4, 6, 2, 5]
    numbers2 = [5, 1, 1, 5]
    print(max_non_adjacent(numbers))
    print(max_non_adjacent(numbers2))
    print("")
    print(max_non_adjacent_dp(numbers))
    print(max_non_adjacent_dp(numbers2))

if __name__ == "__main__":
    main()