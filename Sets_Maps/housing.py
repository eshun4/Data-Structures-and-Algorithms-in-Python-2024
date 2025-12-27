"""
Along one side of a road, there is a sequence of vacant plots of land.
Each plot hs a different area (non-zero). So the areas form the sequence A[1], A[2], ...A[N].

You want to buy k acres of land to build a house. You want to find all segments of contigious plots (i.e. subsection in the sequence) of whose sum is exactly k. 

Example:

Plots = [1 3 2 1 4 1 3 2 1 1]

k = 8

"""

def find_subarrays_with_sum_k(plots, k):
    # check early exit
    if not plots:
        return []
    if len(plots) == 1:
        if plots[0] == k:
            return [[0, 0]]
        else:
            return []
    # create left pointer 
    left = 0 
    # create result list
    result = []
    # create cur_sem variable 
    cur_sum = 0 
    for right in range(len(plots)):
        cur_sum += plots[right]
        while cur_sum > k and left < right:
            cur_sum -= plots[left]
            left += 1 
        if cur_sum == k:
            result.append([left, right])
    return result


def main():
    plots = [1, 3, 2, 1, 4, 1, 3, 2, 1, 1]
    k = 8
    print(find_subarrays_with_sum_k(plots, k))
    
    
if __name__ == "__main__":
    main()