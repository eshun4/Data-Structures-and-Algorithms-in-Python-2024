"""
# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # String Join

# Without using a built-in string join method, implement a `join(arr, s)` method, which receives an array of strings, `arr`, and a string, `s`, and returns a single string consisting of the strings in `arr` with `s` in between them.

# Example 1: arr = ["join", "by", "space"], s = " "
# Output: "join by space"

# Example 2: arr = ["b", "", "k", "", "p", "r n", "", "d", "d!!"], s = "ee"
# Output: "beeeekeeeepeer neeeedeed!!"

# Example 3: arr = [], s = "x"
# Output: ""

# If strings in your language are immutable, assume that you have access to a function `array_to_string(arr)`, which takes an array of individual characters and returns a string with those characters in `O(len(arr))` time.

# Constraints:

# - 0 <= s.length <= 500
# - 0 <= arr.length <= 10^5
# - 0 <= arr[i].length <= 10^5
# - the sum of the lengths of the strings in `arr` is at most 10^5
"""


def join(arr, s):
    # if arr is empty
    if not arr:
        return ""
    # create a result array buffer 
    res = []
    # iterate through the words in array
    for i in range(len(arr)):
        if i != 0:
            for c in s:
                res.append(c)
        for c in arr[i]:
            res.append(c)
    # return arr passed in function
    return array_to_string(res)

def run_tests():
  tests = [
      # Example 1 from the book
      (["join", "by", "space"], " ", "join by space"),
      # Example 2 from the book
      (["b", "", "k", "", "p", "r n", "", "d", "d!!"],
          "ee", "beeeekeeeepeer neeeedeed!!"),
      # Edge case - empty arrays
      ([], "x", ""),
      ([], "", ""),
      ([], "long separator", ""),
      # Edge case - single element arrays
      (["a"], "x", "a"),
      ([""], "x", ""),
      (["multiple words"], "x", "multiple words"),
      # two element arrays
      (["a", "b"], "", "ab"),
      (["a", "b"], " ", "a b"),
      (["", ""], ",", ","),
      # Edge case - empty strings in array
      (["", "", ""], ",", ",,"),
      (["hello", "", "world"], " ", "hello  world"),
      # special characters
      (["\n", "\t"], ",", "\n,\t"),
      (["tab", "separated"], "\t", "tab\tseparated"),
      # long separators
      (["short", "strings"], "very long separator",
       "shortvery long separatorstrings"),
      # mixed content
      (["123", "abc", "!@#", "   "], "|", "123|abc|!@#|   "),
      # whitespace handling
      (["  leading", "trailing  ", "  both  "],
          "|", "  leading|trailing  |  both  "),
      # numbers and special chars
      (["123", "456"], "-", "123-456"),
      (["!@#", "$%^"], "&", "!@#&$%^"),
  ]
  for arr, s, want in tests:
    got = join(arr, s)
    print(got == want, f"\njoin({arr}, {s}): got: {got}, want: {want}\n")


def array_to_string(arr):
    """
    Converts an array of characters to a string in O(len(arr)) time.
    
    Args:
        arr: A list of individual characters
        
    Returns:
        A string consisting of the characters in arr
    """
    return ''.join(arr)


def main():
    run_tests()
    
if __name__ == "__main__":
    main()