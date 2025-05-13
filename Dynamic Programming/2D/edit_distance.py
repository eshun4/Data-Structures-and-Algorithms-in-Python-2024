"""
Problem: Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character

Example:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
- Replace 'h' with 'r': "horse" -> "rorse"
- Remove 'r': "rorse" -> "rose"
- Remove 'e': "rose" -> "ros"

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
- Replace 'i' with 'e': "intention" -> "entention"
- Replace 'n' with 'x': "entention" -> "extention"
- Replace 't' with 'c': "extention" -> "execution"
- Remove 'e': "execution" -> "execution"
- Remove 'n': "execution" -> "execution"

Write a function to solve this problem using dynamic programming.
"""

def edit_distance(word1, word2, i, j):
    # if both indexes are equal to the length of the strings
    if i == len(word1) and j == len(word2):
        return 0
    # if i has alredy exceeded the legth of word1
    if i == len(word1):
        return len(word2) - j
    # if j has already reached the length of word2
    if j == len(word2):
        return len(word1) - i
    
    # Now we can only iterate when i and j is less than len of both string
    ans = 0
    if word1[i] != word2[j]:
        ans = 1 + min(edit_distance(word1, word2, i + 1, j), edit_distance(word1, word2, i , j + 1), edit_distance(word1, word2, i + 1 , j + 1))
    else:
        ans = edit_distance(word1, word2, i + 1, j + 1)
        
    # return ans
    return ans

def edit_distance_memoized(word1, word2, i, j, memo=None):
    if not memo:
        memo = {}
    # if both indexes are equal to the length of the strings
    if i == len(word1) and j == len(word2):
        return 0
    # if i has alredy exceeded the legth of word1
    if i == len(word1):
        return len(word2) - j
    # if j has already reached the length of word2
    if j == len(word2):
        return len(word1) - i
    
    # Now we can only iterate when i and j is less than len of both string
    ans = 0
    if word1[i] != word2[j]:
        ans = 1 + min(edit_distance_memoized(word1, word2, i + 1, j), edit_distance_memoized(word1, word2, i , j + 1), edit_distance_memoized(word1, word2, i + 1 , j + 1))
        memo[(i, j)] = ans
    else:
        ans = edit_distance_memoized(word1, word2, i + 1, j + 1)
        memo[(i, j)] = ans
        
    # return ans
    return memo[(i, j)]

def edit_distance_dp(word1, word2):
    # get the lengths of both strings
    word1_len, word2_len = len(word1), len(word2)
    # create a dp array
    dp = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]
    
    # initialize the base cases
    for i in range(word1_len + 1):
        dp[i][0] = i  # cost of deleting all characters from word1
    for j in range(word2_len + 1):
        dp[0][j] = j  # cost of inserting all characters into word1

    # fill in the dp table
    for i in range(1, word1_len + 1):
        for j in range(1, word2_len + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no operation needed
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # delete
                                   dp[i][j - 1],    # insert
                                   dp[i - 1][j - 1])  # replace

    return dp[word1_len][word2_len]

            
    

def main():
    """
    Main function to demonstrate the calculation of the minimum number of operations 
    required to convert one string into another using three different approaches:
    recursive, memoized, and bottom-up dynamic programming.
    Examples:
        1. Recursive approach:
            - Converts "horse" to "ros".
            - Converts "intention" to "execution".
        2. Memoized approach:
            - Converts "horse" to "ros" using memoization to optimize recursion.
            - Converts "intention" to "execution" using memoization.
        3. Bottom-up dynamic programming approach:
            - Converts "horse" to "ros" using a tabular method.
            - Converts "intention" to "execution" using a tabular method.
    Each example prints the minimum number of operations required for the conversion.
    Note:
        - `edit_distance` is the recursive implementation.
        - `edit_distance_memoized` is the memoized implementation.
        - `edit_distance_dp` is the bottom-up dynamic programming implementation.
    """
    # example 1
    word1 = "horse"
    word2 = "ros"
    print(f"The minimum number of operations to convert {word1} to {word2} is: {edit_distance(word1, word2, 0, 0)}")
    
    # example 2
    word3 = "intention" 
    word4 = "execution"
    print(f"The minimum number of operations to convert {word1} to {word2} is: {edit_distance(word3, word4, 0, 0)}")
    
    # example 3
    word1 = "horse"
    word2 = "ros"
    print(f"The minimum number of operations to convert {word1} to {word2} (memoized) is: {edit_distance_memoized(word1, word2, 0, 0)}")
    
    # example 4
    word3 = "intention" 
    word4 = "execution"
    print(f"The minimum number of operations to convert {word1} to {word2} (memoized) is: {edit_distance_memoized(word3, word4, 0, 0)}")
    
     # example 5
    word1 = "horse"
    word2 = "ros"
    print(f"The minimum number of operations to convert {word1} to {word2} (Bottom-up) is: {edit_distance_dp(word1, word2)}")
    
    # example 6
    word3 = "intention" 
    word4 = "execution"
    print(f"The minimum number of operations to convert {word1} to {word2} (Bottom-up) is: {edit_distance_dp(word3, word4)}")
    
    
if __name__ == "__main__":
    main()



