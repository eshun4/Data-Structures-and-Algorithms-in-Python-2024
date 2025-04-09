




def linear_search(A, i, j, k):
    """ This function recursively searches for the value k in the array A. If the value k exists return the index of the element. else return -1.1
    i:the starting index of the array.
    j: the ending index of the array.
    A: the array being searched.
    k: the value being searched for.
    """
    # Check if the start index is greater than the end index
    if i > j:
        return -1
    # If the start index is less than the end index then check if the value at the start of the array A is equal to k.
    if A[i] == k:
        return i
    # If the value is not equal to k in the Array A, then recursively search the remaining array starting from the next element
    return linear_search(A, i + 1, j, k)


def main():
    A = [23, 45, 12, 65 ,77, 89, 100, 2, 3, 4, 5]
    k = 2
    i = 0
    j = len(A) - 1
    result = linear_search(A, i, j, k)
    if result != -1:
        print(f"Element {k} found at index {result}.")
    else:
        print(f"Element {k} not found in the array.")
    

if __name__ == "__main__":
    main()