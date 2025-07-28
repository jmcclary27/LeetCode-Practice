class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Creates our result array that is the length of the temperatures list
        res = [0] * len(temperatures)
        # Creates our stack
        stack = []  # pair: [temp, index]

        # Enumerates through temperatures with i as the index and t as the temperature
        for i, t in enumerate(temperatures):
            # Loops while the stack is not empty and the temperature is greater than the most recent temp in the stack
            while stack and t > stack[-1][0]:
                # Creates a variable holding the index of the most recent temperature from the stack
                stackInd = stack.pop()
                # Adds the difference between the current index and the variable's index to our resulting array
                res[stackInd] = i - stackInd
            # Adds the newest data to the stack
            stack.append((t, i))
        # Returns the resulting array
        return res