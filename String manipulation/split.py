"""
# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # String Split

# Without using a built-in string split method, implement a `split(s, c)` method, which receives a string `s` and a character `c` and splits `s` at each occurrence of `c`, returning a list of strings.

# Example 1: s = "split by space", c = ' '
# Output: ["split", "by", "space"]

# Example 2: s = "beekeeper needed", c = 'e'
# Output: ["b", "", "k", "", "p", "r n", "", "d", "d"]

# Example 3: s = "/home/./..//Documents/", c = '/'
# Output: ["", "home", ".", "..", "", "Documents", ""]

# Example 4: s = "", c = '?'
# Output: []

# Constraints:

# - The length of the input string is at most 10^6
# - The delimiter is a single character
"""



def split(s, t):
    # do first check what happens when s is empty for an early exit
    if not s:
        return []
    # crete a result and curr array
    res, cur = [], []
    # iterte through the characters in the string 
    for char in s:
        if char == t:
            res.append("".join(cur))
            # reset the current length of string to a new empty array
            cur = []
        else:
            cur.append(char)
    res.append("".join(cur))
    # return the results 
    return res


def run_tests():
  tests = [
      # Example 1 from the book
      ("split by space", ' ', ["split", "by", "space"]),
      # Example 2 from the book
      ("beekeeper needed", 'e', ["b", "", "k", "", "p", "r n", "", "d", "d"]),
      # Example 3 from the book
      ("/home/./..//Documents/", '/',
          ["", "home", ".", "..", "", "Documents", ""]),
      # Example 4 from the book
      ("", '?', []),
      # Edge case - empty string with various delimiters
      ("", ' ', []),
      ("", '\n', []),
      ("", '', []),
      # Edge case - single character string
      ("a", 'a', ["", ""]),
      ("a", 'b', ["a"]),
      # Edge case - no splits
      ("hello", 'x', ["hello"]),
      ("hello", '?', ["hello"]),
      # Edge case - all splits
      ("aaa", 'a', ["", "", "", ""]),
      # Edge case - special characters
      ("\n\n\n", '\n', ["", "", "", ""]),
      ("tab\tseparated\ttext", '\t', ["tab", "separated", "text"]),
      # Edge case - consecutive delimiters
      ("one,,two,,,three", ',', ["one", "", "two", "", "", "three"]),
      # Edge case - delimiter at start/end
      (",start,middle,end,", ',', ["", "start", "middle", "end", ""]),
      # Edge case - mixed length strings
      ("short,medium string,very very long string", ',', [
          "short", "medium string", "very very long string"]),
      # Edge case - whitespace handling
      ("  leading space", ' ', ["", "", "leading", "space"]),
      ("trailing space  ", ' ', ["trailing", "space", "", ""]),
      # Edge case - numbers and special chars
      ("123,456,789", ',', ["123", "456", "789"]),
      ("!@#$%", '@', ["!", "#$%"]),
  ]
  for s, c, want in tests:
    got = split(s, c)
    print(got == want, f"\nsplit({s}, {c}): got: {got}, want: {want}\n")

run_tests()



def main():
    pass


if __name__ == "__main__":
    main()