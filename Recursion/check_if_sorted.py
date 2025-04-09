
def is_sorted(A):
    """ This function checks if the array A is sorted in ascending order. If the array is sorted return True else return False.
    A: the array being checked.
    """
    # Check for the base case where the array A is of length 1
    if len(A) == 1:
        return True
    # Check if the first element is less than or equal to the second element
    else:
        return A[0] <= A[1] and is_sorted(A[1:])
   


def main():
    A = [1,2,3,4,5,6,7,8,9]
    result = is_sorted(A)
    if result != True:
        print(f"Result is not sorted.")
    else:
        print(f"Result is sorted")
    

if __name__ == "__main__":
    main()