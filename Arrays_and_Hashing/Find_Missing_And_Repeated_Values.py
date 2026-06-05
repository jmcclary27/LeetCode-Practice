class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        a, b = None, None

        seen = set()
        for row in range(n):
            for col in range(n):
                if grid[row][col] not in seen:
                    seen.add(grid[row][col])
                else:
                    a = grid[row][col]
        
        for i in range(1, (n ** 2) + 1):
            if i not in seen:
                b = i
                break
        
        return [a, b]