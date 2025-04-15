


def count_set_bits(n):
    """
    Count the number of set bits from 1 to n.
    :param n: The number to count set bits from 1 to n.
    :return: The number of set bits from 1 to n.
    """
    # Create the dp table
    dp = [0] * (n + 1)
    # Check for the base cases
    dp[0] = 0
    
    # Fill the dp table from 1 to n + 1
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1) # i >> 1 is the same as i // 2 and i & 1 is the same as i % 2
    # return the last element of the dp table
    return sum(dp)

def main():
    n = 5
    result = count_set_bits(n)        
    print(f"The number of set bits from 1 to {n} is: {result}")
    
    n = 10
    result = count_set_bits(n)        
    print(f"The number of set bits from 1 to {n} is: {result}")
    
    n = 20
    result = count_set_bits(n)        
    print(f"The number of set bits from 1 to {n} is: {result}")

if __name__ == "__main__":
    # Test the function with different values of n
    main()