class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        n = len(arr)
        res = [0] * n
        minheap = []
        for i, val in enumerate(arr):
            heapq.heappush(minheap, (val, i))
        prev = None
        rank = 0
        while minheap:
            val, idx = heapq.heappop(minheap)
            if prev is None or val != prev:
                rank += 1
            res[idx] = rank
            prev = val
        return res