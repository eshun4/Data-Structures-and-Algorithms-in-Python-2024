"""
Write:

def is_anagram(s: str, t: str) -> bool:
    ...


Rules:

Use the one dict subtract method

Must include the len early exit

No sorting
"""

def is_anagram(s: str, t: str) -> bool:
    # early exit if lengths are not equal
    if len(s) != len(t):
        return False
    # create frequecy counter
    freq_s = {}
    # iterate through s and count characters 
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
    
    # check if any characters in t if you subtract the count  -1 it return < 0 
    for char in t:
        freq_s[char] = freq_s.get(char, 0) - 1 
        if freq_s[char] < 0:
            return False 
    return True 


if __name__ == "__main__":
    pass

