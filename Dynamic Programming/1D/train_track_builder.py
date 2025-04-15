"""
10. The Train Track Builder

Story:
A team building train tracks must work at least 1 day out of every 2 days. 
No 2 consecutive skips. Optimize the build schedule for cost.

Function Signature:
    def minTrackBuilderTime(time: List[int]) -> int:
        pass
        
Input:

    2 <= len(time) <= 10^4

    0 <= time[i] <= 1000

Output:

Minimum cost ensuring every 2-day window includes at least 1 workday.

Examples:

Input: time = [1, 100, 1, 100, 1]
Output: 3
Explanation: Work on 0,2,4. Never skip two days.

Input: time = [10, 1, 1]
Output: 1
Explanation: Work on day 1.

"""

from typing import List

def minTrackBuilderTime(time: List[int]) -> int:
    n = len(time)
    if n == 0:
        return 0
    if n == 1:
        return time[0]
    dp = [0] * n
    dp[0] = time[0]
    dp[1] = min(time[0], time[1])

    for i in range(2, n):
        dp[i] = min(dp[i-1] + time[i], dp[i-2] + time[i])

    return min(dp[-1], dp[-2])


def main():
    # Example 1
    time1 = [1, 100, 1, 100, 1]
    print(minTrackBuilderTime(time1))  # Output: 3
    
    # Example 2
    time2 = [10, 1, 1]
    print(minTrackBuilderTime(time2))  # Output: 1

if __name__ == "__main__":
    main()  
