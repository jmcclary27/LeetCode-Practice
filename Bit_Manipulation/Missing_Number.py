class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        perfect, res = 0, 0
        
        for i in range(len(nums)):
            perfect += i + 1
            res += nums[i]
        
        return perfect - res