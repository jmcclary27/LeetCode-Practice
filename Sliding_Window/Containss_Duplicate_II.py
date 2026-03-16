class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            r = i + 1
            while r - i <= k:
                if r >= len(nums):
                    break
                if nums[i] == nums[r]:
                    return True
                r += 1
        return False