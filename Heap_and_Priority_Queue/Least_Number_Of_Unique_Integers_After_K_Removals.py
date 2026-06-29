    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hp = list(collections.Counter(arr).values())
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)
        return len(hp) + (k < 0)  