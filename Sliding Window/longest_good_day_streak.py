"""
Given an array, sales, where sales[i] is the number of sales on the i-th day, find the most consecutive days with no bad days.

A bad day is a day with fewer than 10 sales.


Example 1: sales = [0, 14, 7, 12, 10, 20]
Output: 3. The subarray [12, 10, 20] has no bad days.

Example 2: sales = [10, 10, 10]
Output: 3. All days are good days.

Example 3: sales = [5, 5, 5]
Output: 0. There are no good days.
Constraints:

0 <= len(sales) <= 10^5
0 <= sales[i] <= 10^3
"""

def good_day_streak(sales):
    # early exit
    if not sales:
        return 0
    # create best Streak variable
    best = 0 
    # create left pointer 
    left = 0 
    for right in range(len(sales)):
        if sales[right] < 10:
            left = right + 1 
        curr_streak = right - left + 1 
        best = max(best, curr_streak)
    return best
        
 
if __name__ == "__main__":
    def run_tests():
      tests = [
      # Example from the book
      ([0, 14, 7, 12, 10, 20], 3),
      # Edge case - empty array
      ([], 0),
      # Edge case - all good days
      ([10, 11, 12], 3),
      # Edge case - all bad days
      ([1, 2, 3], 0),
      # alternating
      ([10, 5, 10, 5], 1),]
      for sales, want in tests:
          got = good_day_streak(sales)
          print(got == want, f"\nmax_no_bad_days({sales}): got: {got}, want {want}\n")
      print("all tests passed!")

run_tests()