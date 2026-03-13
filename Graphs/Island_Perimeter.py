class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def BFS(a, b):
            q = deque([(a, b)])
            visited.add((a,b))
            counter = 0

            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0:
                        counter += 1
                    elif (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return counter

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return BFS(row, col)

        return 0