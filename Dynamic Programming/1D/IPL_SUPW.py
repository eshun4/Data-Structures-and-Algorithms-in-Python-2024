"""
In IPL 2025, the amount that each player is paid varies from match to match.
The match fee depends on the quality of opposition, the venue etc.

The match fees for each match in the new season have been announced in advance. Each team has to enforce a 
mandatory rotation policy so that no player ever plays three matches in a row during a season.

Nikhi is the captain and chooses the team for each match. He wants to allocate a
playing schedule for himself to maximize his earnings through match fees during the season. The

"""

"""
No player can play three matches in a row.
game1, game2, _
game1, _, game3,
_, game2, game3 

Options:
1. if n games are possble we can pick the first game and the second game = f(n) = n-2 + n - 1 + dp[n-3]
2. If n games are availble we can pick the first game and the third game = f(n) = n - 2 + n - 3 + dp[n - 1]
3. If n games are available we can pick the second and the third game = f(n) = n - 1 + n - 3 + dp[n - 2]

Base cases:
1. If n = 0, return 0
2. if n == 1, return time[0]
3. if n == 2, return max(time[0] + time[1], time[1] + time[2], time[0] + time[2])  
"""
from typing import List

def cannotPlayThreeMatchesInARow(time: List[int]) -> int:
    # Get the length of the elements in the array
    n = len(time)
    
    # Check the base cases
    if n == 0:
        return 0
    elif n == 1:
        return time[0]
    elif n == 2:
        return time[0] + time[1]
    
    # Create dp array or table
    dp = [0] * n 
    
    # Check the base cases 
    dp[0]  = time[0]
    dp[1]  = time[0] + time[1]
    dp[2]  = max(time[0] + time[1], time[1] + time[2], time[0] + time[2])
    
    # Iterate when the number is greater than 3 and populate the dp table
    for i in range(3, n):
        dp[i] = max(time[i - 2] + time[i - 1] + dp[i - 3], time[i - 2] + time[i - 3] + dp[i - 1], time[i - 1] + time[i - 3] + dp[i - 2])
        
    return dp[n - 1]

def main():
    # Example test cases
    time1 = [1, 2, 3]
    print(f"Maximum total time for {time1} is: {cannotPlayThreeMatchesInARow(time1)}")

    time2 = [10, 1, 10, 1, 10]
    print(f"Maximum total time for {time2} is: {cannotPlayThreeMatchesInARow(time2)}")

    time3 = [5, 15, 10, 20, 25, 30]
    print(f"Maximum total time for {time3} is: {cannotPlayThreeMatchesInARow(time3)}")

    time4 = [3, 6, 8, 7, 6, 5, 4]
    print(f"Maximum total time for {time4} is: {cannotPlayThreeMatchesInARow(time4)}")

    time5 = [50, 40, 30, 20, 10]
    print(f"Maximum total time for {time5} is: {cannotPlayThreeMatchesInARow(time5)}")

    time6 = [100, 200, 300, 400, 500, 600, 700]
    print(f"Maximum total time for {time6} is: {cannotPlayThreeMatchesInARow(time6)}")
    
if __name__ == "__main__":
    main()


