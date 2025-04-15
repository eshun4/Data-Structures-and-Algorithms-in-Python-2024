"""
2. The Temple Restoration

Story:
You're restoring a sacred temple over n days. 
To ensure momentum, your master demands that at least 2 of every 3 consecutive days must be worked on. 
Choose the workdays such that the total time spent is minimized.

Function Signature:
    def minTimeTwoOutOfThree(time: List[int]) -> int:
        pass

Input:

3 <= len(time) <= 10^4

0 <= time[i] <= 1000

Output:

    Integer representing the minimum time to work under the 2-of-3-day constraint.

    Input: time = [1, 2, 3]
    Output: 3
    Explanation: Work on days 0 and 2. Skipping only day 1, which maintains 2 workdays in a 3-day window.

    Input: time = [10, 1, 10, 1, 10]
    Output: 22
    Explanation: Work on days 1, 2, 4 to maintain the 2-of-3-day rule.

"""

from typing import List


def minTimeTwoOutOfThree(time: List[int]) -> int:
    # Lets understand the problem first
    # Given 1,2, 3 abstart array how do i choose the workdays such that my total is minimal?
    # Options:
    # 1 + 3 = 4, for each i in a[0....i], time[i] + dp[i - 1] + time[i- 2] 
    # 2 + 3 = 5, for each i in a[0....i], time[i] + time[i - 1] + dp[i - 3]
    # 1 + 2 = 3, for each i in a[0....i], dp[i - 3] + time[i - 1] + time[i - 2]
    
    # get the base cases
    # dp[0] = time[0]
    # dp[1] = time[1] + time[0]
    # dp[2] = min(time[0] + time[1], time[1] + time[2], time[0] + time[2])
    
    # recurrence relation 
    # = f(n) =
    # {
        # min(time[i] + dp[i - 1] + time[i- 2], time[i] + time[i - 1] + dp[i - 3], dp[i - 3] + time[i - 1] + time[i - 2]), if n >=3,
    # }


    # get the length of the array
    n = len(time)
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return time[1] + time[0]
    # if n == 2:
    #     return min(time[0] + time[1], time[1] + time[2], time[0] + time[2])
    
    
    # create the dp array
    dp = [0] * n
    
    # Base cases
    dp[0] = time[0]
    dp[1] = time[1] + time[0]
    dp[2] = min(time[0] + time[1], time[1] + time[2], time[0] + time[2])
    
    # fill the dp table
    for i in range(3, n):
        dp[i] = min(time[i] + dp[i - 1] + time[i- 2], time[i] + time[i - 1] + dp[i - 3], dp[i - 3] + time[i - 1] + time[i - 2])
        
    # return the minimum of the last three days
    return dp[n - 1]
    

def main():
    # Example test cases
    time1 = [1, 2, 3]
    print(f"Minimum total time for {time1} is: {minTimeTwoOutOfThree(time1)}")

    time2 = [10, 1, 10, 1, 10]
    print(f"Minimum total time for {time2} is: {minTimeTwoOutOfThree(time2)}")

    # time3 = [1, 2, 3, 4, 5]
    # print(f"Minimum total time for {time3} is: {minTimeTwoOutOfThree(time3)}")

if __name__ == "__main__":
    main()