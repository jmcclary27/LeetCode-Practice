class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                curr = [max(triplets[i][0], curr[0]), max(triplets[i][1], curr[1]), max(triplets[i][2], curr[2])]
            
        return True if curr == target else False