"""
### Binary Strings

This module contains a function to generate all binary strings of length n.

"""


def binary_strings(n):
    """
    Count the number of binary strings with no consecutive 1's that can be formed using
    a binary string of length n. 
    n: the length of the binary string.
    recurrence relation:
    T(n) = {
        T(n-1) + T(n-2) if n > 2
        1 if n == 0
        1 if n == 1
    }
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    return binary_strings(n - 1) + binary_strings(n - 2)
    


def main():
    n = 5
    result = binary_strings(n)
    print(f"Number of binary strings of length {n} is {result}.")
    n = 4
    result = binary_strings(n)
    print(f"Number of binary strings of length {n} is {result}.")
    n = 3
    result = binary_strings(n)
    print(f"Number of binary strings of length {n} is {result}.")



if __name__ == '__main__':
    main()