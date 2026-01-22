class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while True:
            if len(nums) <= 1:
                return ops
            
            isSorted = True
            minPair, minn = (-1, -1), float('inf')
            for i in range(len(nums) - 1):
                if nums[i] + nums[i+1] < minn:
                    minn = nums[i] + nums[i+1]
                    minPair = (i, i+1)
                if nums[i] > nums[i+1]:
                    isSorted = False
            
            if isSorted:
                return ops
            
            ops += 1
            nums.pop(minPair[1])
            nums[minPair[0]] = minn