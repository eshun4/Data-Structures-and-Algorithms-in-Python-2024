"""
# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Max Subarray Sum

# Given a non-empty array `arr` of integers (which can be negative), find the non-empty subarray with the maximum sum and return its sum.

# Example 1: arr = [1, 2, 3, -2, 1]
# Output: 6. The subarray with the maximum sum is [1, 2, 3].

# Example 2: arr = [1, 2, 3, -2, 7]
# Output: 11. The subarray with the maximum sum is the whole array.

# Example 3: arr = [1, 2, 3, -8, 7]
# Output: 7. The subarray with the maximum sum is [7].

# Example 4: arr = [-2, -3, -4]
# Output: -2. The subarray cannot be empty.

# Constraints:

# - `1 <= len(arr) <= 10^5`
# - Each element in `arr` is an integer between `-10^6` and `10^6`

"""


def max_subarray_sum(sales):
    # create left pointer
    left = 0 
    # create current sum
    cur_sum = 0 
    best = -float('inf')
    # iterate through the array
    for right in range( len(sales)):
        if cur_sum < 0:
            cur_sum = left
        cur_sum += sales[right]
        best = max(best, cur_sum)
    return best

def run_tests():
    tests = [
        # Example 1 from the book
        ([1, 2, 3, -2, 1], 6),
        # Example 2 from the book
        ([1, 2, 3, -2, 7], 11),
        # Example 3 from the book
        ([1, 2, 3, -8, 7], 7),
        # Example 4 from the book
        ([-2, -3, -4], -2),
        # Edge case - single element
        ([5], 5),
        # Edge case - all positive
        ([1, 2, 3], 6),
    ]
    for arr, want in tests:
        got = max_subarray_sum(arr)
        print(got == want, f"\nmax_subarray_sum({arr}): got: {got}, want {want}\n")

if __name__ == "__main__":
    run_tests()
         
        