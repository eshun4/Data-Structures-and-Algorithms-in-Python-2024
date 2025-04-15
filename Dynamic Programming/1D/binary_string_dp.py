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

def binary_strings_memo(n, memo={}):
    """
    Count the number of binary strings with no consecutive 1's that can be formed using
    a binary string of length n and memoization. 
    n: the length of the binary string.
    recurrence relation:
    T(n) = {
        T(n-1) + T(n-2) if n > 2
        1 if n == 0
        1 if n == 1
    }
    """
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = binary_strings_memo(n - 1, memo) + binary_strings_memo(n - 2, memo)
    result = memo[n]
    return result


def binary_strings_tabu(n):
    """
    Count the number of binary strings with no consecutive 1's that can be formed using
    a binary string of length n and tabulization. 
    n: the length of the binary string.
    recurrence relation:
    T(n) = {
        T(n-1) + T(n-2) if n > 2
        1 if n == 0
        1 if n == 1
    }
    """
    # Create dp table to store results of computation
    dp = [0] * (n + 1)
    # Create base cases
    dp[0] = 1
    dp[1] = 1
    
    # FIll the table from 2 to n + 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # Return the last element of the dp table
    return dp[n]
    


def main():
    for n in range(1, 11):
        result = binary_strings(n)
        print(f"Number of binary strings of length {n} is {result}.")
    
    for n in range(1, 11):
        result = binary_strings_memo(n, memo={})
        print(f"Number of binary strings of length {n} is {result}.")
    
    for n in range(1, 11):
        result = binary_strings_tabu(n)
        print(f"Number of binary strings of length {n} is {result}.")


if __name__ == '__main__':
    main()