class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        curr = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                curr += 1
        
        return nums