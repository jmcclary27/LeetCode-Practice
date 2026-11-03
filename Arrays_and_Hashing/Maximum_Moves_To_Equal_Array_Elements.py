class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxx = max(nums)
        res = 0
        for num in nums:
            res += maxx - num
        return res