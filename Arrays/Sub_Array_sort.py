"""
Subarray Sort.

Given an array of size at least 2, find the smallest subarray that needs to be sorted in place
so that the entire input array becomes sorted.

If the input array is already sorted, the function should return [-1, -1], andotherwise return the start and end index
of the smallest subarray.

Sample Input:
[1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11]

Sample Output:
[5, 7]

"""
def out_of_order(arr, i, numbers):
    """
    Determines if the element at index i in the array is out of order.

    An element is considered out of order if:
    - It is greater than the next element (for all elements except the last one).
    - It is smaller than the previous element (for all elements except the first one).

    Args:
    arr (list): The input array (not used in this function, can be removed).
    i (int): The index of the element to check.
    numbers (list): The input array.

    Returns:
    bool: True if the element is out of order, False otherwise.
    """
    x = numbers[i]
    # Check if the first element is greater than the second element
    if i == 0:
        return x > numbers[1]
    # Check if the last element is smaller than the second-to-last element
    if i == len(numbers) - 1:
        return x < numbers[i - 1]
    # Check if the current element is greater than the next or smaller than the previous
    return x > numbers[i + 1] or x < numbers[i - 1]


def sub_array_sort(numbers):
    """
    Given an array of size at least 2, find the smallest subarray that needs to be sorted in place
    so that the entire input array becomes sorted.
    """
    # Initialize smallest and largest to extreme values
    smallest = float("inf")  # Smallest out-of-order value in the array
    largest = float("-inf")  # Largest out-of-order value in the array

    # Iterate through the array to find out-of-order elements
    for i in range(len(numbers)):
        x = numbers[i]
        # Check if the current number is out of order
        if out_of_order(numbers, i, numbers):
            # Update smallest and largest with the out-of-order values
            smallest = min(smallest, x)
            largest = max(largest, x)

    # If no out-of-order elements are found, return [-1, -1]
    if smallest == float("inf"):
        return [-1, -1]

    # Find the correct position of the smallest out-of-order element
    left = 0
    while smallest >= numbers[left]:
        left += 1

    # Find the correct position of the largest out-of-order element
    right = len(numbers) - 1
    while largest <= numbers[right]:
        right -= 1

    # Return the indices of the smallest subarray that needs to be sorted
    return [left, right]
    
    

def main():
    # Example usage of the function
    numbers = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11]
    result = sub_array_sort(numbers)
    print(result) # Output: [5, 7]


if __name__ == "__main__":
    main()