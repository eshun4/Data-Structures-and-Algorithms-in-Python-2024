# testing outthe quickselect algorithm first bu sorting, then a heap and then lastly with quicksoelect with both lomuto and horare partition
import heapq 
import random 

def kth_smallest_with_sorting(arr, k):
    # sort the array 
    arr.sort()
    return arr[k - 1]
    
def kth_smallest_with_min_heap(arr,k):
    # create a min heap 
    heapq.heapify(arr)
    # create a var to store kth element
    kth = 0
    
    #iterte through min_heap 
    for _ in range(k):
        elem = heapq.heappop(arr)
        kth = elem 
    return elem
    
def lomuto_partition(A, left, right):
    # get the pivot 
    pivot = A[right]
    i = left - 1 
    # iterate through the array for j 
    for j in range(left, right):
        if A[j] <= pivot:
            i += 1 
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1
    
def partition_hoare(nums, left, right):
    # 1. Select a random pivot and move it to the middle/start to avoid O(n^2)
    pivot_idx = random.randint(left, right)
    pivot = nums[pivot_idx]
    
    i = left - 1
    j = right + 1
    
    while True:
        # Move i right while nums[i] < pivot
        while True:
            i += 1
            if nums[i] >= pivot: break
        
        # Move j left while nums[j] > pivot
        while True:
            j -= 1
            if nums[j] <= pivot: break
        
        # If pointers cross, return the split point
        if i >= j:
            return j
        
        # Swap elements at i and j
        nums[i], nums[j] = nums[j], nums[i]


def quickselect(A, left, right, k_index):
    if left == right:
        return A[left]
    
    # get the pivot index 
    pivotI = lomuto_partition(A, left, right) 
    # check k is equeal to pIndex 
    if pivotI == k_index:
        return A[pivotI]
    elif pivotI < k_index:
        return quickselect(A, pivotI + 1, right, k_index)
    else:
        return quickselect(A, left, pivotI - 1, k_index)
        
def quickselect_horare(A, left, right, k_index):
    if left == right:
        return A[left]
    
    # get the pivot index 
    pivotI = partition_hoare(A, left, right) 
    # check k is equeal to pIndex 
    if pivotI == k_index:
        return A[pivotI]
    elif pivotI < k_index:
        return quickselect(A, pivotI + 1, right, k_index)
    else:
        return quickselect(A, left, pivotI - 1, k_index)
    
    

    
    


def main():
    arr = [1, 5, 7, 10, 9, 20, 0]
    k = 3 #should return 5 as output
    k_index = k - 1
    print(kth_smallest_with_sorting(arr[:], k))
    
    # for heapq
    print("")
    print("Priority queue implementation")
    print(kth_smallest_with_min_heap(arr[:],k))
    
    # for quickselect with lomuto
    print("")
    print("Quickselect with Lomuto")
    left, right= 0, len(arr) - 1,
    print(quickselect(arr[:], left, right, k_index))
    
    # for quickselect with horare
    print("")
    print("Quickselect with Horare")
    left, right= 0, len(arr) - 1,
    print(quickselect_horare(arr[:], left, right, k_index))
    

if __name__ == "__main__":
    main()