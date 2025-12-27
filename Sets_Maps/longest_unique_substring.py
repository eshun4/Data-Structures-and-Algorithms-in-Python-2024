"""
Implement:

def length_of_longest_unique_substring(s: str) -> int:
    ...


Rules:

Use sliding window with left, right, and a set

While-loop to shrink when duplicate appears

Return the max length
"""

def length_of_longest_unique_substring(s: str) -> int:
    left = 0 #left pointer
    seen = set()
    best_length = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1 #left pointer moves right
            
        seen.add(s[right])
        cur_best =  right - left + 1
        if cur_best > best_length:
            best_length = cur_best
    return best_length
            

def _check(s: str, expected: int):
    got = length_of_longest_unique_substring(s)
    print(got == expected, f'Input: {s} | expected {expected}, got {got}')


def test_empty_string():
    _check("", 0)


def test_single_character():
    _check("a", 1)


def test_all_unique_characters():
    _check("abcdef", 6)


def test_all_duplicate_characters():
    _check("aaaa", 1)


def test_mixed_duplicates():
    _check("abcabcbb", 3)


def test_with_space_and_special_chars():
    # "au out" -> longest unique substring is " out" => 4
    _check("au out", 4)


def test_long_unique_at_end():
    _check("aabcdefg", 7)


def test_long_unique_at_start():
    _check("abcdefgg", 7)


def test_two_characters():
    _check("ab", 2)


def test_two_same_characters():
    _check("aa", 1)


if __name__ == "__main__":
    test_empty_string()
    test_single_character()
    test_all_unique_characters()
    test_all_duplicate_characters()
    test_mixed_duplicates()
    test_with_space_and_special_chars()
    test_long_unique_at_end()
    test_long_unique_at_start()
    test_two_characters()
    test_two_same_characters()
    print("All tests passed!")
