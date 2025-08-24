class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Creates the minheap (nums) and k value for the class
        self.minHeap, self.k = nums, k
        # Heapifies the minHeap
        heapq.heapify(self.minHeap)
        # Removes the smallest element until there are k elements left
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Adds the new value to the heap
        heapq.heappush(self.minHeap, val)
        # Removes the smallest value if the length is larger than k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Returns the first element in the minHeap (the smallest element)
        return self.minHeap[0]