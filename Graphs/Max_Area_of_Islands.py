class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        # List of possible ways to move through the grid
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


        def BFS(r, c):
            '''Iterative BFS function to find every piece of the island'''
            q = [[r, c]]
            grid[r][c] = 0
            pieces = 1
            # Loops until the queue is empty
            while q:
                node = q.pop(0)
                row, col = node[0], node[1]
                # Finds every possible direction of movement
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    # Checks if it is a value island piece
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1:
                        # Adds it to the queue and changes its value to 0 so we don't find the same piece
                        q.append([nr, nc])
                        grid[nr][nc] = 0
                        pieces += 1
            # Returns the number of pieces in the island
            return pieces

        # Loops through every square, applying BFS to potential islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(BFS(r, c), res)
        # Returns the max area
        return res