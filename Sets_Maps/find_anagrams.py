"""
Write:

def find_anagrams(s: str, p: str) -> list[int]:
    ...


Rules:

If len(p) > len(s): return []

Build need counts for p

Maintain window counts for a fixed-size window in s

When window size exceeds k, remove left char (decrement + delete if 0)

If window size == k and window == need, append left
"""


def find_anagrams(s: str, p: str) -> list[int]:
    # get k 
    k = len(p)
    # early exit
    if k > len(s):
        return []
    
    if k == 0:
        return []
    
    result = []
    # create a need and window hashmap
    need = {}
    window = {}
    matches = 0
    # build need counts for p
    for char in p:
        need[char] = need.get(char, 0) + 1
        
    # add elements to windoe
    left = 0 #left pointer 
    
    for right in range(len(s)):
        window[s[right]] = window.get(s[right], 0) + 1
        # if ch in need
        if s[right] in need:
            if window[s[right]] == need[s[right]]:
                matches += 1
            elif window[s[right]] == need[s[right]] + 1:
                matches -= 1
            
        # shrink if window size exceeds k
        if right - left + 1 > k:
            if s[left] in need:
                if window[s[left]] == need[s[left]]:
                    matches -= 1
                elif window[s[left]] == need[s[left]] + 1:
                    matches += 1
            
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
            
        # if window size == k and window == need
        if right - left + 1 == k and matches == len(need):
            result.append(left)
    return result
            
            
            
    
            
    

if __name__== "__main__":   
    def test_find_anagrams_basic():
        assert find_anagrams("cbaebabacd", "abc") == [0, 6]


    def test_find_anagrams_no_match():
        assert find_anagrams("abab", "xyz") == []


    def test_find_anagrams_single_char():
        assert find_anagrams("aaaaaaaaaa", "aa") == [0, 1, 2, 3, 4, 5, 6, 7, 8]


    def test_find_anagrams_pattern_longer_than_string():
        assert find_anagrams("abc", "abcd") == []


    def test_find_anagrams_empty_pattern():
        assert find_anagrams("abc", "") == []


    def test_find_anagrams_empty_string():
        assert find_anagrams("", "a") == []


    def test_find_anagrams_both_empty():
        assert find_anagrams("", "") == []


    def test_find_anagrams_single_match():
        assert find_anagrams("ab", "ab") == [0]


    def test_find_anagrams_pattern_equals_string():
        assert find_anagrams("abc", "abc") == [0]


    def test_find_anagrams_multiple_matches():
        assert find_anagrams("abab", "ab") == [0, 1, 2]


    # def test_find_anagrams_repeated_chars():
    #     assert find_anagrams("aabbcc", "ab") == [0, 1, 3]



    test_find_anagrams_basic()
    test_find_anagrams_no_match()
    test_find_anagrams_single_char()
    test_find_anagrams_pattern_longer_than_string()
    test_find_anagrams_empty_pattern()
    test_find_anagrams_empty_string()
    test_find_anagrams_both_empty()
    test_find_anagrams_single_match()
    test_find_anagrams_pattern_equals_string()
    test_find_anagrams_multiple_matches()
    # test_find_anagrams_repeated_chars()
    print("All tests passed!")