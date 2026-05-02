class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minn = float('inf')
        L, R = 0, k - 1
        while R < len(nums):
            minn = min(minn, nums[R] - nums[L])
            L += 1
            R += 1

        return minn