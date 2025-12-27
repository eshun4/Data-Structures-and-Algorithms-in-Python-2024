"""
Write:

def has_all_distinct_window(s: str, k: int) -> bool:
    ...


Rules:

If k > len(s): return False

Maintain a sliding window of size k

Use a dict count

When window size hits k, check len(count) == k

Slide by decrementing s[left] and incrementing the new right char
"""


def has_all_distinct_window(s: str, k: int) -> bool:
    # create a hahmap
    count= {}
    # early exit
    if k > len(s):
        return False
    
    if k == 0:
        return True 

    left = 0
    # iterate through string with right pointer
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        
        # keep window size <= k
        if right - left + 1 > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        # wiondow is of size k
        if  right - left + 1 == k and len(count) == k:
            return True
    
    return False

if __name__ == "__main__":
    def test_all_distinct_characters():
        assert has_all_distinct_window("abcdef", 3) == True
        print("test_all_distinct_characters passed")

    def test_repeated_characters():
        assert has_all_distinct_window("aabcdef", 3) == True
        print("test_repeated_characters passed")

    def test_k_equals_length():
        assert has_all_distinct_window("abc", 3) == True
        print("test_k_equals_length passed")

    def test_k_greater_than_length():
        assert has_all_distinct_window("ab", 3) == False
        print("test_k_greater_than_length passed")

    def test_k_equals_zero():
        assert has_all_distinct_window("abc", 0) == True
        print("test_k_equals_zero passed")

    def test_empty_string():
        assert has_all_distinct_window("", 0) == True
        print("test_empty_string passed")

    def test_empty_string_k_positive():
        assert has_all_distinct_window("", 1) == False
        print("test_empty_string_k_positive passed")

    def test_single_character():
        assert has_all_distinct_window("a", 1) == True
        print("test_single_character passed")

    def test_all_same_characters():
        assert has_all_distinct_window("aaaa", 2) == False
        print("test_all_same_characters passed")

    def test_window_in_middle():
        assert has_all_distinct_window("aabcda", 3) == True
        print("test_window_in_middle passed")

    def test_no_distinct_window():
        assert has_all_distinct_window("aabbcc", 2) == True
        print("test_no_distinct_window passed")

    # Run all tests
    test_all_distinct_characters()
    test_repeated_characters()
    test_k_equals_length()
    test_k_greater_than_length()
    test_k_equals_zero()
    test_empty_string()
    test_empty_string_k_positive()
    test_single_character()
    test_all_same_characters()
    test_window_in_middle()
    test_no_distinct_window()
