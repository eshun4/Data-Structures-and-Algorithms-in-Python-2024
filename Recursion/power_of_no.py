

def power(a, n):
    """
    Write a function to find the power of a number, both number and power are given as input.
    
    a: the base number.
    n: the exponent number.
    """
    # Check if n is 0, if so return 1
    if n == 0:
        return 1
    if n == 1:
        return a
    # Else
    return a * power(a, n - 1)


def fastPower(a, n):
    """
    Write a function to find the power of a number, both number and power are given as input.
    
    a: the base number.
    n: the exponent number.
    """
    # Check if n is 0, if so return 1
    if n == 0:
        return 1
    if n == 1:
        return a
    # Else
    half = fastPower(a, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * a
    
    
def fastPower2(a, n):
    """
    Write a function to find the power of a number, both number and power are given as input.
    
    """
    # Check if n is 0, if so return 1
    if n == 0:
        return 1
    if n == 1:
        return a
    # Else
    subProb = fastPower2(a, n // 2)
    subProbSq = subProb * subProb
    if n & 1:
        return subProbSq * a
    return subProbSq    
    

def main():
    n = 10
    a = 2
    result = power(a, n)        
    print(f"The power of {a} to the {n} is: {result}")
    result = fastPower(a, n)
    print(f"The power of {a} to the {n} is: {result}")
    result = fastPower2(a, n)
    print(f"The power of {a} to the {n} is: {result}")     
     
if __name__ == "__main__":
    main()