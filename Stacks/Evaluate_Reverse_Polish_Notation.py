class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initializes stack.
        stack = []
        # Loops through the list token by token.
        for c in tokens:
            # Performs checklist of if statements to check for each of the four possible symbols.
            # If one of the four symbols is found, then their mathematical function is performed.
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # Assigns the two most recent pops to variables so the order can be flipped.
                # Order does not matter in addition and multiplication, so this is only done on subtraction and diviion.
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            # Adds the token (converted to an integer) to the stack if it is not one of the four symbols
            else:
                stack.append(int(c))
        # Returns our final answer
        return stack[0]