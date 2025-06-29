class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Stores the length of the array so we only have to calculate it once
        n = len(nums)
        # Creates an array of length n, all with default value 1 for our prefix suffix method
        res = [1] * n

        # Loops through the array forwards, storing the prefix products in the results array
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]
        # Creates a suffix variable so that it can be stored outside hte loop
        suffix = 1
        for i in range(n - 2, -1, -1):
            # Updates the suffix product
            suffix *= nums[i + 1]
            # Multiplies our prefix products by the suffix product
            res[i] *= suffix
        # Returns our final array
        return res