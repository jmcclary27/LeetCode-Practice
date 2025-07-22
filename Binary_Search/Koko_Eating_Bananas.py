class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Creates our intiial outer bounds for binary search
        low, high = 1, max(piles)
        # Creates a variable to keep track of our minimum number along the way
        res = high
        # Loops until we have searched through all possibilities
        while low <= high:
            # Calculates out middle number
            mid = (low + high) // 2
            # Counter for how many hours to eat the bananas
            total = 0
            # Loops through the piles
            for p in piles:
                # Adds the amount of hours per pile to total
                total += math.ceil(float(p) / mid)
            # Checks if our total hours is less than or equal to h
            if total <= h:
                # Updates res and makes our new high equal to mid - 1
                res = mid
                high = mid - 1
            # Executes if our total number of hours is greater than h (our number was too small)
            else:
                low = mid + 1
        # Returns the final number
        return res
