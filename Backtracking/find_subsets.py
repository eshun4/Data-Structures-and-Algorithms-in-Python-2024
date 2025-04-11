"""
Given a string, find all subsets of the given string.

Input:
    "abc"
    
Output:   
    [
        "", "a", "ab", "abc", "ac", "b", "bc", "c"
    ]
    
In finding subsets of a string, we decide if we will include a character in a string or not. 
In this case, we have 3 characters in the string.
We can either include or exclude each character for each level of recursion.
So, we have 2^3 = 8 subsets in total.
"""


def find_subsets(inputarr, outputArr, i, j):
    # base case
    # if i == len(inputarr):
    #     # append the subset to the output array
    #     outputArr.append(''.join(outputArr[:j]))
    #     print(outputArr[:j])
    #     return
    
    # # recursion case
    # # include the character
    # outputArr[j] = inputarr[i]
    # find_subsets(inputarr, outputArr, i + 1, j + 1)
    # # exclude the character
    # find_subsets(inputarr, outputArr, i + 1, j)
    
        
    if inputarr[i] == '\0':
        outputArr[j] = '\0'
        print(outputArr)
        return
    
    # Recursion case
    # include the character
    outputArr[j] = inputarr[i]
    find_subsets(inputarr, outputArr, i + 1, j + 1)
    # exclude the character
    find_subsets(inputarr, outputArr, i + 1, j)
    
    
def find_subsets2(input_set):
    def backtrack(index, current_subset):
        # Base case: if we've processed all elements
        if index == len(input_set):
            subsets.append(current_subset[:])  # Record the current subset
            return
        
        # Include the current element
        current_subset.append(input_set[index])
        backtrack(index + 1, current_subset)  # Recurse with the element included
        
        # Exclude the current element (backtrack step)
        current_subset.pop()
        backtrack(index + 1, current_subset)  # Recurse without the element

    subsets = []  # This will store all the subsets
    backtrack(0, [])  # Start backtracking with an empty subset
    return subsets

def find_subsets3(input_set):
    n = len(input_set)
    sol, res = [], []
    def backtrack(index):
        # Base case: if we've processed all elements
        if index == n:
            res.append(sol[:])  # Record the current subset
            return
        
        # Include the current element
        sol.append(input_set[index])
        backtrack(index + 1)  # Recurse with the element included
        
        # Exclude the current element (backtrack step)
        sol.pop()
        backtrack(index + 1)  # Recurse without the element

  
    backtrack(0)  # Start backtracking with an empty subset
    return res



def subsets4(nums):
    # Start with the DP table containing only the empty subset
    dp_table = [[]]  # Initial row (base case)

    # Process each number in the input list
    for num in nums:
        # Add `num` to all existing subsets in the DP table
        new_subsets = [subset + [num] for subset in dp_table]
        dp_table.extend(new_subsets)  # Update DP table with new subsets

    return dp_table
    


def main():
    # print("All subsets of the given string are:")
    # inputarr = "abc\0"
    # outputArr = ['\0'] * (len(inputarr) + 1)
    # find_subsets(inputarr, outputArr, 0, 0)
    
    # Example usage:
    # input_set = ['a', 'b', 'c']
    # all_subsets = find_subsets2(input_set)
    # print(all_subsets)
    
    # Example usage:
    # input_set = ['a', 'b', 'c'] 
    # all_subsets = find_subsets3(input_set)
    # print(all_subsets)
    
    nums = [1,2,3]
    result = subsets4(nums)
    print("All subsets of the given list are:")
    for subset in result:
        print(subset)
    



if __name__ == "__main__":
    main()