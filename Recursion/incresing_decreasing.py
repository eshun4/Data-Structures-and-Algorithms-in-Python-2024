

def decreasing_number(n):
    """
    Print all number 1 to n recursively in decreasing order.
    n: the number to start from. 
    """
    # Check for the base case when the number is equal to 0 or 1
    if n == 0 or n == 1:
        return 1
    print(f"Decreasing number from {n} to {n - 1}.")
    return decreasing_number(n-1)
    

def incresing_number(n):
    """
    Print all number 1 to n recursively in increasing order.
    n: the number to start from. 
    """
    # Check for the base case when the number is equal to 0 or 1
    if n == 0 or n == 1:
        return 1
    incresing_number(n-1)
    print(f"Increasing number from {n - 1} to {n}.")
    return 
    


def main():
    n = 5
    print("Decreasing number:")
    print(decreasing_number(n))
    print("Increasing number:")
    print(incresing_number(n))

if __name__ == "__main__":
    main()