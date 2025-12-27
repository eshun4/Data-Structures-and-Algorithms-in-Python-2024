
"""
Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# Most Sales In K Days

Given the array `sales` and a number `k` with `1 ≤ k ≤ len(sales)`, find the most sales in any k-day period.

Return the first day of that period (days start at `0`). If there are multiple k-day periods with the most sales, return the first day of the first one.

Example 1: sales = [8, 1, 3, 7], k = 2
Output: 2
The subarray of length 2 with maximum sum is [3, 7], which starts at index 2.

Example 2: sales = [5, 10, 15, 5], k = 1
Output: 2
The day with most sales is day 2 with 15 sales.

Example 3: sales = [1, 2, 3], k = 3
Output: 0
The only valid period is the entire array.

Constraints:

- The length of `sales` is at most `10^6`
- Each element in `sales` is a non-negative integer less than `10^3`
- `1 ≤ k ≤ len(sales)`

"""
def most_sales_in_k_days(sales, k):
    if k > len(sales):
       return 0
    current_sum = 0 #keeps track of the current sum
    best_sum = -float('inf')
    left = 0
    best_left = 0 
    for right in range(len(sales)):
        current_sum += sales[right]

        while right - left + 1 > k:
           current_sum -= sales[left]
           left += 1 

        
        if right - left + 1 == k and current_sum > best_sum:
           best_left = left
           best_sum = current_sum
    return best_left 
    
    
def run_tests():
    tests = [
      # Example from the book
      ([8, 1, 3, 7], 2, 2),
      # Edge case - k=1
      ([5, 10, 15, 5], 1, 2),
      # Edge case - k=len(sales)
      ([1, 2, 3], 3, 0),
      # Edge case - multiple valid answers, return first
      ([10, 5, 10], 2, 0),]
    for sales, k, want in tests:
        got = most_sales_in_k_days(sales, k)
        print(f"most_sales_in_k_days({sales}, {k}): got {got}, want {want}")
        assert got == want, f"\nmost_sales_in_k_days({sales}, {k}): got: {got}, want {want}\n"
    print("All tests passed!")

run_tests()
