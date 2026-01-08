class Solution:
    def jump(self, nums: List[int]) -> int:
        end = len(nums) - 1
        res, farthest, counter = 0, 0, 0

        for i in range(end):
            if i + counter >= end:
                return res
            if nums[i] > farthest:
                farthest = nums[i]
            if counter == 0:
                counter = farthest
                res += 1
            counter -= 1
            farthest -= 1
        return res