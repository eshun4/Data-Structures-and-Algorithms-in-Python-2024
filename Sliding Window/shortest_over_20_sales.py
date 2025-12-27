"""

# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Shortest Period With Over 20 Sales

# Given an array, `sales`, where `sales[i]` is the number of sales on day `i`, find the shortest period of time with over 20 sales, or `-1` if there isn't any.

# Example 1: sales = [5, 10, 15, 5, 10]
# Output: 2. The subarray [10, 15] has over 20 sales.

# Example 2: sales = [5, 10, 4, 5, 10]
# Output: 4. [5, 10, 4, 5] and [10, 4, 5, 10] have over 20 sales.

# Example 3: sales = [5, 5, 5, 5]
# Output: -1. There is no subarray with more than 20 sales.

# Constraints:

# - `0 <= len(sales) <= 10^5`
# - `0 <= sales[i] <= 10^3`
"""



def shortest_over_20_sales(sales):
    # create left pointer
    left = 0 
    # min days starts from inf 
    min_days = float("inf")
    # create current sum 
    curr_sum = 0 
    # iterate through the range of values
    for right in range(len(sales)):
        curr_sum += sales[right]

        while curr_sum > 20:
            
            curr_wind = right - left + 1 
            min_days = min(min_days, curr_wind)

            curr_sum -= sales[left] 
            left += 1 
        
    if min_days == float('inf'):
        min_days = -1 
        
    # return min days 
    return min_days

def run_tests():
  tests = [
      # Example 1 from the book
      ([5, 10, 15, 5, 10], 2),
      # Example 2 from the book
      ([5, 10, 4, 5, 10], 4),
      # Example 3 from the book
      ([5, 5, 5, 5], -1),
      # Edge case - empty array
      ([], -1),
      # Edge case - single element over 20
      ([21], 1),
      # Edge case - exactly 20 sales not enough
      ([10, 10], -1),
  ]
  for sales, want in tests:
    got = shortest_over_20_sales(sales)
    print(got == want, f"\nshortest_over_20_sales({sales}): got: {got}, want {want}\n")

run_tests()

