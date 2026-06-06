class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [-1] * n
        counter = n
        minn = None

        for i in range(n - 1, -1, -1):
            if not minn or heights[i] > minn:
                counter -= 1
                res[counter] = i
                minn = heights[i]
            
        return res[counter:]