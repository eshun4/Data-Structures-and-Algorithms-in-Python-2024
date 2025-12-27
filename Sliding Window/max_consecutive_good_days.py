"""
# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Ad Campaign Boost

# Imagine that you have a little bookstore. We have an array, `projected_sales`, with the projected number of sales per day in the future.

# We are trying to pick `k` days for an advertising campaign, which we expect to boost the sales on those specific days by at least `20`.

# If we pick the days for the advertising campaign correctly, what is the maximum number of consecutive good days in a row we can get?

# A _good day_ is a day with at least `10` sales.

# Example 1: projected_sales = [5, 0, 20, 0, 5], k = 2
# Output: 3.
# The only good day is day 2. We can boost:
#   - days 0 and 1,
#   - days 1 and 3, or
#   - days 3 and 4.
# For instance, if we boost days 0 and 1, the projected sales become:
# [25, 20, 20, 0, 5], with 3 consecutive good days.

# Example 2: projected_sales = [0, 10, 0, 10], k = 1
# Output: 3. We can boost day 2; boosting day 0 is suboptimal.

# Example 3: projected_sales = [5, 5, 5], k = 3
# Output: 3. We can boost all days to make them good days.

# Constraints:

# - `1 <= k <= len(projected_sales) <= 10^5`
# - `0 <= projected_sales[i] <= 10^3`


"""
def max_consecutive_good_days(sales, k):
    # create a pointer for left
    left = 0 
    # create a best to keep track of current window
    best = 0 
    # create a variable to track boostable days
    boostable_days = 0 
    # iterate through the sales 
    for right in range(len(sales)):
        if sales[right] < 10: 
            boostable_days += 1
            while boostable_days > k:
                if sales[left] < 10:
                    boostable_days -= 1
                left += 1
        curr_best = right - left + 1 
        best = max(best, curr_best) 
    
    return best

def run_tests():
  tests = [
      # Example 1 from the book
      ([5, 0, 20, 0, 5], 2, 3),
      # Example 2 from the book
      ([0, 10, 0, 10], 1, 3),
      # Edge case - k=len(projected_sales)
      ([5, 5, 5], 3, 3),
  ]
  for projected_sales, k, want in tests:
    got = max_consecutive_good_days(projected_sales, k)
    print(got == want, f"\nmax_consecutive_good_days({projected_sales}, {k}): got: {got}, want {want}\n")
    
def main():
    run_tests()

if __name__ == "__main__":
    main()