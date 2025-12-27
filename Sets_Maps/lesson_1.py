"""
Write two Python functions:

contains_duplicate(nums: list[int]) -> bool

first_repeating_char(s: str) -> str | None

Rules:

Use set for both.

One pass each.

No sorting.

Keep it clean and short.
"""

def contains_duplicate(nums: list[int]) -> bool:
    # create an empty set 
    seen = set()
    # iterate through nums
    for num in nums:
        # if num in seen return True
        if num in seen:
            return True
        seen.add(num)
    return False

def first_repeating_char(s: str) -> str | None:
    # create an empty seen set
    seen = set()
    # iterate through string s 
    n = len(s)
    for i in range(n):
        if s[i] in seen:
            return s[i]
        seen.add(s[i])
    return None


if __name__ == "__main__":
    pass

