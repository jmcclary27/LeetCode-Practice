class Solution:
    from collections import Counter
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        firstCounter, secondCounter = Counter(nums1), Counter(nums2)
        res = []
        for key, val in secondCounter.items():
            if key in secondCounter:
                num = min(firstCounter[key], secondCounter[key])
                temp = [key] * num
                res.extend(temp)
        return res