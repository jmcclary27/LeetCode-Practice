class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0
        prevHeights = []

        for r in range(ROWS):
            heights = []
            for c in prevHeights:
                if matrix[r][c]:
                    matrix[r][c] += matrix[r - 1][c]
                    heights.append(c)

            for c in range(COLS):
                if matrix[r][c] == 1:
                    heights.append(c)

            for i, c in enumerate(heights):
                res = max(res, (i + 1) * matrix[r][c])

            prevHeights = heights

        return res