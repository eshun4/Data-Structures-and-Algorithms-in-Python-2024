"""
Problem 28.3 - Spiral Order

Given a positive and odd integer n, return an nxn grid of integers filled as follows: 
the grid should have every number from 0 to n^2 - 1 
in spiral order, starting by going down from the center 
and turning clockwise.


Example 1:
n = 5
Output: [[16, 17, 18, 19, 20],
         [15,  4,  5,  6, 21],
         [14,  3,  0,  7, 22],
         [13,  2,  1,  8, 23],
         [12, 11, 10,  9, 24]]

Example 2:
n = 1
Output: [[0]]

Example 3:
n = 3
Output: [[4, 5, 6],
         [3, 0, 7],
         [2, 1, 8]]
Spiral order 1
Constraints:

0 < n < 1000
n is odd
"""

def is_valid(board, r, c):
    """ Check for the boundaries of board."""
    return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 0

def spiral_order(n):
    # create a resulyt board of size n by n
    result = [[0] * n for _ in range(n)]
    # create a directions array
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    # iterate through the result array and set the values to numbers following the specified directions
    val = n * n - 1
    # r, c
    r, c = n - 1, n - 1
    # direction 
    diri = 0 #start by going up
    # iterate through dr, dc
    while val > 0:
        result[r][c] = val 
        val -= 1 
        if not is_valid(result, r + directions[diri][0], c + directions[diri][1]):
            diri = (diri + 1) % 4 #change directions counterclockwise 
        r, c = r + directions[diri][0], c + directions[diri][1]
    return result
    
      

# 10 test cases (inputs)
test_cases = [1, 3, 5, 7, 9, 11, 13, 15, 21, 99]

def main():
    for i, n in enumerate(test_cases, 1):
        print(f"\n--- Test {i}: n = {n} ---")
        grid = spiral_order(n)
        # Print small ones fully; big ones just show corners + center to avoid huge output
        if n <= 9:
            for row in grid:
                print(row)
        else:
            mid = n // 2
            print("Top-left:", grid[0][0], "Top-right:", grid[0][-1])
            print("Center:", grid[mid][mid])
            print("Bottom-left:", grid[-1][0], "Bottom-right:", grid[-1][-1])

# Call this somewhere (e.g., inside main())
# run_tests()

    

if __name__ == "__main__":
    main()