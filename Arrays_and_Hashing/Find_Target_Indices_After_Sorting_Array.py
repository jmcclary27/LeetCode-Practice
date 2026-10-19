class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []
        less, equal = 0, 0
        for i in range(len(nums)):
            if nums[i] == target:
                equal += 1
            elif nums[i] < target:
                less += 1
        while equal > 0:
            res.append(less)
            less += 1
            equal -= 1
        return res