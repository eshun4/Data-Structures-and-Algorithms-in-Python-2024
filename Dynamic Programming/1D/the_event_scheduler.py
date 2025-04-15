"""
8. The Event Scheduler

Story:
A planner is booking work events such that each 4-day block has exactly two events. 
Devise the event schedule that minimizes total event cost.

Function Signature:
    def minTwoInFourEvents(time: List[int]) -> int:
        pass
        
Input:

    4 <= len(time) <= 9996 and len(time) % 4 == 0

    0 <= time[i] <= 1000

Output:

Minimum event time cost.

Examples:

Input: time = [2, 5, 1, 3, 6, 4, 1, 2]
Output: 3
Explanation: [1,2] from first block, [6,7] from second.

Input: time = [4,4,4,4, 1,1,1,1]
Output: 2
Explanation: Choose 2 from each block, pick cheapest.

"""

from typing import List


def minTwoInFourEvents(time: List[int]) -> int:
    pass

def main():
    pass

if __name__ == "__main__":
    main()  