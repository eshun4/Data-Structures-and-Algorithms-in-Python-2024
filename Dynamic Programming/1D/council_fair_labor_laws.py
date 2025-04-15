"""
3. The Council's Fair Labor Law

Story:
The Council of Builders mandates fair scheduling: each 3-day window must contain exactly 2 working days. 
Help a manager assign work such that total work time is minimized.

Function Signature:
    def minTimeExactTwoOutOfThree(time: List[int]) -> int:
        pass
        
Input:

    3 <= len(time) <= 1000

    0 <= time[i] <= 1000

Output:

Integer representing the minimum time.

Input: time = [1, 2, 3]
Output: 3
Explanation: Work on days 0 and 1 or 1 and 2. Must choose exactly 2 in every 3 days.

Input: time = [1, 2, 1, 2, 1]
Output: 5
Explanation: Work on days [0,1], [2,3], [4]. Sliding window guarantees exact 2-day coverage.
    
"""

from typing import List


def minTimeExactTwoOutOfThree(time: List[int]) -> int:
    pass


def main():
    pass

if __name__ == "__main__":
    main()