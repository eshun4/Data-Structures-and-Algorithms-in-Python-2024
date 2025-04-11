"""
### Binary Strings

This module contains a function to generate all binary strings of length n.

"""


def binary_strings(n):
    """
    Generate all binary strings of length n.
    n: the length of the binary string.
    """
    def backtrack(n, prefix="", solutions=[]):
        # Check the base case if n is 0
        if n == 0:
            solutions.append(prefix)
            return
        # Recursive case: append "0" and "1" to the prefix and decrement n
        if n > 0:
            backtrack(n -1, prefix + "0", solutions)
            backtrack(n -1, prefix + "1", solutions)
            
    solutions = []
    backtrack(n,"", solutions)
    return solutions



def binary_strings_no_contigous(n):
    """
    Generate all binary strings of length n with no contiguous 1's.
    n: the length of the binary string.
    """
    def backtrack(n, solutions, prefix=""):
        # Base case: If n is 0, print the binary string
        if n == 0:
            solutions.append(prefix[:])
            return
        
        # Recursive case
        if not prefix or prefix[-1] == "0":
            # Allow both '0' and '1'
            backtrack(n - 1, solutions, prefix + "0")
            backtrack(n - 1, solutions, prefix + "1")
        else:
            # Allow only '0' to prevent consecutive '1's
            backtrack(n - 1, solutions, prefix + "0")
    solutions = []
    backtrack(n, solutions, prefix="")
    return solutions





    


def main():
    n = 2
    result = binary_strings(n)
    print(f"Binary strings of length {n} are:")
    print(result)
    n = 4
    result = binary_strings(n)
    print(f"Binary strings of length {n} are:")
    print(result)
    n = 3
    result = binary_strings(n)
    print(f"Binary strings of length {n} are:")
    print(result)
    print()
    n = 5
    print(f"Binary strings of length {n} with no contigous 1's are:")
    results = binary_strings_no_contigous(n)
    print(results)
    

if __name__ == '__main__':
    main()