"""
Triplets.

Given an array containing N integers, and a number S denoting target sum.

Find all distinct integers that can add up to form target sum. The numbers in each triplet should be ordered in ascending order, and triplets
should be ordered too. 

Return empty array if no such triplet exists.

Example:
Input: [1, 2, 3, 4 ,5, 6, 7, 8, 9, 15]
target = 18.

Output: [[1, 2, 15], [3, 7, 8], [4, 6, 8], [5, 6, 7]]

"""

def triplet(numbers, target):
    """
    Given an array containing N integers, and a number S denoting target sum.
    
    Find all distinct integers that can add up to form target sum. The numbers in each triplet should be ordered in ascending order, and triplets
    should be ordered too. 

    Return empty array if no such triplet exists.

    Input: [1, 2, 3, 4 ,5, 6, 7, 8, 9, 15]
    target = 18.

    Output: [[1, 2, 15], [3, 7, 8], [4, 6, 8], [5, 6, 7]]
    
    """
    # First sort the numbers to make it easier to find triplets
    numbers.sort()
    # create a triplets arry to store the results
    triplets = []
    # Get the lenght of the array of numbers
    n = len(numbers)
    # Iterate through the numbers
    for i in range(0, n - 3):
        # Set the pointers of the other two numbers
        j = i + 1
        k = n - 1 
        
        #  Two pointer approach to find the triplets
        while j < k:
            current_sum = numbers[i]
            current_sum += numbers[j]
            current_sum += numbers[k]   
            
            # Check if the current sum is equal to the target sum
            if current_sum == target:
                triplets.append([numbers[i], numbers[j], numbers[k]])
                # Move the pointers to find other triplets
                j += 1
                k -= 1
            # If the current sum is greater that target sum, move the right pointer to the left
            elif current_sum > target:
                k -= 1
            # If the current sum is less than target sum, move the left pointer to the right
            else:
                j += 1
    # return results         
    return triplets

def main():
    numbers = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 15]
    target = 18
    result = triplet(numbers, target)
    print(result)

if __name__ == "__main__":
    main()



