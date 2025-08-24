class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Creates a variable to keep track of the current minimum
        currMin = 0
        # Loops from position 1 until the end of the array
        for i in range(1, len(cost)):
            # Adds the current minimum (from the last two elements) to the current value in the array
            cost[i] += currMin
            # Finds the new current minimum between the last two elements
            currMin = min(cost[i], cost[i-1])
        # Returns the current minimum
        return currMin