


def fibonacci(n):
    """
    This is a function to find the nth fibonacci without memoization.
    The fibonacci sequence is defined as follows:
    F(0) = 1
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    """
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_tabu(n):
    """
    This is a function to find the nth fibonacci with tabulization.
    The fibonacci sequence is defined as follows:
    F(0) = 1
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    """
    # Create a dp table starting from 0 to n + 1 
    dp = [0] * (n + 1)
    # Base case
    dp[0] = 1
    dp[1] = 1
    # Fill the dp table from 2 to n + 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i -2]
    # Return the last element of the dp table
    return dp[n]


    


def main():
    n = 10
    result = fibonacci(n)
    print(f"The {n}th fibonacci number is: {result}")
    
    n = 20
    result = fibonacci(n)
    print(f"The {n}th fibonacci number is: {result}")
    
    n = 30
    result = fibonacci(n)
    print(f"The {n}th fibonacci number is: {result}")
    
    # Using memoization
    n = 10
    result = fibonacci_tabu(n)
    print(f"The {n}th fibonacci number is: {result}")
    
    n = 20
    result = fibonacci_tabu(n)
    print(f"The {n}th fibonacci number is: {result}")
    
    n = 30
    result = fibonacci_tabu(n)
    print(f"The {n}th fibonacci number is: {result}")
    
    
    
    
    
if __name__ == "__main__":
    main()