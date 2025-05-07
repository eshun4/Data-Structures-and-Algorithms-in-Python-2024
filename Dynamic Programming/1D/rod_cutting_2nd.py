"""
Rod Cutting Problem
Given a rod of length n and a list of prices for different lengths,
find the maximum revenue that can be obtained by cutting the rod into pieces.

Input: n = 8, prices = [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
"""
# recursive solution
def max_profit(prices, n):
    # base case
    if n <= 0:
        return 0
    # recursive case
    max_val = float('-inf')
    for i in range(n):
        cut_length = i + 1
        curr_ans = prices[i] + max_profit(prices, n - cut_length)
        max_val = max(max_val, curr_ans)
    return max_val

# bottom up solution
def max_profit(prices, n):
    # create dp table to store the maximum profit for each length
    dp = [0] * (n + 1)
    dp[0] = 0  # Base case: no profit for length 0
    
    # Fill in the dp table
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            cut_length = j + 1
            curr_ans = prices[j] + dp[i - cut_length]
            max_val = max(max_val, curr_ans)
        # Store the maximum profit for length i
        dp[i] = max_val
    
    # Return the result
    return dp[n]
    
def main():
    # Example usage
    n = 8
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    result = max_profit(prices, n)
    print(f"Maximum profit for rod of length {n} is: {result}")
    
    # Example usage of the memoized function
    n = 8   
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    result = max_profit(prices, n)
    print(f"Maximum profit for rod of length {n} is: {result}")  # Output: 22


if __name__ == "__main__":
    main()