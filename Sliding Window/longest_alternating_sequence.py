"""

# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Longest Alternating Sequence

# Given the array `sales`, where `sales[i]` is the number of sales on the `i`-th day, find the longest sequence of days alternating between good days and bad days.

# A _good day_ is a day with at least `10` sales.
# A _bad day_ is a day with fewer than `10` sales.

# Example 1: sales = [8, 9, 20, 0, 9]
# Output: 3. The only good day is day 2, so the subarray [9, 20, 0] alternates from bad to good to bad.

# Example 2: sales = [0, 0, 0]
# Output: 1. Every day is bad, so we cannot find any pair of consecutive days that alternate.

# Example 3: sales = [5, 10, 5, 10]
# Output: 4. The entire array alternates between bad and good days.

# Constraints:

# - `0 <= len(sales) <= 10^5`
# - `0 <= sales[i] <= 10^3`

"""


def longest_alternating_sequence(sales):
    # create left pointer
    left = 0 
    # create best 
    best = 0 #since we dont have to worry about negative vals
    # iterate through sales
    for right in range(len(sales)):
        if left == right or (sales[right - 1] < 10) != (sales[right] < 10):
            curr_best = right - left + 1 
            best = max(best, curr_best)  
        else:
            left = right 
    return best

def run_tests():
    tests = [
      # Example 1 from the book
      ([8, 9, 20, 0, 9], 3),
      # Example 2 from the book
      ([0, 0, 0], 1),
      # Edge case - empty array
      ([], 0),
      # Edge case - single element
      ([10], 1),
      # perfect alternation
      ([5, 10, 5, 10], 4),
      # all good days
      ([10, 11, 12], 1),]
    for sales, want in tests:
        got = longest_alternating_sequence(sales)
        print(got == want, f"\nlongest_alternating_sequence({sales}): got: {got}, want {want}\n")

run_tests()