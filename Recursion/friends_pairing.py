"""
### Friend's pairing problem.

Given n friends who wnt to go to a party, each one can remain single or can be paired up with
some other friend. Ech friend cn be paired only once. Find out the total number of ways 
in which friends can remain single or can be paired up.

"""

def friends_pairing(n):
    """
    Count the number of ways to pair up n friends.
    n: the number of friends.
    recurrence relation:
    T(n) = {
        T(n-1) + (n-1) * T(n-2) if n > 2
        1 if n == 0 or n == 1
    }
    """
    if n == 0 or n == 1:
        return 1 
    return friends_pairing(n - 1) + (n - 1) * friends_pairing(n - 2)
    
    

def main():
    n = 5
    result = friends_pairing(n)
    print(f"Number of ways to pair up {n} friends is {result}.")
    n = 4
    result = friends_pairing(n)
    print(f"Number of ways to pair up {n} friends is {result}.")
    n = 3
    result = friends_pairing(n)
    print(f"Number of ways to pair up {n} friends is {result}.")


if __name__ == "__main__":
    main()