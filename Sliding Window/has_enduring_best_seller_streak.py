"""
Example 1:
best_seller = ["book3", "book1", "book3", "book3", "book2"]
k = 3

Output: False
No three consecutive days have the same best seller.

Example 2:
best_seller = ["book3", "book1", "book3", "book3", "book2"]
k = 2

Output: True
Days 3-4 have the same best seller "book3".

Example 3:
best_seller = ["book1", "book2", "book1"]
k = 2

Output: False
No two consecutive days have the same best seller.

Example 4:
best_seller = ["book1", "book1", "book1"]
k = 3

Output: True
The entire array has the same best seller.
"""


def has_enduring_best_seller_streak(best_seller, k):
    if k > len(best_seller):
        return False
    if k <= 1:
        return True

    left = 0
    for right in range(len(best_seller)):
        if right > 0 and best_seller[right] != best_seller[right - 1]:
            left = right  # start a new consecutive streak here

        if right - left + 1 == k:
            return True

    return False




def run_tests():
    tests = [
      # Example 1 from the book
      (["book3", "book1", "book3", "book3", "book2"], 3, False),
      # Example 2 from the book
      (["book3", "book1", "book3", "book3", "book2"], 2, True),
      (["book1", "book1", "book2", "book1"], 2, True),
      # Edge case - k=1
      (["book1", "book2"], 1, True),
      # Edge case - k=len(best_seller)
      (["book1", "book1", "book1"], 3, True),
      # no same sequence possible
      (["book1", "book2", "book1"], 2, False),]
    for best_seller, k, want in tests:
        got = has_enduring_best_seller_streak(best_seller, k)
        print(got == want, f"\nhas_enduring_best_seller_streak({best_seller}, {k}): got: {got}, want {want}\n")
        got = has_enduring_best_seller_streak(best_seller, k)
        print(got == want, f"\nhas_enduring_best_seller_streak({best_seller}, {k}): got: {got}, want {want}\n")


if __name__ == "__main__":
    run_tests()