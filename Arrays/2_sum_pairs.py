"""
Pairs.



"""


def pairs(numbers, target):
    """
    Given an array containing N integers, and a number S denoting a target Sum. 
    Find two distinct integers that can pair up to form the target sum.
    
    Input: [10, 5, 2, 3, -6, 9 , 11]
    numbers (list): List of integers.
    target (int): Target sum. 4
    
    Output: [10, -6]
    list: List of pairs that sum up to the target.
    
    """
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            return [num, complement]
        # add the current number to the set if its not in it
        seen.add(num)
    # if no pairs are found return an empty list
    return []


def main():
    n = [10, 5, 2, 3, -6, 9 , 11]
    target = 4
    result = pairs(n, target)
    print(result)


if __name__ == "__main__":
    main()