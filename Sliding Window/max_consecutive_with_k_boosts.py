"""
# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Boosting Days Multiple Times

# Imagine that you have a little bookstore. We have an array, `projected_sales`, with the projected number of sales per day in the future.

# We are doing an advertising campaign and have a total of `k` boosts that we can use on any of the days. We expect each boost to increase the sales on the chosen day by `1`. **You can boost the same day multiple times.**

# If we use the boosts correctly, what is the maximum number of consecutive good days in a row we can get?

# A _good day_ is a day with at least `10` sales.

# Example 1: projected_sales = [5, 5, 15, 0, 10], k = 12
# Output: 3
# We can reach 3 consecutive good days in two ways:
#   - boosting days 0 and 1 to reach 10 sales each, or
#   - boosting day 3 to reach 10 sales.

# Example 2: projected_sales = [5, 5, 15, 0, 10], k = 15
# Output: 4
# We can boost days 1 and 3 to reach 10 sales each.

# Example 3: projected_sales = [0, 0, 0], k = 29
# Output: 2
# We can use all boosts on days 0 and 1 to reach 10 sales each.

# Constraints:

# - `0 <= len(projected_sales) <= 10^5`
# - `0 <= projected_sales[i] <= 10^3`
# - `0 <= k <= 10^7`

"""
def max_consecutive_with_k_boosts(sales, k):
    # create left pointer 
    left = 0 
    # create max days
    max_days = 0 
    # iterate through the array 
    for i in range(len(sales)):
        # since good day is val >= 10 subtract 10 val from 10 and set to current val in arr. If val is less than 0 repalce with 0 
        curr_cost = max(0, 10 - sales[i])
        sales[i] = curr_cost

    # Next use two pointer technique to keep track of costs
    # create sumCosts variable 
    sumCost = 0 
    # iterate through sales 
    for right in range(len(sales)):
        sumCost += sales[right]

        while sumCost > k:
            sumCost -= sales[left]
            left += 1 

        curr_wind = right - left + 1
        max_days = max(curr_wind, max_days)

    # return the maximum number of days 
    return max_days


def run_tests():
  tests = [
      # Example 1 from the book
      ([5, 5, 15, 0, 10], 12, 3),
      # Example 2 from the book
      ([5, 5, 15, 0, 10], 15, 4),
      # Edge case - empty array
      ([], 5, 0),
      # Edge case - k=0
      ([5, 10, 5], 0, 1),
      # all values need max boost
      ([0, 0, 0], 30, 3),
      # all values need max boost
      ([0, 0, 0], 29, 2),
  ]
  for projected_sales, k, want in tests:
    got = max_consecutive_with_k_boosts(projected_sales, k)
    print(got == want, f"\nmax_consecutive_with_k_boosts({projected_sales}, {k}): got: {got}, want {want}\n")

run_tests()