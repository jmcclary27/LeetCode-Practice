class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        r = c = 0
        dr, dc = 0, 1

        for val in range(n * n):
            mat[r][c] = val + 1
            if mat[(r + dr) % n][(c + dc) % n] != 0:
                dr, dc = dc, -dr
            r, c = r + dr, c + dc

        return mat