"""
7. The Accountant's 1-in-3 Rule

Story:
A strict accounting policy says exactly one working day is allowed per 3-day window to avoid fatigue. Find the schedule minimizing time that follows this exact rule.

Function Signature:
    def minWorkOneInThree(time: List[int]) -> int:
        pass
        
Input:

    3 <= len(time) <= 9999 and len(time) % 3 == 0

    0 <= time[i] <= 1000

Output:

Minimum work time under the 1-day-per-3-days rule.

Examples:

Input: time = [3, 2, 1, 9, 5, 1]
Output: 2
Explanation: Choose minimum per block: [1,1] → time[2]=1 and time[5]=1.

Input: time = [10, 5, 2, 3, 4, 1]
Output: 3
Explanation: time[2] and time[5] are cheapest in their respective blocks.

"""

from typing import List

def minWorkOneInThree(time: List[int]) -> int:
    pass

def main():
    pass

if __name__ == "__main__":
    main()