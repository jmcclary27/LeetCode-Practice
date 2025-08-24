class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Creates our result variable and initializes it to 0
        res = 0
        # Creates a dictionary to keep track of the original order before sorting
        order = {}
        # Puts the cars in the order dictionary with the key being their position and the values being their speed
        for i in range(len(position)):
            order[position[i]] = speed[i]
        # Sorts initial position array
        position.sort()
        # Creates our stack
        stack = []
        # Loops with the iterator counting down from 1 minus the length of the position array to 0
        for i in range(len(position) - 1, - 1, - 1):
            # Calculates how long it takes for the ith car to reach the target distance
            time = (target - position[i]) / order[position[i]]
            # Executes if the stack is not empty and our current time is greater than the time at the end of the stack
            # If the time is greater than the end of the stack, that means the fleet will reach target before the ith car
            if stack and time > stack[-1]:
                # Empties the stack (the fleet)
                while stack:
                    stack.pop()
                # Increments res
                res += 1
            # Executes if the stack is not empty (time <= stack[-1])
            if stack:
                # Changes the current time to equal the largest time in the stack
                time = max(stack[-1], time)
            # Adds time to the stack
            stack.append(time)
        # Checks edge case of the loop finishing and there still being a fleet in the stack
        if stack:
            return res + 1
        # Returns the result
        return res