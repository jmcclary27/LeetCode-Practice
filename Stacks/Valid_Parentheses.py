class Solution:
    def isValid(self, s: str) -> bool:
        # Creates a dictionary of all the symbol pairs
        pairs = {"{" : "}", "(" : ")", "[" : "]"}
        # Creates an empty stack
        stack = []
        # Checks to see if s is empty and returns false if it is
        if s[0] not in pairs:
            return False
        
        # Loops through s
        for i in range(len(s)):
            # If the current symbol is open, then add it to the stack
            if s[i] in pairs:
                stack.append(s[i])
            # Executes if the symbol is closed
            else:
                # Checks if there is nothing on the stack but we have encountered a closed symbol
                if len(stack) == 0:
                    return False
                # Checks the last thing on the stack is a pair for the most recent part of the string
                elif pairs[stack[-1]] == s[i]:
                    stack.pop()
                    continue
                return False
        # Makes sure the stack is now empty
        if len(stack) != 0:
            return False
        return True
                