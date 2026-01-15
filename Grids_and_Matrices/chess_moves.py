"""
Problem 28.1 - Chess Moves

For context, this is how the King, Knight, and Queen move on a chessboard:

Chess moves 1
The king can go to any adjacent cell, including diagonals. The knight 'jumps' one 
cell in one dimension and two in the other, even if there are pieces in between. 
The queen can move any number of cells in any direction, including diagonals, 
but cannot go through occupied cells.

We are given three inputs:

a. board, an nxn binary grid, where a 0 denotes an empty cell,
1 denotes an occupied cell (for this problem, it doesn't matter what piece is in it)

b. piece, which is one of "king", "knight", or "queen"

c. r and c, with 0 ≤ r < n and 0 ≤ c < n, which denote an unoccupied position in the board

-- Return a list of all the unoccupied cells in board that can be reached by the given piece in one move starting from [r, c]. The order of the output cells does not matter.


Example 1:
board = [[0, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]
piece = "king"
r = 3
c = 5
Output: [[2, 5], [3, 4], [4, 4], [4, 5]]

Example 2:
board = [[0, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]
piece = "knight"
r = 4
c = 3
Output: [[2, 2], [3, 5], [5, 5]]

Example 3:
board = [[0, 0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]
piece = "queen"
r = 4
c = 4
Output: [[3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5], [5, 3], [5,
4], [5, 5]]
Chess moves 2
Constraints:

1 ≤ n ≤ 100
board[i][j] is either 0 or 1
0 ≤ r, c < n
piece is one of "king", "knight", or "queen"
"""

def is_valid(board, r, c):
    """ This function checks to see if player can 
    make a valid move without going out of bounds.
    
    The player can only make  avove when the adjacent spont is not 1 (unfilled)."""
    return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != 1

def chess_moves(board, piece, r, c):
    "This function tracks the moves the player can make from their current position."
    # first analyze the directions the users can make
    # depending on different pieces users can ,ake different moves
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    # knight directions 
    king_directions = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
    # knight directions
    knight_directions = [[1, 2], [-1, -2], [-1, 2], [1, -2], [2, 1], [-2, -1], [2, -1], [-2, 1]]
    
    # moves array 
    moves = []

    if piece == "king":
        directions += king_directions
    elif piece == "knight":
        directions = knight_directions
    elif piece == "queen":
        directions = king_directions +  directions
        
    # iterate through the directions and append moves based on piece t moves array
    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        if piece == "king" or piece == "knight":
            if is_valid(board, new_r, new_c):
                moves.append([new_r, new_c])
        if piece == "queen":
            while is_valid(board, new_r, new_c):
                moves.append([new_r, new_c])
                new_r += dr 
                new_c += dc
                
    # return the moves
    return moves
            
    

def main():
    test_cases = [
    # 1. King at (3,5) on example board
    ([[0, 0, 0, 1, 0, 0],
      [0, 1, 1, 1, 0, 0],
      [0, 1, 0, 1, 1, 0],
      [1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0]], "king", 3, 5,
     [[2, 5], [3, 4], [4, 4], [4, 5]]),

    # 2. Knight at (4,3) on example board
    ([[0, 0, 0, 1, 0, 0],
      [0, 1, 1, 1, 0, 0],
      [0, 1, 0, 1, 1, 0],
      [1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0]], "knight", 4, 3,
     [[2, 2], [3, 5], [5, 5]]),

    # 3. Queen at (4,4) on example board (queen rays only)
    ([[0, 0, 0, 1, 0, 0],
      [0, 1, 1, 1, 0, 0],
      [0, 1, 0, 1, 1, 0],
      [1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0]], "queen", 4, 4,
     [[3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5], [5, 3], [5, 4], [5, 5]]),

    # 4. King at edge (top-left corner) - (1,1) is occupied so excluded
    ([[0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]], "king", 0, 0,
     [[0, 1], [1, 0]]),

    # 5. Knight at edge (bottom-right) - FIXED board so start is unoccupied
    ([[0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]], "knight", 3, 3,
     [[1, 2], [2, 1]]),

    # 6. Queen at edge (right edge)
    ([[0, 0, 1],
      [0, 0, 0],
      [1, 0, 0]], "queen", 1, 2,
     [[0, 1], [1, 0], [1, 1], [2, 1], [2, 2]]),

    # 7. King with heavy blocks around
    ([[1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]], "king", 1, 1,
     []),

    # 8. Knight from center (all 8 landings are valid/unoccupied)
    ([[0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0]], "knight", 2, 2,
     [[0, 1], [0, 3], [1, 0], [1, 4], [3, 0], [3, 4], [4, 1], [4, 3]]),

    # 9. Queen at (0,0) (includes diagonal ray too)
    ([[0, 0, 0, 1],
      [0, 0, 1, 0],
      [0, 1, 0, 0],
      [1, 0, 0, 0]], "queen", 0, 0,
     [[0, 1], [0, 2], [1, 0], [2, 0], [1, 1], [2, 2], [3, 3]]),

    # 10. Small board (1x1, no moves)
    ([[0]], "king", 0, 0,
     []),
]

    
    for i, (board, piece, r, c, expected) in enumerate(test_cases, 1):
        got = chess_moves(board, piece, r, c)
        print(f"Test {i}: Piece={piece}, Pos=({r},{c})")
        print(f"  Expected: {expected}")
        print(f"  Got:      {got}")
        print(f"  Match:    {set(tuple(x) for x in got) == set(tuple(x) for x in expected)}\n")


if __name__ == "__main__":
    main()