class MinStack:
    def __init__(self):
        # Initializes our stack
        self.stack = []
        # Initializes the stack to keep track of the minimum value at each point
        self.minStack = []

    def push(self, val: int) -> None:
        # Adds val to the main stack
        self.stack.append(val)
        # Checks if there are any values in minStack before trying to index it
        if not self.minStack:
            # Adds val to the minStack if there are no other values in it
            self.minStack.append(val)
            # Executes if minStack is not empty
        else:
            # Finds the minimum between the last value on the minStack and the current value
            val = min(val, self.minStack[-1])
            # Appends the new val to minStack
            self.minStack.append(val)

    def pop(self) -> None:
        # Removes the last element from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Returns the last element of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Returns the last element of the minStack
        return self.minStack[-1]