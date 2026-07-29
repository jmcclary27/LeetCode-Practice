class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        min_row = []
        max_col = []
        result = []

        for i in range(m):
            row = []
            for j in range(n):
                row.append(matrix[i][j])
            min_row.append(min(row))

        for i in range(n):
            col = []
            for j in range(m):
                col.append(matrix[j][i])
            max_col.append(max(col))
            
        for i in min_row:
            if i in max_col:
                result.append(i)

        return result