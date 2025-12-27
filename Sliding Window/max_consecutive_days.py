"""
# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Longest Period At Most K Distinct

# We are given an array of strings, `best_seller`, where `best_seller[i]` is the title of the most sold book for day `i`, and a number `k ≥ 1`.

# Find the maximum consecutive days with at most `k` **distinct** best-selling books.

# Example 1:
# best_seller = ["book1", "book1", "book2", "book1", "book3", "book1"]
# k = 2

# Output: 4
# The subarray ["book1", "book1", "book2", "book1"] contains only 2 distinct titles

# Example 2:
# best_seller = ["book1", "book2", "book3"]
# k = 1

# Output: 1
# Each day has a different best seller

# Example 3:
# best_seller = ["book1", "book1", "book1"]
# k = 2

# Output: 3
# The entire array has only 1 distinct title

# Constraints:

# - `0 <= len(best_seller) <= 10^6`
# - `1 <= k <= len(best_seller)`
# - `1 <= len(best_seller[i]) <= 100`
"""

def max_consecutive_days(best_seller, k):
    # create left pointer 
    left = 0 
    # create max days 
    max_days = 0
    # create a hashmap to track counts
    counter = {} 
    # iterate through the entire array 
    for right in range(len(best_seller)):
        # increase counts
        counter[best_seller[right]] = counter.get(best_seller[right], 0) + 1
        while len(counter) > k:
            counter[best_seller[left]] -= 1 
            if counter[best_seller[left]] == 0:
                del counter[best_seller[left]]
            left += 1 

        # get the current window 
        curr_window = right - left + 1 
        max_days = max(curr_window, max_days)

    # lastly return max days 
    return max_days

def run_tests():
  tests = [
      # Example from the book
      (["book1", "book1", "book2", "book1", "book3", "book1"], 2, 4),
      # Edge case - empty array
      ([], 1, 0),
      # Edge case - k=1
      (["book1", "book2", "book1"], 1, 1),
      # Edge case - k=len(best_seller)
      (["book1", "book2", "book3"], 3, 3),
      # Edge case - all same book
      (["book1", "book1", "book1"], 1, 3),
  ]
  for best_seller, k, want in tests:
    got = max_consecutive_days(best_seller, k)
    print(got == want, f"\nmax_at_most_k_distinct({best_seller}, {k}): got: {got}, want {want}\n")

run_tests()
