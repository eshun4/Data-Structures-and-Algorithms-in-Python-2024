"""
Counting Binary Search Trees.

"""

def countBST(n):
    if n == 0 or n == 1:
        return 1
    ans = 0
    for i in range(1, n + 1):
        x = countBST(i - 1)
        y = countBST(n - i)
        ans += (x * y)
    return ans


def countBSTTopDown(n, memo= {}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    ans = 0
    for i in range(1, n + 1):
        x = countBSTTopDown(i - 1, memo)
        y = countBSTTopDown(n - i, memo)
        ans += (x * y)
    memo[n] = ans
    return memo[n]

def countBSTBottomUp(n):
    if n == 0 or n == 1:
        return 1
    
    # create dp array
    dp = [0] * (n + 1)
    # base case
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    return dp[n]
    

def main():
    n = 5
    print(f"The number of BST's are: {countBST(n)}")
    
    n = 5
    print(f"The number of BST's are: {countBSTTopDown(n)}")
    
    n = 5
    print(f"The number of BST's are: {countBSTBottomUp(n)}")


if __name__ == "__main__":
    main()