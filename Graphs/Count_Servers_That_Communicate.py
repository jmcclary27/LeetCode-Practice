class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            row_sum = sum(grid[r])
            if row_sum <= 1:
                continue
            res += row_sum
            for c in range(COLS):
                if grid[r][c]:
                    grid[r][c] = -1

        for c in range(COLS):
            col_sum = unmarked = 0
            for r in range(ROWS):
                col_sum += abs(grid[r][c])
                if grid[r][c] > 0:
                    unmarked += 1
                elif grid[r][c] < 0:
                    grid[r][c] = 1
            if col_sum >= 2:
                res += unmarked

        return res