"""
A sawtooth sequence is a sequence of numbers that alternate between even and odd. In other words, each element is of different parity than both of its neighboring elements.

Given an array of integers arr, your task is to count the number of contiguous subarrays that represent a sawtooth sequence of at least one element.

A subarray of length 1 is always considered a sawtooth sequence.

Return the total number of sawtooth subarrays.

Example

For arr = [1, 3, 5, 7, 9], the output should be 5.

Since all elements are odd, no subarray of length ≥ 2 alternates parity. Only the 5 single-element subarrays are valid.

For arr = [1, 2, 1, 2, 1], the output should be 15.

Every contiguous subarray alternates parity, so all 15 subarrays are valid.

For arr = [1, 2, 3, 7, 6, 5], the output should be 12.

Only subarrays that do not include the adjacent pair 3, 7 (both odd) satisfy the alternating parity condition.

Input: arr — an array of integers
Output: an integer (the number of sawtooth subarrays)

2 ≤ arr.length ≤ 10⁵

−10⁹ ≤ arr[i] ≤ 10⁹

Output: integer64 (because the number of subarrays can be large)

"""


def sum_of_sawtooth_subarrays(array):
    # early exit
    if len(array) == 1:
        return 1
    # create a left pointer
    left = 0 
    # create a windows sum variable 
    win_sum = 0 
    # iterate through the length of array
    for right in range(len(array)):
        # compare current value to previous 
        if right > 0 and (array[right - 1] % 2) != (array[right] % 2):
            win_sum += right - left + 1
        else:
            left = right
            win_sum += 1
            
    return win_sum
            



# Sawtooth subarray count — test cases (use print)

def run_tests(solution):
    tests = [
        # (arr, expected)
        ([5], 1),                             # single element
        ([1, 3, 5, 7, 9], 5),                  # all odd -> only singletons
        ([2, 4, 6, 8], 4),                     # all even -> only singletons
        ([1, 2], 3),                           # [1],[2],[1,2]
        ([2, 1], 3),                           # [2],[1],[2,1]
        ([1, 2, 1, 2, 1], 15),                 # fully alternating -> all subarrays
        ([1, 2, 3, 7, 6, 5], 12),              # break at (3,7) both odd
        ([1, 2, 4, 5], 6),                     # break at (2,4) both even
        ([0, 1, 2, 3, 4], 15),                 # 0 even, then perfect alternation -> all
        ([-1, 2, -3, 4], 10),                  # negatives: odd/even alternation -> all
        ([10, 11, 12, 14, 15], 9),             # break at (12,14) both even
        ([1, 2, 2, 1], 6),                     # break at (2,2) both even
        ([7, 8, 9, 10, 11, 12], 21),           # fully alternating -> all (n=6 => 21)
        ([1, 1, 2, 3], 7),                     # break at (1,1) both odd
        ([2, 3, 5, 7, 8], 7),                  # breaks at (5,7) odd-odd
    ]

    for arr, expected in tests:
        got = solution(arr)
        print(f"arr={arr} -> got={got}, expected={expected}")

# After you write your function `solution(arr)`, run:

if __name__ == "__main__":
    run_tests(sum_of_sawtooth_subarrays)
    
    

