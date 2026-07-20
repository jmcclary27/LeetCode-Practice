class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        j, curr = 0, 0
        while curr < len(nums):
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)
            else:
                j += 1
            curr += 1
        return nums