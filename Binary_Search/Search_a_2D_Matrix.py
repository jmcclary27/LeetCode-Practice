class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Creates low and high indexes for both rows and columns
        lowRow, lowCol, highRow, highCol = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        
        # Loops until one of the low indexes is higher than one of the high indexes
        while lowRow <= highRow and lowCol <= highCol:
            # Calculates indexes of the middle row and middle column
            midRow = (lowRow + highRow) // 2
            midCol = (lowCol + highCol) // 2
            # Checks if the target is at our indexes
            if matrix[midRow][midCol] == target:
                return True
            # Checks if the number at our indexes is lower than target
            elif matrix[midRow][midCol] < target:
                # Checks if the last number (largest number) in our row is less than target
                if matrix[midRow][len(matrix[0]) - 1] < target:
                    lowRow = midRow + 1
                # Executes if the last number in our row is greater than target (the target is either in the row or not in the matrix)
                else:
                    lowCol = midCol + 1
            # Executes if the number at our indexes is higher than target
            else:
                # Checks if the first number (smalles number) in our row is less than target
                if matrix[midRow][0] > target:
                    highRow = midRow - 1
                # Executes if the first number in our row is greater than target (target is either in our row or not in the matrix)
                else:
                    highCol = midCol - 1
        # Returns False if our loop condition breaks (target is not in the matrix)
        return False