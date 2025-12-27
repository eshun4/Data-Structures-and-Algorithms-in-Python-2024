"""
# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Maximum With At Most 3 Bad Days

# Given an array `sales`, where `sales[i]` is the number of sales on the `i`-th day, find the most consecutive days with at most `3` bad days.

# A _bad day_ is a day with fewer than `10` sales.

# Example 1: sales = [0, 14, 7, 9, 0, 20, 10, 0, 10]
# Output: 6.
# There are two 6-day periods with at most 3 bad days:
#   - [14, 7, 9, 0, 20, 10]
#   - [9, 0, 20, 10, 0, 10]

# Example 2: sales = [10, 10, 10]
# Output: 3. All days are good days.

# Example 3: sales = [5, 5, 5, 5]
# Output: 3. We can include at most 3 bad days.

# Constraints:

# - `0 <= len(sales) <= 10^5`
# - `0 <= sales[i] <= 10^3`
"""


def most_days_with_3_bad_days_at_most(sales):
    # create best window
    best = 0 
    # create left pointer
    left = 0 
    # keep track of the number of bad days
    num_of_bad_days = 0
    # itearate through the sales
    for right in range(len(sales)):
        if sales[right] < 10:
            while num_of_bad_days >= 3:
                if sales[left] < 10:
                    num_of_bad_days -= 1
                left += 1
            num_of_bad_days += 1
        curr_window = right - left + 1
        best = max(curr_window, best)

    return best

def run_tests():
      tests = [
      # Example from the book
      ([0, 14, 7, 9, 0, 20, 10, 0, 10], 6),
      # Edge case - empty array
      ([], 0),
      # Edge case - single element
      ([5], 1),
      # all good days
      ([10, 11, 12], 3),
      # all bad days
      ([1, 2, 3], 3),
      # exactly 3 bad days
      ([5, 10, 5, 10, 5], 5),
      # More than 3 bad days
      ([5, 10, 5, 5, 10, 5], 5),
  ]
      for sales, want in tests:
          got = most_days_with_3_bad_days_at_most(sales)
          print(got == want, f"\nmax_at_most_3_bad_days({sales}): got: {got}, want {want}\n")



def main():
    run_tests()
    

if __name__ == "__main__":
    main()

