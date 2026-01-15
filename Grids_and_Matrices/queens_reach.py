"""
Problem 28.2 - Queen's Reach


Imagine that an n x n chessboard has a number of queens in it. Remember that in chess, a queen can move any number of cells horizontally, vertically, or diagonally.

We are given an nxn binary grid, board, with n > 0, where 0 indicates that the cell is unoccupied, and a 1 indicates a queen (the color of the queen doesn't matter). Return a binary board with the same dimensions. In the returned board, 0 denotes that a cell is 'safe', and a 1 denotes that a cell is not safe. A cell is safe if there isn't a queen in it and no queen on the board can reach it in a single move.


Example 1:
board = [[0, 0, 0, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 0, 0, 0]]
Output: [[1, 1, 1, 1],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [1, 1, 1, 1]]

Example 2:
board = [[1]]
Output: [[1]]
Explanation: The only cell has a queen, so it's not safe.

Example 3:
board = [[0]]
Output: [[0]]
Explanation: With no queens, all cells are safe.
Queens reach 1
Constraints:

1 ≤ n ≤ 100
board[i][j] is either 0 or 1
"""
def is_valid(board, r, c):
    """This verifies in the adjacent cell we want to check is open for us to make a move.
    1 for unopen and 0 for open. If its open meaning there is no queen occupying that position
    """
    return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != 1

def queens_reach(board):
    # get the row and the column
    row, col = len(board), len(board[0])
    # create a directions array for our queen
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    # next create a result bit board for the output 
    # here we want 1 to denote it was safe to move a queen to that position. So in the case there was already a queen there leave it as it is.
    # since the question did nto specify to do anything when we encounter a spot already occupied by a queen
    results = [row[:] for row in board]
    # since iterate through the directions array
    for r in range(row):
        for c in range(col):
            if board[r][c] == 1:
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc 
                    while is_valid(board, new_r, new_c):
                        results[new_r][new_c] = 1 
                        new_r += dr 
                        new_c += dc 
    # return results
    return results
                        
                        
            
    

def main():
    test_cases = [
        (
            [[0, 0, 0, 1],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 0, 0, 0]],
            [[1, 1, 1, 1],
             [1, 0, 1, 1],
             [1, 1, 0, 1],
             [1, 1, 1, 1]]
        ),
        ([[1]], [[1]]),
        ([[0]], [[0]]),

        # FIXED expected outputs (these boards have NO safe cells)
        ([[0, 1], [0, 0]], [[1, 1], [1, 1]]),
        ([[1, 0], [0, 0]], [[1, 1], [1, 1]]),
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        ([[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
         [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]),

        ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
         [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),

        ([[1, 1], [1, 1]], [[1, 1], [1, 1]])
    ]

    for i, (board, expected) in enumerate(test_cases, start=1):
        result = queens_reach(board)
        if result != expected:
            print(f"❌ Test case {i} FAILED")
            print(f"Expected: {expected}")
            print(f"Got:      {result}")
        else:
            print(f"✅ Test case {i} passed")

if __name__ == "__main__":
    main()