"""
# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Shortest With All Letters

# Given a string, `s1`, and a shorter but non-empty string, `s2`, return the length of the shortest substring of `s1` that has every letter in `s2` at least as many times as they appear in `s2`. If there is no such substring, return `-1`.

# Example 1: s1 = "helloworld", s2 = "well"
# Output: 5. The substring "ellow" in s1 has all the letters in s2.

# Example 2: s1 = "helloworld", s2 = "weelll"
# Output: -1. s1 does not have 2 e's.

# Constraints:

# - `1 <= len(s2) < len(s1) <= 10^5`
# - All characters are lowercase English letters
"""


def shortest_with_all_letters(s1, s2):
    # create a left pointer 
    left = 0 
    # create a min window variable to track the min window we have so far
    min_window = float("inf")
    # create a hashmap to count the number of elements in s2 
    need = {}
    # count the number of elements in s2
    for i in range(len(s2)):
        need[s2[i]] = need.get(s2[i], 0) + 1 
    # create another hashmap for the elements we have so far
    have = {}
    # create a formed variable
    formed = 0
    # iterate through the characters in s1 and check if their frequencies are same esle add it to have 
    for right in range(len(s1)):
        if s1[right] in need:
            have[s1[right]] = have.get(s1[right], 0) + 1 
            if have[s1[right]] == need[s1[right]]:
                formed += 1
            # the window is valid when have is directly equal to need
            while formed == len(need):
                min_window = min(min_window, right - left + 1)
                if s1[left] in have:
                    if s1[left] in need:
                        have[s1[left]] -= 1 
                        if have[s1[left]] < need[s1[left]]:
                            formed -= 1
                        if have[s1[left]] == 0:
                            del have[s1[left]]
                left += 1
    # return minimum window
    return min_window if min_window != float("inf") else -1


def run_tests():
  tests = [
      # Example 1 from the book
      ("helloworld", "well", 5),
      # Example 2 from the book
      ("helloworld", "weelll", -1),
      # Edge case - s2 is single character
      ("hello", "l", 1),
      # s2 not in s1
      ("hello", "z", -1),
  ]
  for s1, s2, want in tests:
    got = shortest_with_all_letters(s1, s2)
    print(got == want, f"\nshortest_with_all_letters({s1}, {s2}): got: {got}, want {want}\n")

run_tests()