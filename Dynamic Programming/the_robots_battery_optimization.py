"""
6. The Robot's Battery Optimization

Story:
A robot works daily but must recharge fully at least once every three days. 
This means at least one day out of any three consecutive days must be skipped. 
Help the engineer determine the minimum working time while ensuring the robot recharges enough.

Function Signature:
    def minRobotWorkingTime(time: List[int]) -> int:
        pass

Input:

    3 <= len(time) <= 10^4

    0 <= time[i] <= 1000

Output:

Minimum total time worked with the recharge constraint.

Examples:

Input: time = [5, 5, 5, 5, 5]
Output: 15
Explanation: Work days 0,1, skip 2, then 3,4.

Input: time = [1, 2, 3, 1, 2, 3]
Output: 6
Explanation: Work days 0,1, skip 2, then 3,4.

"""

from typing import List

def minRobotWorkingTime(time: List[int]) -> int:
    # get the length of time 
    n = len(time)
    
    if n == 0:
        return 0
    if n == 1:
        return time[0]
    if n == 2:
        return min(time[0], time[1])
    
    # create the dp array 
    dp = [0] * n 
    
    # Check base cases 
    dp[0] = time[0]
    dp[1] = time[1]
    dp[2] = min(time[0] + time[1], time[0] + time[2], time[1]+ time[2])
    
    # FIll the dp array
    for i in range(3, n):
        dp[i] = min(time[i - 1] + time[i - 2] + dp[i - 3], time[i - 2] + time[i - 3] + dp[i - 1], time[i - 1] + time[i - 3] + dp[i - 2])
        
    return dp[n - 1]

def main():
    time1 = [5, 5, 5, 5, 5]
    result1 = minRobotWorkingTime(time1)
    print(f"The min time for array {time1} is {result1}")
    
    time2 = [1, 2, 3, 1, 2, 3]
    result2 = minRobotWorkingTime(time2)
    print(f"The min time for array {time2} is {result2}")
    
    time3 = [10, 20, 30, 40, 50, 60, 70]
    result3 = minRobotWorkingTime(time3)
    print(f"The min time for array {time3} is {result3}")
    
    time4 = [0, 0, 0, 0, 0, 0, 0]
    result4 = minRobotWorkingTime(time4)
    print(f"The min time for array {time4} is {result4}")
    
    time5 = [100, 200, 300, 400, 500]
    result5 = minRobotWorkingTime(time5)
    print(f"The min time for array {time5} is {result5}")
    
    time6 = [3, 2, 1, 3, 2, 1, 3]
    result6 = minRobotWorkingTime(time6)
    print(f"The min time for array {time6} is {result6}")
    
    

if __name__ == "__main__":
    main()  