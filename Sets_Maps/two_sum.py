"""
Write this function:

def two_sum_exists(nums: list[int], target: int) -> bool:

Rules:

Use a set

One pass

Return True/False only

"""


def two_sum_exists(nums: list[int], target: int) -> bool:
    # create a seen set
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False

def two_sum_indices(nums: list[int], target: int) -> list[int]:
    # create pos 
    pos = {}
    # iterate through nums 
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in pos:
            return [pos[complement], i]
        pos[nums[i]] = i
    return []


if __name__ == "__main__":
    pass