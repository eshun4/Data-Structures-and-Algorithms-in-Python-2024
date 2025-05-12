"""
Longest Common Subsequence.

Given two sequences, find the length of the longest subsequence which is common to both of them. 

Input.
s1 = "ABCD"
s2 = "ABEDG"

Output
3
(ABD)

"""

def longest_common_subsequence(s1, s2, i ,j):
    # base case
    if i == len(s1) or j == len(s2):
        return 0
    # recursive case
    if s1[i] == s2[j]:
        return 1 + longest_common_subsequence(s1, s2, i + 1, j + 1)
    
    # If we include or exclude 
    op1 = longest_common_subsequence(s1, s2, i + 1, j)
    op2 = longest_common_subsequence(s1, s2, i, j + 1)
    
    return max(op1, op2)

def longest_common_subsequence_memo(s1, s2, i ,j, memo=None):
    if memo is None:
        memo = {}
    # base case
    if i == len(s1) or j == len(s2):
        return 0
    
    # recursive case
    if (i, j) in memo:
        return memo[(i, j)]
    
    if s1[i] == s2[j]:
        memo[(i, j)] = 1 + longest_common_subsequence_memo(s1, s2, i + 1, j + 1)
        return memo[(i, j)]
    
    # If we include or exclude 
    op1 = longest_common_subsequence_memo(s1, s2, i + 1, j)
    op2 = longest_common_subsequence_memo(s1, s2, i, j + 1)
    
    memo[(i, j)] = max(op1, op2)
    return memo[(i, j)]

def longest_common_subsequence_dp(s1, s2, i, j, dp):
    # base case
    if i == len(s1) or j == len(s2):
        return 0

    # Check if dp state is already computed
    if dp[i][j] != -1:
        return dp[i][j]

    # recursive case
    if s1[i] == s2[j]:
        dp[i][j] = 1 + longest_common_subsequence_dp(s1, s2, i + 1, j + 1, dp)
        return dp[i][j]

    # If we include or exclude
    op1 = longest_common_subsequence_dp(s1, s2, i + 1, j, dp)
    op2 = longest_common_subsequence_dp(s1, s2, i, j + 1, dp)

    dp[i][j] = max(op1, op2)
    return dp[i][j]

def longest_common_subsequence_bottom_up(s1, s2):
    # get length of t s1 and s2
    s1_len, s2_len = len(s1), len(s2)
    # create dp array
    dp = [[0] * (s2_len + 1) for _ in range(s1_len + 1)]
    
    # Iterate and fill dp table
    for i in range(1, s1_len + 1):
        for j in range(1, s2_len + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # If we include or exclude
                op1 = dp[i - 1][j]
                op2 = dp[i][j - 1]
                dp[i][j] = max(op1, op2)
                
    return dp[s1_len][s2_len]
            

def main():
    s1 = "ABCD"
    s2 = "ABEDG"
    
    # get length of t s1 and s2
    s1_len, s2_len = len(s1), len(s2)
     # create dp table
    dp = [[-1] * s2_len for _ in range(s1_len)]
    
    print(f"The length of the longest common subsequence is: {longest_common_subsequence(s1, s2, 0, 0)}")
    print(f"The length of the longest common subsequence (Memoized) is: {longest_common_subsequence(s1, s2, 0, 0)}")
    print(f"The length of the longest common subsequence (DP - Memoized) is: {longest_common_subsequence_dp(s1, s2, 0, 0, dp)}")
    print(f"The length of the longest common subsequence (DP - Bottom-Up) is: {longest_common_subsequence_bottom_up(s1, s2)}")

if __name__ == "__main__":
    main()