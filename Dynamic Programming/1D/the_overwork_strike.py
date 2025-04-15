"""

5. Problem: The Overwork Strike

Description:
Workers demand a schedule where no more than 2 days are worked in every sliding 3-day window. 
Your task is to design a work schedule that satisfies their condition while minimizing the total work time.

Function Signature:

        
Input:

    3 <= len(time) <= 10^4

    0 <= time[i] <= 1000

Return the minimum total work time while adhering to the 2-day work limit per sliding 3-day window.

Examples:
- Input: time = [1, 1, 1, 1, 1]
Output: 3

Explanation: Skip every third day. Work on days [0, 1], skip day 2, then work on days [3, 4].

- Input: time = [10, 1, 1, 1, 10]
Output: 12

Explanation: Skip days 0 and 4. Work on days [1, 2, 3] to minimize time.

"""

from typing import List

def minTimeAtMostTwoOfThree(time: List[int]) -> int:
    pass

def main():
    pass

if __name__ == "__main__":
    main()
    
    
