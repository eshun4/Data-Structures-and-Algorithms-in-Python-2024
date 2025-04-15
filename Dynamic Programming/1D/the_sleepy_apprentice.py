"""
4. The Sleepy Apprentice

Story:
The apprentice is allowed to rest but must not skip two consecutive days. Help plan the apprentice’s work schedule to minimize effort.

Function Signature:
    def minTimeNoTwoSkips(time: List[int]) -> int:
        pass
        
Input:

    1 <= len(time) <= 10^4

    0 <= time[i] <= 1000

Output:

Minimum work time while ensuring no 2 consecutive skips.

Examples:

Input: time = [1, 100, 1, 100, 1]
Output: 3
Explanation: Work on days 0, 2, 4. Never skip two in a row.

Input: time = [10, 5, 10]
Output: 5
Explanation: Work on day 1. Skipping day 0 and 2 is invalid.

min(dp[i-1] + time[i], dp[i - 2] + time[i])
"""

from typing import List

def minTimeNoTwoSkips(time: List[int]) -> int:
    # get the length of the array
    n = len(time)
    
    if n == 0:
        return 0
    if n == 1:
        return time[0]
    
    # Create dp table
    dp = [0] * n 
    # Create base cases
    dp[0] = time[0]
    dp[1] = time[1]
    
    # populate dp table
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + time[i], dp[i - 2] + time[i])
        
    return dp[n - 1]

def main():
    # Example test cases
    time1 = [1, 100, 1, 100, 1]
    print(f"Minimum work time for {time1} is {minTimeNoTwoSkips(time1)}.")

    time2 = [10, 5, 10]
    print(f"Minimum work time for {time2} is {minTimeNoTwoSkips(time2)}.")

if __name__ == "__main__":
    main()  