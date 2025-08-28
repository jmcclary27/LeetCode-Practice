class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # List of possible ways to move in the grid
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        # Breadth first search function
        def bfs(r, c):
            # Creates a queue
            q = [[r, c]]
            # Loops until the queue is empty
            while q:
                # Dequeues the first element and changes it to "0" in the grid
                node = q.pop(0)
                row, col = node[0], node[1]
                grid[row][col] = "0"
                # Loops through the directions with rows and columns
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Checks if our new direction is in the grid and if its value is "1"
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == "1":
                        q.append([nr, nc])
        
        # Loops through the grid
        for r in range(rows):
            for c in range(cols):
                # Enactes BFS and updates the counter if the current value is "1"
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands