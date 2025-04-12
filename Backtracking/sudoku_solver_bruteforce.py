# This code isnt efficient for larger or extremely larger test cases. Optimization is needed.


def is_safe(board, row, col, n, number):
    """
    Check if it's safe to place the number in the given cell.
    board: 2D list representing the Sudoku board.
    row: row index of the cell.
    col: column index of the cell.
    n: size of the subgrid.
    number: the number to be placed.
    """
    # Check the row and column
    for i in range(n):
        if board[row][i] == number or board[i][col]== number:
            return False
    # check for subgrid
    start_row = row - row % 3
    start_col = col - col % 3 
    subgrid_n = int(n ** 0.5)  
    for i in range(subgrid_n):
        for j in range(subgrid_n):
            if board[i + start_row][j + start_col] == number:
                return False
    return True

def sudoku_solver(board, row, col, n):
    """
    Solve the Sudoku puzzle using backtracking.
    board: 2D list representing the Sudoku board.
    col: number of columns of the board.
    row: number of rows of the board.
    n: size of the subgrid.
    """
    # Base cases
    if row == n:
        # print solution here
        return True
    
    if col == n:
        return sudoku_solver(board, row + 1, 0, n)
    
    # recursive case
    if board[row][col] != 0:
        return sudoku_solver(board, row, col + 1, n)
    
    # call to be filled
    for number in range(1, n + 1):
        # check if it is safe to place the number
        if is_safe(board, row, col, n, number):
            # place number
            board[row][col] = number
            # call to be filled
            solve_sub_problem = sudoku_solver(board, row, col + 1, n)
            # check if it is solved
            if solve_sub_problem:
                return True
            # backtrack if not solved
            board[row][col] = 0
            
    return False
    
    
    
     
    


def main():
    n = 9
    # Case 1: Solvable Sudoku puzzle
    board1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    print("Case 1:")
    if sudoku_solver(board1, 0, 0, n):
        print("Sudoku solved successfully!")
        for row in board1:
            print(row)
    else:
        print("No solution exists for the given Sudoku puzzle.")

    # Case 2: Unsolvable Sudoku puzzle
    board2 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 8]  # Invalid row (two 8s)
    ]
    print("\nCase 2:")
    if sudoku_solver(board2, 0, 0, n):
        print("Sudoku solved successfully!")
        for row in board2:
            print(row)
    else:
        print("No solution exists for the given Sudoku puzzle.")

    # Case 3: Already solved Sudoku puzzle
    board3 = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    print("\nCase 3:")
    if sudoku_solver(board3, 0, 0, n):
        print("Sudoku solved successfully!")
        for row in board3:
            print(row)
    else:
        print("No solution exists for the given Sudoku puzzle.")

    # Case 4: Extremely large Sudoku puzzle (16x16 grid)
    board4 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print("\nCase 4:")
    if sudoku_solver(board4, 0, 0, 16):
        print("Sudoku solved successfully!")
        for row in board4:
            print(row)
    else:
        print("No solution exists for the given Sudoku puzzle.")
            

if __name__ == "__main__":
    main()