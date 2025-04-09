### Dynamic Programming

Definition of Terms:
- Steps:
- 1. Form a State. -> f(x, y, z ...). 
- 2. Forming a recursive relation. e.g. fibonacci number: f(n) -> f(n-1) + f(n-2). This part is also called Optimal Substructure. 
- 3. Overlapping Subproblems. Tabulation (fixed size, static, not go to any state twice) and Memoization(saving and reusing, memopad).


Tabulation and Memoization:
- Tabulation: Bottom up approach. Fill the table from the bottom up.
- Memoization: Top down approach. Recursion with memoization.
- Tabulation is usually faster than memoization because it avoids the overhead of recursive function calls.
- Memoization is usually easier to implement because it follows the natural recursive structure of the problem.
- Tabulation is usually more space efficient because it uses a fixed size table, while memoization can use a lot of space if the recursion goes deep.
- Memoization can be more intuitive for problems that have a clear recursive structure, while tabulation can be more intuitive for problems that have a clear iterative structure.
- Memoization can be more difficult to debug because it can lead to stack overflow errors if the recursion goes too deep, while tabulation is usually easier to debug because it uses a fixed size table.
- Memoization can be more difficult to optimize because it can lead to a lot of function calls, while tabulation is usually easier to optimize because it uses a fixed size table.
- Memoization can be more difficult to parallelize because it can lead to a lot of function calls, while tabulation is usually easier to parallelize because it uses a fixed size table.
- Memoization can be more difficult to test because it can lead to a lot of function calls, while tabulation is usually easier to test because it uses a fixed size table.


## Recusrion is Everywhere.
- DP = Recursion + Optimization.
- e.g. Number of ways to fill an array with 0's and 1's sucht that there are no consecutive ones.
  - f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(0). This is a recursive relation.
    - First, find a state. f(n) = number of ways to fill an array of size n with 0's and 1's such that there are no consecutive ones.
    - Second, find a recursive relation. f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(0). This is a recursive relation.
    - Third, find a base case. f(0) = 1, f(1) = 2, f(2) = 3, f(3) = 5. This is a base case.
    - Fourth, optimize.i.e. Memoization or Tabulation works. 
