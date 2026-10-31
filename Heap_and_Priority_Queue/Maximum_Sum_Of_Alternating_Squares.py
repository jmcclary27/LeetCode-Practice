class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, abs(num))
        
        n = len(nums)
        res = [0] * n
        for i in range(1, n, 2):
            res[i] = heapq.heappop(heap)
        for i in range(0, n, 2):
            res[i] = heapq.heappop(heap)
        
        final = 0
        for i in range(n):
            if i % 2 == 0:
                final += (res[i] ** 2)
            else:
                final -= (res[i] ** 2)
        return final