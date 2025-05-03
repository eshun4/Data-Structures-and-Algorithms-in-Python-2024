"""
Given a ladder of size N, and an integer k, write a function to compute the 
number of ways to climb the ladder if you can take a jump of 
at most k at every step. 

Input N = 4, k = 3
Output 7
Explanation:
There are 7 ways to climb the ladder:
"""
# recursive
def countWays(n, k,):
    # get the base case if n == 0 or n == 1
    if n == 0:
        return 1
    if n < 0:
        return 0
    ans = 0
    # loop through the range of k and add the number of ways to climb the ladder
    for jump in range(1, k + 1):
        ans += countWays(n - jump, k)
    return ans


# mempized
def countWaysMemoized(n, k, memo={}):
    # get the base case if n == 0 or n == 1
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    ans = 0
    # loop through the range of k and add the number of ways to climb the ladder
    for jump in range(1, k + 1):
        ans += countWaysMemoized(n - jump, k, memo)
    memo[n] = ans
    return memo[n]

# DP O(n**k)
def countWaysDP(n, k):
    # get the base case if n == 0 or n == 1
    if n == 0:
        return 1
    if n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    # loop through the range of k and add the number of ways to climb the ladder
    for i in range(1, n + 1):
        for jump in range(1, k + 1):
            if i - jump >= 0:
                dp[i] += dp[i - jump]
    return dp[n]
    
# DP O(n)
def countWaysDPOptimized(n, k):
    # get the base case if n == 0 or n == 1
    if n == 0:
        return 1
    if n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    # loop through the range of k and add the number of ways to climb the ladder
    for i in range(2, n + 1):
        dp[i] = 2 * dp[i - 1]
        if i - k - 1 >= 0:
            dp[i] -= dp[i - k - 1]
    return dp[n]
        
    

    

def main():
    # Example usage of the function
    n = 4
    k = 3
    result = countWays(n, k)
    print(f"Number of ways to climb the ladder of size {n} with max jump {k}: {result}")  # Output: 7
    
    # Example usage of the memoized function
    n = 4
    k = 3
    result = countWaysMemoized(n, k)
    print(f"Number of ways to climb the ladder of size {n} with max jump {k}: {result}")  # Output: 7
    
    # Example usage of the dp function
    n = 4
    k = 3
    result = countWaysDP(n, k)
    print(f"Number of ways to climb the ladder of size {n} with max jump {k}: {result}")  # Output: 7
    
    # Example usage of the optimized dp function
    n = 4
    k = 3
    result = countWaysDPOptimized(n, k)
    print(f"Number of ways to climb the ladder of size {n} with max jump {k}: {result}")  # Output: 7
    
   

if __name__ == "__main__":
    main()