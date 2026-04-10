"""
702

Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists,
then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array 
using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
"""

from typing import List


class ArrayReader:
    def __init__(self, arr: List):
        self.arr = arr
    
    def get(self, k: int | float) -> int:
        if k < 0 or k >= len(self.arr):
            return 2147483647
        return self.arr[k]


def search(reader: ArrayReader, target: int) -> int:
    """
    Search for target in unknown size sorted array using binary search.
    
    Args:
        reader: ArrayReader interface to access array elements
        target: Value to search for
    
    Returns:
        Index of target if found, otherwise -1
        
    Reasons:
    For this question above brute force will be to check for each index 
    in the array of unknown size and compare if the value at that index is equal to the target.
    Considering the possible size of the array, it will not be efficient enough aand hence
    lead to a time complexity of O(n) and space complecity of O(1).
    
    Hence we need a more optimized slution where we can iterate through half of the search space at each step.
    Since the array is sorted we can use binary search on it but there is a catch.
    
    Before we do vanilla binary search we have to get closer to the range of values
    where our target value could fall in.
    
    Then we can do regular binar search.
    """
    # create left and right pointers
    left, right = 0, 1
    
    # We increment right in exponents untill it becomes greater than the target but not to close to the greatest value
    while reader.get(right) < target:
        left = right
        right = right << 1 #(<<1 is same as multiplying by 2)
    
    while left <= right:
        mid = (left + right) // 2 
        value = reader.get(mid)
        if value == target:
            return mid 
        elif value < target:
            left = mid + 1 
        else:
            right = mid - 1
    return - 1
        
        
    
    
    


def main():
    # Official-style example 1
    array1 = [-1, 0, 3, 5, 9, 12]
    reader1 = ArrayReader(array1)
    assert search(reader1, 9) == 4, "Example 1 failed"

    # Official-style example 2
    array2 = [-1, 0, 3, 5, 9, 12]
    reader2 = ArrayReader(array2)
    assert search(reader2, 2) == -1, "Example 2 failed"

    # Target is the first element
    array3 = [-1, 0, 3, 5, 9, 12]
    reader3 = ArrayReader(array3)
    assert search(reader3, -1) == 0, "First element test failed"

    # Target is the last element
    array4 = [-1, 0, 3, 5, 9, 12]
    reader4 = ArrayReader(array4)
    assert search(reader4, 12) == 5, "Last element test failed"

    # Single-element array, target exists
    array5 = [1]
    reader5 = ArrayReader(array5)
    assert search(reader5, 1) == 0, "Single element found test failed"

    # Single-element array, target does not exist
    array6 = [1]
    reader6 = ArrayReader(array6)
    assert search(reader6, 0) == -1, "Single element not found test failed"

    # Target smaller than all elements
    array7 = [2, 4, 6, 8, 10]
    reader7 = ArrayReader(array7)
    assert search(reader7, 1) == -1, "Smaller than all elements test failed"

    # Target larger than all elements
    array8 = [2, 4, 6, 8, 10]
    reader8 = ArrayReader(array8)
    assert search(reader8, 12) == -1, "Larger than all elements test failed"

    # Negative numbers, target exists
    array9 = [-20, -10, -5, -2, 0, 3, 7]
    reader9 = ArrayReader(array9)
    assert search(reader9, -5) == 2, "Negative numbers test failed"

    # Negative numbers, target does not exist
    array10 = [-20, -10, -5, -2, 0, 3, 7]
    reader10 = ArrayReader(array10)
    assert search(reader10, -6) == -1, "Negative numbers not found test failed"

    # Target in the middle
    array11 = [1, 3, 5, 7, 9, 11, 13]
    reader11 = ArrayReader(array11)
    assert search(reader11, 7) == 3, "Middle element test failed"

    # Two-element array, target is first
    array12 = [1, 3]
    reader12 = ArrayReader(array12)
    assert search(reader12, 1) == 0, "Two-element first test failed"

    # Two-element array, target is second
    array13 = [1, 3]
    reader13 = ArrayReader(array13)
    assert search(reader13, 3) == 1, "Two-element second test failed"

    # Two-element array, target missing
    array14 = [1, 3]
    reader14 = ArrayReader(array14)
    assert search(reader14, 2) == -1, "Two-element missing test failed"

    # Large gap values
    array15 = [1, 10, 100, 1000, 10000]
    reader15 = ArrayReader(array15)
    assert search(reader15, 1000) == 3, "Large gap values test failed"

    # Target near expansion boundary
    array16 = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    reader16 = ArrayReader(array16)
    assert search(reader16, 128) == 7, "Expansion boundary test failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()