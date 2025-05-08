"""
There are N stons given in the form of an array, each element in the array represents the height
of the ith stone. There is a frog who is initially on stone 1.

Frog will repeat the following actions one number of timesto reach stone N:

1. If the frog is currently on stone i, hump to stone i + 1 
or stone i + 2, there the ith cost of |hi - hj| is incurred, where j is the stone to land on.

"""



def frog_min_cost(stones):
    # get the length of the stones array
    n = len(stones)
    # create a dp array of size n
    dp = [0] * n
    # base case, the first stone has no cost
    dp[0] = 0
    # the second stone has a cost of |h1 - h2|
    dp[1] = abs(stones[0] - stones[1])
    # iterate through the stones array from the 3rd stone to the last stone
    for i in range(2, n):
        # calculate the cost of jumping from the previous stone and the stone before that
        jump_one = dp[i - 1] + abs(stones[i] - stones[i - 1])
        jump_two = dp[i - 2] + abs(stones[i] - stones[i - 2])
        # take the minimum of the two costs
        dp[i] = min(jump_one, jump_two)
    # return the cost of reaching the last stone
    return dp[n - 1]

def main():
    # Example 1:
    stones = [10, 30, 40, 50, 20]
    print(f"Minimum cost to reach the last stone: {frog_min_cost(stones)}")

    # Example 2:
    stones = [10, 20, 30, 10]
    print(f"Minimum cost to reach the last stone: {frog_min_cost(stones)}")

if __name__ == "__main__":
    main()