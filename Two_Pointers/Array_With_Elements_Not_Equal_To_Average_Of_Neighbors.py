class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res = []
        l, r = 0, n - 1
        while l <= r:
            res.append(nums[l])
            if l == r:
                break
            l += 1
            res.append(nums[r])
            r -= 1
        return res