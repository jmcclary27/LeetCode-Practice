class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Creates teh stack for each individual answer
        stack = []
        # Creates the resulting list of lists
        res = []

        # Creates a nested function to back track with the count of open and closed parenthesis as the parameters
        def backtrack(openN, closedN):
            # Checks if there are the same amount of open and closed parenthesis and that they are equal to n
            if openN == closedN == n:
                # Joins it to a string and adds it to res
                res.append("".join(stack))
                return
            # Checks if our open count is less than n
            if openN < n:
                # Adds an open parenthesis to the stack
                stack.append("(")
                # Recalls backtrack with the added open parenthesis
                backtrack(openN + 1, closedN)
                # Pops most recent number in the stack (backtracking)
                stack.pop()
            # Checks if our closed count is less than n
            if closedN < openN:
                # Adds a closed parenthesis to the stack
                stack.append(")")
                # Recalls backtrack with the added closed parenthesis
                backtrack(openN, closedN + 1)
                # Pops most recent number in the stack (backtracking)
                stack.pop()
        # Calls backtrack with a 0 open and closed count
        backtrack(0, 0)
        # Returns the result
        return res