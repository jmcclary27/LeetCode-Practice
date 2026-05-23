class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum, rsum = 0, sum(nums)
        for l in range(len(nums)):
            rsum -= nums[l]
            if lsum == rsum:
                return l
            lsum += nums[l]
            l += 1
        return -1