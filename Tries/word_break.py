"""
LeetCode Problem: Word Break

Given a string `s` and a dictionary of strings `wordDict`, return true if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- `s` and `wordDict[i]` consist of only lowercase English letters.
"""


from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word):
        # get the root of the Trie
        temp = self.root
        # iterate through every character in the word
        for char in word:
            if char not in temp.children:
                temp.children[char] = Node(char)
            # ELse move to the next node
            temp = temp.children[char]
        # Lastly set last not to True
        temp.is_terminal = True

    def search(self, s, start):
        # get root of the Trie
        temp = self.root
        # itearate through each character and check if its in the children nodes
        for i in range(start, len(s)):
            char = s[i]
            if char not in temp.children:
                return None
            # Else move to the next one
            temp = temp.children[char]
            # when its not found
            if temp.is_terminal:
                yield i + 1

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create Object
        trie_node = Trie()
        for char in wordDict:
            trie_node.insert(char)

        # use dp
        # get length of n
        n = len(s)
        # create dp table
        dp = [False] * (n + 1)
        dp[0] = True # when the string is empty

        for i in range(n):
            if dp[i]:
                # CHeck substring starting from index i
                for end in trie_node.search(s, i):
                    dp[end] = True

        # return dp[n - 1]
        return dp[n]
    
    
def main():
    # Example usage
    s = "leetcode"
    wordDict = ["leet", "code"]
    solution = Solution()
    result = solution.wordBreak(s, wordDict)
    print("Can the string be segmented?", result)  # Output: True
    
    # Another example
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    result2 = solution.wordBreak(s2, wordDict2)
    print("Can the string be segmented?", result2)  # Output: True
    
    # Another example
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    result3 = solution.wordBreak(s3, wordDict3)
    print("Can the string be segmented?", result3)  # Output: False
    
if __name__ == "__main__":
    main()