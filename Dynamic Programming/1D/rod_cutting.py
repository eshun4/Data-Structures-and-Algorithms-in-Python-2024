"""
*** Rod cutting Problem ***

    In this question the greedy approach does not work.
    
    Statement:
        Given a rod of length n and array prices of length n denoting the cost of pieces of the rod of length 1 to n, find the maximum amount
        if the rod is cut up optimally.
        
        Example 1:
        n = 8, prices = [1, 3, 4, 5, 7, 9, 10, 11]
        Output: Maximum profit = 12 (cut the rod into 1 piece of length 2)

        Example 2:
        n = 4, prices = [1, 1, 1, 6]
        Output: Maximum profit = 10 (cut the rod into 2 pieces of length 2 each)

"""
def rod_cutting(n, prices, memo=None):
    if memo is None:
        memo = {}

    if n == 0:
        return 0

    if n in memo:
        return memo[n]

    ans = 0
    for i in range(1, n + 1):
        if i <= len(prices):  # Ensure we don't index out of bounds
            ans = max(ans, prices[i - 1] + rod_cutting(n - i, prices, memo))
    
    memo[n] = ans
    return ans


def rod_cutting(prices):
    n = len(prices)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, i + 1):
            max_val = max(max_val, prices[j - 1] + dp[i - j])
        dp[i] = max_val

    return dp[n]


def main():
    # Example 1:
    n, prices = 8, [1, 3, 4, 5, 7, 9, 10, 11]
    print(f"Maximum profit = {rod_cutting(n, prices)}")

    # Example 2:
    n, prices = 4, [1, 1, 1, 6]
    print(f"Maximum profit = {rod_cutting(n, prices)}")

if __name__ == "__main__":
    main()