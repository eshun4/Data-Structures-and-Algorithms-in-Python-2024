


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


def fibonacci_memo(n, memo={}):
    """
    This is a function to find the nth fibonacci with memoization.
    The fibonacci sequence is defined as follows:
    F(0) = 1
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    """
    # Check if the number is alredy in the memo
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    result = memo[n]
    return result


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
    result = fibonacci_memo(n, memo={})
    print(f"The {n}th fibonacci number is: {result}")
    
    n = 20
    result = fibonacci_memo(n, memo={})
    print(f"The {n}th fibonacci number is: {result}")
    
    n = 30
    result = fibonacci_memo(n, memo={})
    print(f"The {n}th fibonacci number is: {result}")
    
    
    
    
    
if __name__ == "__main__":
    main()