def generate_parenthesis(n):
    """
    Generates all combinations of well-formed parentheses.

    This function is intended to generate all possible valid combinations
    of parentheses for a given number of pairs. It uses backtracking to 
    explore all potential combinations and ensures that only valid 
    configurations are included in the result.

    Returns:
        list: A list of strings, where each string represents a valid 
        combination of well-formed parentheses.
    """
    def backtracking(output, n, opening, close, index, solutions):
        # base case
        if index == 2*n:
            solutions.append(output)
            return

        if opening < n:
            backtracking(output + "(", n, opening + 1 , close, index + 1, solutions)

        if close < opening:
            backtracking(output + ")", n, opening, close + 1 , index + 1, solutions)

    output = ""
    opening = 0
    close = 0
    index = 0
    solutions = []
    backtracking(output, n, opening, close, index, solutions)
    return solutions

def main():
    n = 3
    result = generate_parenthesis(n)
    print(f"All combinations of well-formed parentheses for {n} pairs are:")
    print(result)
    print("*****************************************************************************")
    n = 2
    result = generate_parenthesis(n)
    print(f"All combinations of well-formed parentheses for {n} pairs are:")
    print(result)

if __name__ == "__main__":
    main()