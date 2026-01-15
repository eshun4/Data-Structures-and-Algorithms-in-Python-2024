"""

# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Smaller Prefixes

# Given an array of integers, `arr`, where the length, `n`, is even, return whether the following condition holds for every `k` in the range `1 ≤ k <= n/2`: "the sum of the first `k` elements is smaller than the sum of the first `2k` elements." If this condition is false for any `k` in the range, return `false`.

# Example 1: arr = [1, 2, 2, -1]
# Output: True. The prefix [1] has a smaller sum than the prefix [1, 2], and the prefix [1, 2] has a smaller sum than the prefix [1, 2, 2, -1]. The other prefixes have length > n/2.

# Example 2: arr = [1, 2, -2, 1, 3, 5]
# Output: False. The prefix [1, 2] has a larger sum than the prefix [1, 2, -2, 1].

# Constraints:

# - len(arr) is even
# - 0 ≤ len(arr) ≤ 10^6
# - -10^9 ≤ arr[i] ≤ 10^9

"""


def smaller_prefixes(arr):
    if not arr:
        return True
    # create small and fast pointers 
    sp, fp = 0, 0 
    # small sum and large sum
    small_sum, large_sum = 0, 0 
    while fp < len(arr):
        small_sum += arr[sp]
        large_sum += arr[fp] + arr[fp + 1]

        if small_sum >= large_sum:
            return False
        
        sp += 1
        fp += 2

    return True


def run_tests():
  tests = [
      # Example 1 from the book
      ([1, 2, 2, -1], True),
      # Example 2 from the book
      ([1, 2, -2, 1, 3, 5], False),
      # Additional test cases
      ([0, 3, 7, 12, 10, 5, 0, 1], True),
      ([], True),
      ([1, 2], True),
      ([2, 1], True),
      ([-2, 1, -4, 5, -3, 7], True),
      ([-2, 1, -14, 8, -3, 2], False),
  ]
  for arr, want in tests:
    got = smaller_prefixes(arr)
    print(got == want, f"\nsmaller_prefixes({arr}): got: {got}, want: {want}\n")

run_tests()