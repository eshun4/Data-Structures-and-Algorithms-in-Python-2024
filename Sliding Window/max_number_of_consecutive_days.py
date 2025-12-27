"""

# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Ad Campaign With Small Boosts

# Imagine that you have a little bookstore. We have an array, `projected_sales`, with the projected number of sales per day in the future.

# We are trying to pick `k` days for an advertising campaign, which we expect to boost the sales on those specific days by `5` sales. **You cannot boost the same day more than once.**

# If we pick the days for the advertising campaign correctly, what is the maximum number of consecutive good days in a row we can get?

# A _good day_ is a day with at least `10` sales.

# Example 1: projected_sales = [8, 4, 8], k = 3
# Output: 1. We can boost all 3 days, resulting in [13, 9, 13] projected sales.
# The max consecutive good days is 1.

# Example 2: projected_sales = [10, 5, 8], k = 1
# Output: 2. We should boost day 1, resulting in [10, 10, 8] projected sales.

# Example 3: projected_sales = [8, 8, 8], k = 3
# Output: 3. We can boost all days to reach 13 sales each.

# Constraints:

# - `0 <= len(projected_sales) <= 10^5`
# - `0 <= projected_sales[i] <= 10^3`
# - `0 <= k <= len(projected_sales)`
"""


def max_number_of_consecutive_days(sales, k):
    # create left pointer
    left = 0 
    # create a best tracker
    best = 0
    # create a number of boostable days count 
    boostable_days = 0
    # iterate through the range of sales 
    for right in range(len(sales)):
        if sales[right] < 10: #and sales[right] > 5:
            if sales[right] < 5:
                boostable_days = 0
                left = right + 1
        if sales[right] >= 5 and sales[right] <= 9:
            boostable_days += 1

            while boostable_days > k:
                if sales[left] < 10 and sales[left] >= 5:
                    boostable_days -= 1
                left += 1

        curr_window = right - left + 1 
        best = max(curr_window, best)

    return best


def run_tests():
  tests = [
      # Example 1 from the book
      ([8, 4, 8], 3, 1),
      # Example 2 from the book
      ([10, 5, 8], 1, 2),
      ([8, 8, 8], 3, 3),
      # Example with mix of values
      ([4, 8, 12, 3, 9], 2, 2),
      # Edge case - empty array
      ([], 1, 0),
      # Edge case - k=0
      ([5, 10, 5], 0, 1),
      # Edge case - all values between 5-9
      ([7, 8, 9], 3, 3),
      # Edge case - values below 5 break sequence
      ([8, 4, 8], 2, 1),
  ]
  for projected_sales, k, want in tests:
    got = max_number_of_consecutive_days(projected_sales, k)
    print(got == want, f"\nmax_consecutive_good_days_with_small_boost({projected_sales}, {k}): got: {got}, want {want}\n")

def main():
    run_tests()

if __name__ == "__main__":
    main()