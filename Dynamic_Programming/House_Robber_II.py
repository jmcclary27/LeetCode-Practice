class Solution:
    def rob(self, nums: List[int]) -> int:
        def robAcyclic(nums):
            ''' House Robber I algorithm '''
            # Creates backMax to keep track of the max from at least two houses back
            # Creates currMax to keep track of the max at position i
            backMax, currMax = 0, 0
            # Loops for the length of nums
            for i in range(len(nums)):
                # Adds backMax to the current position
                nums[i] += backMax
                # Finds the current maximum
                currMax = max(currMax, nums[i])
                # Finds the current backMax (checks to make sure we are not at the beginning of the array)
                if i != 0:
                    backMax = max(backMax, nums[i-1])
            # Returns the current maximum
            return currMax
        # Returns the max of of the acyclic algorithm either without the first element or without the last
        # (Edge case) could also return the start of the array if the length is one
        return max(nums[0], robAcyclic(nums[:-1]), robAcyclic(nums[1:]))