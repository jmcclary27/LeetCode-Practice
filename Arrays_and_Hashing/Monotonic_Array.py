class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)

        if n <= 1:
            return True
        
        inc, dec = False, False
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                dec = True
            elif nums[i] < nums[i + 1]:
                inc = True
        
        return not (inc and dec)