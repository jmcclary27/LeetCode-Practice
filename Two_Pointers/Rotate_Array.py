class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums) - k
        nums[k:], nums[0:k] = nums[0:n], nums[n:]