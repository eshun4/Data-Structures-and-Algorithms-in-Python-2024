"""
Coin Change Problem
Given a list of coin denominations and a target amount, 
find the minimum number of coins needed to make that amount. 
If it's not possible to make that amount, return -1.

Input: coins = [1, 2, 5], amount = 11
Output: 3

"""

# bottomUp Approach
def minNumberOfCoinsForChnge(coins, amount):
    # create dp table to store the minimum number of coins needed to make each amount
    dp = [0] * (amount + 1)
    dp[0] = 0
    
    # Fill in the dp table
    for i in range(1, amount + 1):
        dp[i] = float('inf')  # Initialize with infinity
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    # Return the result
    return dp[amount] if dp[amount] != float('inf') else -1

# recursive
def minNumberOfCoinsForChangeRecursive(coins, amount):
    # get length of coins
    n = len(coins)
    # check for base cases
    if n == 0:
        return float('inf')
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    min_coins = float('inf')
    for coin in coins:
        minCoins = minNumberOfCoinsForChangeRecursive(coins, amount - coin) + 1
        min_coins = min(min_coins, minCoins)
    return min_coins if min_coins != float('inf') else -1

# Memoized recursive approach
def minNumberOfCoinsForChangeMemoized(coins, amount, memo=None):
    if memo is None:
        memo = {}
    # Check if the result is already in the memo
    if amount in memo:
        return memo[amount]
    # Base cases
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    # Recursive case
    min_coins = float('inf')
    for coin in coins:
        minCoins = minNumberOfCoinsForChangeMemoized(coins, amount - coin, memo) + 1
        min_coins = min(min_coins, minCoins)
    # Store the result in the memo
    memo[amount] = min_coins if min_coins != float('inf') else -1
    return memo[amount]

def main():
    # Example usage of the function
    coins = [1, 5, 7, 10]
    amount = 8
    result = minNumberOfCoinsForChnge(coins, amount)
    print(f"Minimum number of coins needed to make {amount} with coins {coins}: {result}")  # Output: 2

    # Example usage of the memoized function
    coins = [1, 5, 7, 10]   
    amount = 8
    result = minNumberOfCoinsForChangeRecursive(coins, amount)
    print(f"Minimum number of coins needed to make {amount} with coins {coins}: {result}")  # Output: 2
    
    # example usage of the memoized function
    coins = [1, 5, 7, 10]   
    amount = 8
    result = minNumberOfCoinsForChangeMemoized(coins, amount)
    print(f"Minimum number of coins needed to make {amount} with coins {coins}: {result}")  # Output: 2
if __name__ == "__main__":
   main()