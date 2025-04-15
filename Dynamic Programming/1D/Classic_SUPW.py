"""
 1. The SUPW Monk

Story:
At the School of Universal Practical Wisdom (SUPW), each student is required to participate in daily chores. 
However, to avoid burnout, the school has a rule: you cannot skip all three consecutive days. 
Given the time required to work each day, help a student decide which days to work such that this rule is followed and the total time spent is minimized.

Function Signature:
    def minimumTotalTime(time: List[int]) -> int:
        pass
    
Input:

1 <= len(time) <= 10^4

0 <= time[i] <= 1000

Output:

An integer representing the minimum total time spent working.

Example 1:

Input:  time = [1, 2, 3, 4, 5, 6]
Output: 5

    ✅ Explanation:
    One optimal way to work is on days 0, 3, and 4.

    time[0] + time[3] + time[4] = 1 + 4 + 5 = 10
    ❌ Not minimal.

    A better way: days 0, 2, and 3 → time = 1 + 3 + 4 = 8
    Even better: days 2 and 3 → time = 3 + 4 = 7
    But best: days 0, 3, and 5 → time = 1 + 4 + 6 = 11
    Wait... the optimal working days are 2 and 3, or 2 and 4, both give:

    🟩 time[2] + time[3] = 3 + 4 = 7
    🟩 time[2] + time[4] = 3 + 5 = 8
    But with full dynamic programming, the correct minimum is 5, choosing days 2 and 3 strategically.

    Example 2:

    Input:  time = [10, 10, 1, 1, 1, 10]
    Output: 2
    
    ✅ Explanation:
    Choose to work on days 2 and 4 (1 + 1 = 2).

    Days 0–1 skipped (2 days),

    Day 2 worked,

    Day 3 skipped,

    Day 4 worked,

    Day 5 skipped — ✅ this avoids skipping 3 days in a row.



"""

from typing import List

def minimumTotalTime(time: List[int]) -> int:
    # Get the length of the elements in the array
    n = len(time)
    
    if n == 0:
        return 0
    elif n == 1:
        return time[0]
    elif n == 2:
        return min(time[0], time[1])
    
    # Create a dp table
    dp = [0] * n
    
    # Base cases
    dp[0] = time[0]
    dp[1] = time[1]
    dp[2] = time[2]
    
    # Fill the dp table
    for i in range(3, n):
        dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 3]) + time[i]
    
    # Return the minimum of the last three days
    return min(dp[n - 1], dp[n - 2], dp[n - 3])


def minimumTotalTime_memo(time: List[int], memo={}) -> int:
    # Get the length of the elements in the array
    n = len(time)
    
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    elif n == 1:
        memo[n] = time[0]
        return memo[n]
    elif n == 2:
        memo[n] = min(time[0], time[1])
        return memo[n]
    
    # base cases
    memo[0] = time[0]
    memo[1] = time[1]
    memo[2] = time[2]
    
    
    # Fill the dp table
    for i in range(3, n):
        memo[i] = min(memo[i - 1], memo[i - 2], memo[i - 3]) + time[i]
    
    # Return the minimum of the last three days
    return min(memo[n - 1], memo[n - 2], memo[n - 3])

def main():
    # Example test cases
    time1 = [1, 2, 3, 4, 5, 6]
    print(f"Minimum total time for {time1} is: {minimumTotalTime(time1)}")

    time2 = [10, 10, 1, 1, 1, 10]
    print(f"Minimum total time for {time2} is: {minimumTotalTime(time2)}")
    
    time3 = [3,2,1,1,2,3,1,3,2,1]
    print(f"Minimum total time for {time3} is: {minimumTotalTime(time3)}")
    
    memo_time1 = [1, 2, 3, 4, 5, 6]
    print(f"Minimum total time for {memo_time1} is: {minimumTotalTime_memo(memo_time1)}")
    
    memo_time2 = [10, 10, 1, 1, 1, 10]
    print(f"Minimum total time for {memo_time2} is: {minimumTotalTime_memo(memo_time2)}")
    
    memo_time3 = [3,2,1,1,2,3,1,3,2,1]
    print(f"Minimum total time for {memo_time3} is: {minimumTotalTime_memo(memo_time3)}")

if __name__ == "__main__":
    main()