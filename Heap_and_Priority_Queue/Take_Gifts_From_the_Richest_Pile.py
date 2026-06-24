class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-x for x in gifts]
        heapq.heapify(maxHeap)
        
        for _ in range(k):
            n = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -floor(sqrt(n)))

        return -sum(maxHeap)