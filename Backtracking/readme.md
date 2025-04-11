### Backtracking

- Algorith Technique in which we recursively try to build solutions to a problem usually by searching the entire search space to solve a computation problem.
  - Problem types:
    - Decision Problemn: check for feasible solution. e.g. is there a path from A to B?
    - Optimization Problem: find the best solution. e.g. find the shortest path from A to B at a min cost.(i.e. Travelling salesman problem).
    - Enumeration Problem: find all solutions. e.g. find all paths from A to B.(i.e. Permutation problem, Rat in maze, N-queen problems, Sudoku Solver, Knights Towers).
    - Counting Problem: count the number of solutions. e.g. count the number of paths from A to B.
- `
    class Solution:
        def subsets(self, nums: List[int]) -> List[List[int]]:
            """# The process
            # 1. Get the base case
            # 2. Get the recursive case.
            #   a. Decide to include a character
            #   b. Decide to exclude a character

            # Start off by choosing the state variables to keep track of the states.
            # Since the input array has been given, I need another 2 arrays to keep track of the current state of the
            # recursion and all the elements and another to return the results. i.e. call them res & sol = [], []
            # We also need the length of the number of elements in the array to keep track of when the recursion has completed moving
            # from one element to another
            # I need n index to keep track of the current element I am on
            """
            # get the length of the array
            n = len(nums)
            # crate two arrys to keep track of the state and the final result
            sol, res = [], []

            # Create a backtracking method that keeps track of the index of the current element
            def backtracking(index):
                # Base case 
                if index == n:
                    res.append(sol[:])
                    return # We dont return anything since the recursive loop ends here
            
                # Recursive case
                # If character is included
                sol.append(nums[index])
                backtracking(index + 1)

                # If the character is not included
                sol.pop() #to return to the previous state of the recursive loop
                backtracking(index + 1)

            # Finally call the backtracking method and return results
            backtracking(0) # starting from the first element
            return res
- `