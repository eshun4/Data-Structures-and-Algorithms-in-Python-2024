"""
# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Palindrome Check

# Given a string `s`, return whether `s` is a _palindrome_. A palindrome is a string that reads the same forward and backward.

# Example 1: s = "level"
# Output: true

# Example 2: s = "naan"
# Output: true

# Example 3: s = "hello"
# Output: false

# Constraints:

# - The length of s is at most 10^6
# - s consists of lowercase English letters

"""
def palindrome(s):
    # create pointers 
    left, right = 0, len(s) - 1
    # itearet while left is less than right 
    while left < right:
        if s[left] != s[right]:
            return False 
        left += 1 
        right -= 1 
    return True


def run_tests():
  tests = [
      # Example from the book
      ("level", True),
      ("naan", True),
      # Additional test cases
      ("", True),
      ("a", True),
      ("ab", False),
      ("abc", False),
      ("abba", True),
      ("abcba", True),
  ]
  for s, want in tests:
    got = palindrome(s)
    print(got == want, f"\npalindrome({s}): got: {got}, want: {want}\n")

run_tests()


