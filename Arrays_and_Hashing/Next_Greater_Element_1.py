class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                curr = stack.pop()
                seen[curr] = nums2[i]
            stack.append(nums2[i])
            
        while stack:
            curr = stack.pop()
            seen[curr] = -1
        
        res = []
        for num in nums1:
            res.append(seen[num])
        
        return res