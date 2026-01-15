"""


# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Smallest Range With K Elements

# Given an array of integers, `arr`, and a number `k` with `1 ≤ k ≤ len(arr)`, return a pair of numbers `[low, high]`, with `low ≤ high`, representing the smallest range such that there are at least `k` elements in `arr` with values at least `low` and at most `high`.

# If there are multiple valid answers, return any of them.

# Example 1: arr = [1, 2, 5, 7, 8], k = 3
# Output: [5, 8]
# The range has 3 elements in arr (5, 7, and 8).
# It is smaller than other ranges with 3 elements, such as [1, 5], because 8-5 < 5-1.

# Example 2: arr = [5, 5, 2, 2, 8, 8], k = 3
# Output: [2, 5]
# The range has 4 elements in arr (5, 5, 2, and 2).
# There is no smaller range with at least 3 elements.
# [5, 8] is also a valid answer.

# Example 3: arr = [0], k = 1
# Output: [0, 0]

# Constraints:

# - `1 <= k <= len(arr) <= 10^5`
# - `-10^9 <= arr[i] <= 10^9`

"""

def smallest_range_with_k_elements(arr, k):
    # sort array
    arr.sort()
    # create a left pointer 
    left = 0 
    # best so far
    best = float("inf")
    # create a result array
    result = []
    # iterate through the arr elements
    for right in range(len(arr)):

        while right - left + 1 >= k:
            curr_range = arr[right] - arr[left]
            if curr_range < best:
                best = curr_range
                result = [arr[left], arr[right]]
            left += 1

    return result


def run_tests():
  tests = [
      # Example 1 from the book
      ([1, 2, 5, 7, 8], 3, [5, 8]),
      # Example 2 from the book - both [2,5] and [5,8] are valid
      ([5, 5, 2, 2, 8, 8], 3, [2, 5]),
      # Example 3 from the book
      ([0], 1, [0, 0]),
      # Edge case - k=len(arr)
      ([1, 5, 10], 3, [1, 10]),
      # Edge case - all same number
      ([5, 5, 5], 2, [5, 5]),
  ]
  for arr, k, want in tests:
    got = smallest_range_with_k_elements(arr, k)
    # For this problem, there might be multiple valid answers
    # We check if the range contains at least k elements and is minimal
    count = sum(1 for x in arr if want[0] <= x <= want[1])
    print(count >= k, f"\nsmallest_range_with_k_elements({arr}, {k}): range {got} )contains fewer than {k} elements\n")
    print(got[1] - got[0] <= want[1] - \
        want[0], f"\nsmallest_range_with_k_elements({arr}, {k}): range {got} is larger than {want}\n")

run_tests()  


