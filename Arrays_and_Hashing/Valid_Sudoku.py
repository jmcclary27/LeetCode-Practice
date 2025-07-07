class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Creates a list of lists with length 9
        # The lengths are nine for the nine rows, columns, and squares
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        square = [[] for _ in range(9)]
        # Creates a dictionary to help us figure out what square we are in
        square_key = {0 : [0, 1, 2], 1 : [3, 4, 5], 2: [6, 7, 8]}
        
        # Loops through the rows
        for i in range(9):
            # Loops through the columns
            for j in range(9):
                # Skips iteration if not a number
                if board[i][j] == ".":
                    continue
                # Checks if the number is already in the row or columns lists
                if board[i][j] in row[i] or board[i][j] in col[j]:
                    return False
                # Adds the number to proper row and col index
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                # Figures what square we are in
                idx = square_key[i // 3]
                square_idx = idx[j // 3]
                # Checks if the number is in the square
                if board[i][j] in square[square_idx]:
                    return False
                # Adds the number to the square list
                square[square_idx].append(board[i][j])
        # Returns valid sudoku board if False is never flagged
        return True