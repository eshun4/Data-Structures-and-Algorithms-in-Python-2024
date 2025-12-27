"""
We are given an array, best_seller, with the title of the most sold book for each day over a given period. We are also given a number k with 1 ≤ k ≤ len(sales).

We need to return whether there is any k-day period where each day has a different best-selling title.


Example 1:
best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4",
"book3"]
k = 3

Output: True
There is a 3-day period without a repeated value: ["book2", "book3", "book4"]

Example 2:
best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4",
"book3"]
k = 4

Output: False
There are no 4-day periods without a repeated value

Example 3:
best_seller = ["book1", "book2", "book3"]
k = 3

Output: True
The entire array has no repeated values
Constraints:

The length of best_seller is at most 10^6
Each book title has length at most 100
1 <= k <= len(best_seller)
"""


def best_seller_streak(best_seller, k) -> bool:
    # create variable for left pointer
    left = 0
    # create seen dictionary
    seen = {}

    # iterate through the array of books
    for right in range(len(best_seller)):
        right_book = best_seller[right]
        seen[right_book] = seen.get(right_book, 0) + 1 

        if right - left + 1 > k:
            left_book = best_seller[left]
            seen[left_book] -= 1 
            if seen[left_book] == 0:
                del seen[left_book]
            left += 1
        
        # if the books in seen are unique and if the window size is equal to k
        if right - left + 1 == k and len(seen) == k:
            return True 
    return False 


def run_tests():
    tests = [
      # Example 1 from the book
        (["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"], 3, True),
      # Example 2 from the book
      (["book3", "book1", "book3", "book3", "book2",
       "book3", "book4", "book3"], 4, False),
      # Edge case - k=1
      (["book1", "book2"], 1, True),
      # Edge case - k=len(best_seller)
      (["book1", "book2", "book3"], 3, True),
      # no unique sequence possible
      (["book1", "book1", "book1"], 2, False),]
    for best_seller, k, want in tests:
        got = best_seller_streak(best_seller, k)
        print(got == want, f"\nhas_unique_k_days({best_seller}, {k}): got: {got}, want {want}\n")
    
    print("all tests passed!")
        

if __name__ == "__main__":
    run_tests()
