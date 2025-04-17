"""
*** Get Maximum Reward Points. ***

Problem Statement:

Amazon Shopping Periodically has offers to attract more customers.

It recently launched an offer for n iitems in its inventory, where the ith item offered reward[i] 
reward points to the customer purchasing the item. Every time an offer-bearing item is purchased,
the customer gains the reward points associated with that item. Then the reward points of the
remaining items are reduced by 1 unless it will reduce the points below 0. 

Find the maximum possible reward points that can be gathered by purchasing items optimally.

Note: Each item can be purchased at most once, in other words reward[i] becomes 0 after the ith
item is purchased. 

** Example **

Consider the number of items to be n = 5, and their reward points to be reward = [5, 2, 2, 3, 1].
The items an be purchased as follows:

    - 5, 2, 2, 3, 1 - > point = 2, Total points earned: 2.
    - 4, 1, 0, 2, 0 - > point = 2, Total points earned: 4
    - 3, 0, 0, 0, 0 - > point = 3, Total points earned: 7

Finally point = 0 , 0, 0, 0, 0, 0 -> 
                output: 2 + 2 + 3 = 7

At this point, no items have reward points left. 
The maximum reward points is 2 + 2 + 3 = 7

** Function Description ***
Complete the Function

getMaximumRewardPoints has the following parameters:

    int reward[n]: the reward points for each item
    
    Returns long_int: the maximum points which can be collected.
    
Constraints.

    1 <= n <= 10 **5
    0 <= reward[i] <= 10 ** 6    
    
"""


def getMaximumRewardPoints(reward):
    """
    Calculate the maximum reward points that can be collected by purchasing items optimally.

    Args:
        reward (list[int]): A list of integers representing the reward points for each item.

    Returns:
        int: The maximum reward points that can be collected.
    """
    # Sort the reward points in descending order to prioritize higher rewards first
    reward.sort(reverse=True)
    
    # Initialize the total reward points collected
    total = 0
    
    # Iterate through the sorted reward list
    for i in range(len(reward)):
        # Calculate the contribution of the current item after reducing by its index
        contribution = reward[i] - i
        
        # Only add the contribution if it is greater than 0
        if contribution > 0:
            total += contribution
    
    # Return the total reward points collected
    return total



# *** Not optimal enough because it involves making choices
# def getMaximumRewardPoints(reward):
#     """
#     Analyze the question:
#     - optimally: in this case where we compare items at each iteration for the max points.
#     - after an iteration set the value at that index to 0
#     - reduce the other numbers by 1 
#     - repeat the steps until all elements have it 0 base case
#     """
#     # get the lenght of n
#     n = len(reward)
#     # create if clauses
#     if n == 0:
#         return 0
#     if n == 1:
#         return reward[0]
#     if n == 2:
#         return max(reward[0], reward[1])
    
#     # Create a dp array
#     dp = [0] * n
    
#     # create base cases
#     dp[0] = reward[0]
#     dp[1] = max(reward[0], reward[1])
#     dp[2] = max(reward[0] + reward[1], reward[1] + reward[2], reward[2] + reward[0])
    
#     # Populate the dp table
#     for i in range(3, n):
#         # Use the recurrence relation
#         dp[i] = max(dp[i - 2] + reward[i], dp[i - 3] + reward[i])
#     return dp


def main():
    import sys
    test_cases = [
        # Provided example
        ([5, 2, 2, 3, 1], 7),
        
        # Edge cases
        ([0], 0),
        ([10**6], 10**6),
        ([0, 0, 0, 0], 0),
        
        # Basic scenarios
        ([3, 2, 1], 3 + 1),
        ([5, 4, 3, 2, 1], 5 + 3 + 1),
        ([1, 1, 1], 1),
        ([10, 9, 8, 7, 6], 10 + 8 + 6 + 4 + 2),
        
        # Medium-sized cases
        ([10**6] * 100, sum(max(10**6 - i, 0) for i in range(100))),
        (list(range(10**4, 0, -1)), sum(max(x - i, 0) for i, x in enumerate(sorted(range(10**4, 0, -1), reverse=True)))),
        
        # Large input simulation (conceptual)
        # ([10**6] * 10**5, (10**6 + (10**6 - 10**5 + 1)) * 10**5 // 2)
    ]

    for i, (input_case, expected) in enumerate(test_cases):
        try:
            result = getMaximumRewardPoints(input_case)
            assert result == expected, f"FAILED (expected {expected}, got {result})"
            print(f"Test {i+1}: Passed")
        except AssertionError as e:
            print(f"Test {i+1}: {e}")
            sys.exit(1)

    print("All test cases passed!")

if __name__ == "__main__":
    main()
