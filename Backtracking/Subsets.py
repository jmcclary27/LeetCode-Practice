class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Defines nested backtracking function with the parameters being the starting index and current stack
        def backtrack(start, stack):
            # Append current stack to res (Uses list manipulation to make a shallow copy)
            res.append(stack[:])
            # Loops from the start variable to the end of nums
            for i in range(start, len(nums)):
                # Adds the current number to the stack
                stack.append(nums[i])
                # Calls our backtracking function with start incremented and stack with the new number
                backtrack(i + 1, stack)
                # Pops most recent number in stack (backtracking)
                stack.pop()
        # Creates the result list
        res = []
        # Calls backtrack with a 0 index and an empty stack
        backtrack(0, [])
        # Returns the result
        return res