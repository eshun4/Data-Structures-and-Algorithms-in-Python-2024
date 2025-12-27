"""
Implement:

def longest_substring_at_most_k_distinct(s: str, k: int) -> int:
    ...


Rules:

If k == 0: return 0

Use variable-length sliding window + count dict

Return max length

Paste your code and I’ll test it on:

"eceba", 2 -> 3

"aa", 1 -> 2

"a", 0 -> 0

"abc", 2 -> 2
"""

def longest_substring_at_most_k_distinct(s: str, k: int) -> int:
    # early exit
    if k == 0:
        return 0 
    # create count hashmap
    count = {}
    
    # create left pointer
    left = 0 
    best = 0 
    
    # iterate through string with right pointer
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1 
        
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        
        best = max(best, right - left + 1)
            
    return best

def test_longest_substring_at_most_k_distinct():
    # Given examples / core sanity
    assert longest_substring_at_most_k_distinct("eceba", 2) == 3   # "ece"
    assert longest_substring_at_most_k_distinct("aa", 1) == 2      # "aa"
    assert longest_substring_at_most_k_distinct("a", 0) == 0
    assert longest_substring_at_most_k_distinct("abc", 2) == 2     # "ab" or "bc"

    # Edge cases
    assert longest_substring_at_most_k_distinct("", 1) == 0
    assert longest_substring_at_most_k_distinct("", 0) == 0
    assert longest_substring_at_most_k_distinct("a", 1) == 1
    assert longest_substring_at_most_k_distinct("a", 5) == 1       # k > distinct count
    assert longest_substring_at_most_k_distinct("ab", 5) == 2      # k > distinct count

    # Repeats / patterns
    assert longest_substring_at_most_k_distinct("aaaaa", 1) == 5   # all same char
    assert longest_substring_at_most_k_distinct("abababab", 2) == 8
    assert longest_substring_at_most_k_distinct("abcabcabc", 2) == 2  # can't reach 3 w/ only 2 distinct

    # Tricky: lots of alternating distincts
    assert longest_substring_at_most_k_distinct("abacabad", 2) == 3    # "aba", "aca", "aba"
    assert longest_substring_at_most_k_distinct("dvdf", 3) == 4        # k=3 allows all 3 distincts -> whole string
    assert longest_substring_at_most_k_distinct("dvdf", 2) == 3        # "vdf"

    print("All tests passed!")


if __name__ == "__main__":
    test_longest_substring_at_most_k_distinct()
