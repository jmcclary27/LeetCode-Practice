class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Creates two pointers at the first two indexes
        l, r = 0, 1
        # Creates a variable to store the max possible profit
        maxP = 0

        # Loops until r has reached the end of the array
        while r < len(prices):
            # Checks if the price at l is lower than the price at r
            if prices[l] < prices[r]:
                # Adds their difference to profit
                profit = prices[r] - prices[l]
                # Makes the max profit the larger between profit and the current max profit
                # This is done to make sure you don't buy and sell multiple times
                maxP = max(maxP, profit)
            # Executes if the price at r is lower than the price at l
            else:
                # Moves l up to r
                l = r
            # Increments r
            r += 1
        # Returns the max profit
        return maxP