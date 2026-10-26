class Solution:
    from collections import deque
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(a, b):
            q = deque([(a, b)])
            visited.add((a, b))
            islandSum = grid[a][b]
            while q:
                row, col = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] > 0 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        islandSum += grid[nr][nc]
            if islandSum % k == 0:
                return True
            return False
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] > 0 and (row, col) not in visited:
                    if bfs(row, col):
                        res += 1
        return res