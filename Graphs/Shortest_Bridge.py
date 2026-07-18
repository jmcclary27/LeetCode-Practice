class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def markIsland(row, col):
            island = set()
            q = deque([(row, col)])
            island.add((row, col))

            while q:
                r, c = q.popleft()

                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                        and (nr, nc) not in island
                    ):
                        island.add((nr, nc))
                        q.append((nr, nc))

            return island

        def BFS(island):
            visited = set(island)
            q = deque()

            # Every point on the first island is a starting point
            for row, col in island:
                q.append((row, col, 0))

            while q:
                r, c, counter = q.popleft()

                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and (nr, nc) not in visited
                    ):
                        # Found second island
                        if grid[nr][nc] == 1:
                            return counter

                        # Mark visited WHEN adding to queue
                        visited.add((nr, nc))
                        q.append((nr, nc, counter + 1))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    island = markIsland(row, col)
                    return BFS(island)