class Solution:
    def majorityElement(self, nums):
        import random
        n = len(nums)
        while True:
            candidate = random.choice(nums)
            if nums.count(candidate) > n // 2:
                return candidate