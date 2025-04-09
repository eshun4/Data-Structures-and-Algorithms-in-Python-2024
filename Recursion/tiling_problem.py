"""
### Tiling Problem

Given a "4 x n" board and tiles of size "4 x 1", count the number of ways to tile the given board using 4 x 1 tiles.

A tile can either be placed vertically or horizontally. i.e., as a 1 x 4 tile or vertically as a 4 x 1 tile.

input: n 
output: number of ways to tile the board.

"""

def tile_problem(n):
    """
    implement the function to solve the tiling problem.
    n: the length of the board.
    recurrence relation:
    T(n) ={
        T(n-1) + T(n-4) if n > 4
        1 if n <= 3
    }
    }
    """
    if n <= 3:
        return 1
    return tile_problem(n - 1) + tile_problem(n - 4)





def main():
    n = 10
    result = tile_problem(n)
    print(f"Number of ways to tile the board of length {n} is {result}.")
    n = 4

if __name__ == "__main__":
    main()