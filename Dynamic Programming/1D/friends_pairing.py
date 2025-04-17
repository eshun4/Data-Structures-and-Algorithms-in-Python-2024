"""
Question:
You are given `n` friends, each one can remain single or can be paired up with another friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up.

Input:
An integer `n` representing the number of friends.

Output:
An integer representing the total number of ways friends can remain single or paired.

Example:
Input: 3
Output: 4

Explanation:
- All three friends remain single: {1}, {2}, {3}
- Friend 1 pairs with Friend 2, and Friend 3 remains single: {1,2}, {3}
- Friend 1 pairs with Friend 3, and Friend 2 remains single: {1,3}, {2}
- Friend 2 pairs with Friend 3, and Friend 1 remains single: {2,3}, {1}

Bonus:
If an array of letters is given representing friends, generate all possible combinations of friends being single or paired.
['A', 'B', 'C']
[
    [['A'], ['B'], ['C']],
    [['A', 'B'], ['C']],
    [['A', 'C'], ['B']],
    [['B', 'C'], ['A']]
]
- All friends remain single: [['A'], ['B'], ['C']]
- Friend 'A' pairs with Friend 'B', and 'C' remains single: [['A', 'B'], ['C']]
- Friend 'A' pairs with Friend 'C', and 'B' remains single: [['A', 'C'], ['B']]
- Friend 'B' pairs with Friend 'C', and 'A' remains single: [['B', 'C'], ['A']]

"""

import time

def friends_pairing_recursive(n):
    """ This function returns the number of ways a friend can remain single or paired.
    Explanation:
        There are two options for a person to make:
        1. Be single. i.e.( in the case of n if one decides to be single it leaves (n - 1) friends to decide whether to remain single or paired)
        2. Paired.i.e (in this case if one person decides to pair up it leaves (n - 2) friends remaining. Now since the remaining n - 2 friends also can be paired,
        each n - 1 can pair with n - 2 remaining options)
        
        To conclude we have f(n) = f(n - 1) + f(n - 1)f(n - 2), when n >= 2, if  n == 0, f(0) = 1 and if n == 1, f(1) = 1.
        
    *** WARNING ***
    This method will encounter a recursive overhead and hence should be optimized for efficiency.
    If larger inputs are given, it will hit a stack overflow where the memory size exceeds the one allocated to it at runtime.
    To add, the time complexity is an exponential one O(2**n) which is not efficient enough to handle larger inputs.
    The space complexity is O(n) due to the recursive call stack.
    """
    
    # Check if cases
    if n == 0 or n == 1:
        return 1
    result = friends_pairing_recursive(n - 1) + friends_pairing_recursive(n - 1) * friends_pairing_recursive(n - 2)
    return result

def friends_pairing_memo(n, memo):
    """
    Calculates the number of ways friends can remain single or pair up using memoization.
    Explanation:
        There are two options for each person:
        1. Be single: If one person decides to remain single, it leaves (n - 1) friends to decide.
        2. Pair up: If one person pairs up, it leaves (n - 2) friends to decide. Additionally, the person can pair
           with any of the remaining (n - 1) friends.
        The recurrence relation is:
            f(n) = f(n - 1) + (n - 1) * f(n - 2), for n >= 2
        Base cases:
            f(0) = 1 (no friends, one way to do nothing)
            f(1) = 1 (one friend, only one way to remain single)
    Memoization:
        This implementation optimizes the recursive approach by storing intermediate results to avoid redundant calculations.
        It reduces the time complexity to O(n) and the space complexity to O(n) for the memoization table.
    Parameters:
        n (int): The number of friends.
    Returns:
        int: The number of ways friends can remain single or pair up.
    """
    # Check if memo is not initialized to a dictionary
    if memo is None:
        memo = {}
    # Check if n is in memo
    if n in memo:
        return memo[n]
    # If cases
    if n == 0 or n == 1:
        return 1
    else:
        memo[n] =  friends_pairing_memo(n - 1, memo) + friends_pairing_memo(n - 1, memo) * friends_pairing_memo(n - 2, memo)
    result = memo[n]
    return result


