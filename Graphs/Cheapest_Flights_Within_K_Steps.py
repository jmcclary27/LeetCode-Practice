class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        res = float('inf')

        for flight in flights:
            adj[flight[0]].append([flight[1], flight[2], float('inf')])
        
        minheap = [(-1, 0, src)]
        while minheap:
            dist, price, node = heapq.heappop(minheap)
            if node == dst and dist <= k:
                res = min(res, price)
                continue
            if dist > k:
                continue
            for tupes in adj[node]:
                if tupes == []:
                    continue
                newPrice = tupes[1] + price
                if newPrice < tupes[2]:
                    tupes[2] = newPrice
                heapq.heappush(minheap, (dist+1, tupes[2], tupes[0]))

        return res if res != float('inf') else -1