class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]
        
        maxx = 0
        for i in range(len(customers) - minutes + 1):
            curr = 0
            for j in range(minutes):
                if grumpy[i + j] == 1:
                    curr += customers[i + j]
            maxx = max(maxx, curr)
        
        return maxx + satisfied