def friends_pairing_tabulation(n):
    
    """
    Calculates the number of ways to pair up friends or leave them single
    using a tabulation (bottom-up dynamic programming) approach.
    The problem is based on the idea that each friend can either:
    1. Stay single, in which case the problem reduces to solving for (n-1) friends.
    2. Pair up with one of the remaining (n-1) friends, in which case the problem
       reduces to solving for (n-2) friends.
    This function uses a table to iteratively compute the solution for all values
    from 1 to n, avoiding the overhead of recursion.
    Args:
        n (int): The number of friends.
    Returns:
        int: The total number of ways to pair up or leave single the given number of friends.
    """
    # First check the if cases
    if n <= 1:
        return 1
    # Create the table to compute values
    dp = [0] * n
    
    # CHeck the base cases
    dp[0] = 1
    dp[1] = 1 
    
    # Iterate the table and populate with the values
    for i in range(2, n):
        dp[i] = dp[i - 1] + (dp[i - 1] * dp[i - 2])
    
    # lastly return the number of ways to pair or be single which is the last elemnt in the array
    return dp[n - 1]
        
def bonus_question(array):
    
    """
    Generates all possible pairs of characters from the given array.
    This function takes an array of characters as input and returns all 
    unique pairs of characters that can be formed. Each pair is represented 
    as a tuple, and the order of characters in the array does not affect 
    the pairing.
    Args:
        array (list): A list of characters to generate pairs from.
    Returns:
        list: A list of lists, where each list represents a unique pair 
              of characters from the input array.
    Example:
        >>> bonus_question(['a', 'b', 'c'])
        [['a', 'b'], ['a', 'c'], ['b', 'c']]    
    """
    
    # Get the length of the input array
    n = len(array)
    
    if n < 2:
        return []
    
    # crete two state arrays to keep track of the results and solutions
    res, sol = [], []
    
    # Create a backtracking function that recursively pairs the elemnts in the array 
    def backtrack(start):
        if len(sol) == 2:
            res.append(sol[:])
            return
        
        for i in range(start, n):
            # include current character
            sol.append(array[i])
            backtrack(i + 1)
            sol.pop() #remove array from current pair
            
    backtrack(0)
    return res
        
        
        
            
    
    
    

def main():
    start1 = time.time()
    n = 3
    result = friends_pairing_recursive(n)
    print(f"The number of ways {n} friends can be single or paired are: {result}")
    end1 = time.time()
    print(f"Time elapsed for first call: {round(end1 - start1, 3)} secs.")
    
    # Maximum reursion error with the test case below
    start2 = time.time()
    n = 20 # Crashes at 21
    result = friends_pairing_recursive(n)
    end2 = time.time()
    print(f"The number of ways {n} friends can be single or paired are: {result} secs.")
    print(f"Time elapsed for second call: {round(end2 - start2 , 3)} secs.")
    
    print("----------------------------------------------------------------------")
    
    start3 = time.time()
    n = 3
    memo = {}
    result = friends_pairing_memo(n, memo)
    print(f"The number of ways {n} friends can be single or paired are: {result}")
    end3 = time.time()
    print(f"Time elapsed for first call: {round(end3 - start3, 3)} secs.")
    
    start4 = time.time()
    n = 21 # crashes at 22
    result = friends_pairing_memo(n, memo)
    print(f"The number of ways {n} friends can be single or paired are: {result}")
    end4 = time.time()
    print(f"Time elapsed for second call: {round(end4 - start4, 3)} secs.")
    
    print("----------------------------------------------------------------------")
    
    start5 = time.time()
    n = 3
    memo = {}
    result = friends_pairing_memo(n, memo)
    print(f"The number of ways {n} friends can be single or paired are: {result}")
    end5 = time.time()
    print(f"Time elapsed for first call: {round(end5 - start5, 3)} secs.")
    
    start6 = time.time()
    n = 22 # Crashes at 23
    result = friends_pairing_tabulation(n)
    print(f"The number of ways {n} friends can be single or paired are: {result}")
    end6 = time.time()
    print(f"Time elapsed for second call: {round(end6 - start6, 3)} secs.")
    
    print("--------------------------------------------------------------------")
    array = ['A', 'B', 'C']
    n = len(array)
    result = bonus_question(array)
    print(f"All the possible combinations {n} friends are: {result}")    
    
if __name__ == "__main__":
    main()