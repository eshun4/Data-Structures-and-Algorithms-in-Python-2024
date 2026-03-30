"""
1231. Divide Chocolate 🔒

Description
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
 

Constraints:

0 <= k < sweetness.length <= 104
1 <= sweetness[i] <= 105
"""

from typing import List
import math

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
        Starter function for LeetCode 1231 - Divide Chocolate

        Args:
            sweetness: List of chunk sweetness values.
            k: Number of friends. You must make exactly k cuts to form k + 1 pieces.

        Returns:
            The maximum sweetness of the minimum-sweetness piece you can get.

        TODO:
            Implement the solution.
        """
        def helper(guess):
            total_divisions = 0
            cur_sweetness_sum = 0
            for s in sweetness:
                cur_sweetness_sum += s 
                if cur_sweetness_sum >= guess:
                    cur_sweetness_sum = 0
                    total_divisions += 1 
            return total_divisions >= k + 1
                    
                    
        left = 1
        right = sum(sweetness) 
        answer = -1 
        
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                answer = mid 
                left = mid  + 1 
            else:
                right = mid - 1 
        return answer 
    
def run_test_case(test_id: int, sweetness: List[int], k: int, expected: int) -> None:
    solver = Solution()
    actual = solver.maximizeSweetness(sweetness, k)

    print(f"Test {test_id}")
    print(f"  sweetness = {sweetness}")
    print(f"  k         = {k}")
    print(f"  expected  = {expected}")
    print(f"  actual    = {actual}")
    print(f"  PASS      = {actual == expected}")
    print("-" * 50)


def main() -> None:
    # Given examples
    run_test_case(1, [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6)
    run_test_case(2, [5, 6, 7, 8, 9, 1, 2, 3, 4], 8, 1)
    run_test_case(3, [1, 2, 2, 1, 2, 2, 1, 2, 2], 2, 5)

    # Smallest valid size
    run_test_case(4, [7], 0, 7)

    # No cuts: you keep the whole chocolate
    run_test_case(5, [3, 4, 5], 0, 12)

    # Must cut into all single chunks
    run_test_case(6, [4, 1, 7, 3], 3, 1)

    # All equal sweetness values
    run_test_case(7, [5, 5, 5, 5], 1, 10)
    run_test_case(8, [5, 5, 5, 5], 3, 5)

    # Repeated pattern
    run_test_case(9, [1, 1, 1, 1, 1, 1], 2, 2)

    # Increasing values
    run_test_case(10, [1, 2, 3, 4, 5], 1, 6)

    # Decreasing values
    run_test_case(11, [9, 8, 7, 6, 5], 2, 9)

    # One very large chunk
    run_test_case(12, [1, 1, 100, 1, 1], 2, 2)

    # Balanced grouping possible
    run_test_case(13, [2, 2, 2, 2, 2, 2], 2, 4)

    # Uneven grouping
    run_test_case(14, [6, 3, 2, 8, 7, 5], 2, 9)

    # Many small values
    run_test_case(15, [1] * 10, 4, 2)

    # Large end values
    run_test_case(16, [10, 1, 1, 1, 10], 1, 11)

    # Another useful edge-style test
    run_test_case(17, [8, 2, 2, 2, 8], 2, 6)

    # Random mixed case
    run_test_case(18, [3, 1, 4, 1, 5, 9, 2], 3, 4)


if __name__ == "__main__":
    main()