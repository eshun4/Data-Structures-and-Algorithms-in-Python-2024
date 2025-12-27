"""
Write:

def first_unique_char(s: str) -> str | None:
    ...


Rules:

Must use a dict frequency map

Use the 2-pass approach

Return None if no unique char

"""

def first_unique_char(s: str) -> str | None:
    # create a frequecty map
    freq = {}
    # first pass to count elements 
    for char in s:
        if char in freq:
            freq[char] = freq.get(char, 0) + 1 
    # second pass to find the unique chracter 
    for char in s:
        if freq[char] == 1:
            return char 
    return None
            

if __name__ == "__main__":
    pass

