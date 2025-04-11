"""
### Problem Statement

N-Queend is the problem of placing N chess queens on an N x N chessboard such that no two queens attack each other.

Input:
- An integer N, the size of the chessboard (N x N).

Output:
- A list of all possible solutions, where each solution is represented as a list of integers. Each integer represents the column position of the queen in that row.
- i.e. 2D Matrix with Queens.

In other words return a chessboard where no queen attacks each other in all directions (i.e. row, column, diagonal).
### Examples
Input:
    n = 4   
    
    
Posible Variations of this problem:
- Print one configuration of N-Queens.
- *** Print all configurations of N-Queens. ***
- Count the number of configurations of N-Queens.
"""

def canPlace(board, n, row, col):
    # Check for the column
    for k in range(row):
        if board[k][col] == 'Q':
            return False
        
    # Check left diagonal
    i, j = row, col 
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
        
    # Check right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True


def solve_n_queens(n, board, i, solutions):
    # base case
    if i == n:
        # add the board configuration to solutions
        solutions.append([''.join(row) for row in board])
        return 
    
    # recursive case
    for j in range(n):
        # check if current position is safe or not
        if canPlace(board, n, i, j):
            board[i][j] = "Q"  # place the queen
            success = solve_n_queens(n, board, i + 1, solutions)
            if success:
                return True
            # if not successful, remove the queen (backtrack)
            # backtrack
            board[i][j] = '.'
        
    return False
            

def n_queens(n):
    solutions = []
    solve_n_queens(n, [['.'] * n for _ in range(n)], 0, solutions)
    return solutions


def main():
    n = 4
    solutions = n_queens(n)  # Call the function to solve N-Queens problem
    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    main()
    
    
    
    
    
    
# def canPlace(board, n, row, col):
#     # Check for the column
#     for k in range(row):
#         if board[k][col] == 'Q':
#             return False
        
#     # Check left diagonal
#     i, j = row, col 
#     while i >= 0 and j >= 0:
#         if board[i][j] == 'Q':
#             return False
#         i -= 1
#         j -= 1
        
#     # Check right diagonal
#     i, j = row, col
#     while i >= 0 and j < n:
#         if board[i][j] == 'Q':
#             return False
#         i -= 1
#         j += 1
    
#     return True


# def print_board(board):
#     for row in board:
#         print([' '.join(row)])
#     print()
    
    
# def solve_n_queens(n, board, i):
#     # base case
#     if i == n:
#         # print the board configuration
#         print_board(board)
#         return 
    
#     # recursive case
#     for j in range(n):
#         # check if current position is safe or not
#         # safe meaning no other queen is in the same row, column or diagonal
#         if(canPlace(board,n, i, j)):
#             board[i][j] = "Q"  # place the queen
#             success = solve_n_queens(n, board, i + 1)
#             if success:
#                 return True
#             # backtrack
#             board[i][j] = '.'
            
#     return False


# def n_queens(n):
#     solve_n_queens(n, [['.'] * n for _ in range(n)], 0)


# def main():
#     n = 4
#     n_queens(n) # Call the function to s    olve N-Queens pr    oblem'




# if __name__ == "__main__":
#     main()        