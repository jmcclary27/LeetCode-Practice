class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        prev = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 == prev:
                return False
            prev = nums[i] % 2
        
        return True