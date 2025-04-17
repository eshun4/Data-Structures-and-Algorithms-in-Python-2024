"""
### Alphacode / Decode Ways on Leetcode.

ACODE - Alphacode
#dynamic-programming

    - Alice and Bob need to send secret messages to each other and are discussing ways to encode their messages:

    - Alice: “Let’s just use a very simple code: We’ll assign ‘A’ the code word 1, ‘B’ will be 2, and so on down to ‘Z’ being assigned 26.”

    - Bob: “That’s a stupid code, Alice. Suppose I send you the word ‘BEAN’ encoded as 25114. You could decode that in many different ways!”

    - Alice: “Sure you could, but what words would you get? Other than ‘BEAN’, you’d get ‘BEAAD’, ‘YAAD’, ‘YAN’, ‘YKD’ and ‘BEKD’. I think you would be able to figure out the correct decoding. And why would you send me the word ‘BEAN’ anyway?”

    - Bob: “OK, maybe that’s a bad example, but I bet you that if you got a string of length 5000 there would be tons of different decodings and with that many you would find at least two different ones that would make sense.”

    - Alice: “How many different decodings?”

    - Bob: “Jillions!”

    - For some reason, Alice is still unconvinced by Bob’s argument, so she requires a program that will determine how many decodings there can be 
    for a given string using her code.

Input
Input will consist of multiple input sets. Each set will consist of a single line of at most 5000 digits representing a valid encryption 
(for example, no line will begin with a 0). There will be no spaces between the digits. 
An input line of ‘0’ will terminate the input and should not be processed.

Output
For each input set, output the number of possible decodings for the input string. All answers will be within the range of a 64 bit signed integer.

    Example
    Input:
    25114
    1111111111
    3333333333
    0

    Output:
    6
    89
    1

"""

def alpha_code(s):
    """
    Function to calculate the number of ways to decode a given string `s`.
    Uses recursion with memoization to solve the problem efficiently.
    """
    
    def dp(i):
        """
        Recursive helper function to calculate the number of decodings starting from index `i`.
        """
        # Base case: If index reaches the end of the string, there is one valid decoding
        if i == len(s):
            return 1
        
        # Initialize the answer for the current index
        ans = 0
        
        # Check if the current character is a valid single-digit number (1-9)
        if s[i] >= "1" and s[i] <= '9':
            ans += dp(i + 1)  # Recur for the next index
            
        # Check if the current and next characters form a valid two-digit number (10-19)
        if (i + 1 < len(s) and s[i] == "1"):
            ans += dp(i + 2)  # Recur for the index after the next one
            
        # Check if the current and next characters form a valid two-digit number (20-26)
        if (i + 1 < len(s) and s[i] == "2" and s[i + 1] <= '6'):
            ans += dp(i + 2)  # Recur for the index after the next one
            
        return ans  # Return the total number of decodings for the current index
    
    return dp(0)  # Start the recursion from index 0

def alpha_code_dp_tabulize(s):
    """
    Function to calculate the number of ways to decode a given string `s`.
    Uses dynamic programming with tabulation to solve the problem efficiently.
    """
    
    n = len(s)
    if n == 0:
        return 0

    # dp[i] will store the number of ways to decode the substring s[:i+1]
    dp = [0] * n
    dp[0] = 1 if s[0] != '0' else 0  # Base case: single character decoding

    for i in range(1, n):
        # Check if the current character is a valid single-digit number (1-9)
        if s[i] >= '1' and s[i] <= '9':
            dp[i] += dp[i - 1]

        # Check if the last two characters form a valid two-digit number (10-26)
        if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
            dp[i] += dp[i - 2] if i - 2 >= 0 else 1

    return dp[n - 1]  # The result is stored in the last element of dp


def decode_ways_return_results(s):
    """
    Function to return all possible decodings of the given string `s`.
    """
    results, sol = [], []
    def backtrack(index):
        # If we reach the end of the string, add the current path to results
        if index == len(s):
            results.append("".join(sol[:]))
            return
        
        # Single-digit decoding
        if s[index] >= '1' and s[index] <= '9':
            sol.append(chr(int(s[index]) + 64))  # Convert to corresponding letter
            backtrack(index + 1)
            sol.pop()
        
        # Two-digit decoding
        if index + 1 < len(s) and (s[index] == '1' or (s[index] == '2' and s[index + 1] <= '6')):
            sol.append(chr(int(s[index:index + 2]) + 64))  # Convert to corresponding letter
            backtrack(index + 2)
            sol.pop()
    
    backtrack(0)
    return results
            
def main():
    """
    Main function to handle input and output.
    Continuously reads input strings, calculates the number of decodings, and prints the result.
    Terminates when the input string is '0'.
    """
    print(alpha_code("25114"))
    print(alpha_code("1111111111"))
    print(alpha_code("3333333333"))
    print(alpha_code("1"))
    print()
    print(alpha_code_dp_tabulize("25114"))
    print(alpha_code_dp_tabulize("1111111111"))
    print(alpha_code_dp_tabulize("3333333333"))
    print(alpha_code_dp_tabulize("1"))
    print()
    print(decode_ways_return_results("25114"))
    print(decode_ways_return_results("1111111111"))
    print(decode_ways_return_results("3333333333"))
    print(decode_ways_return_results("1"))

if __name__ == "__main__":
    main()