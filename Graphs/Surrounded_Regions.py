class Solution:
    def solve(self, board: List[List[str]]) -> None:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])

        def BFS(a, b):
            visited = set()
            visited.add((a, b))
            q = [(a, b)]
            while q:
                node = q.pop()
                for dirs in DIRECTIONS:
                    nr, nc = node[0] + dirs[0], node[1] + dirs[1]
                    newNode = (nr, nc)
                    if board[nr][nc] == "O" and newNode not in visited:
                        if nr > 0 and nc > 0 and nr < ROWS - 1 and nc < COLS - 1:
                            q.append(newNode)
                            visited.add(node)
                        else:
                            return
            for vis in visited:
                board[vis[0]][vis[1]] = "X"


        for i in range(1, ROWS - 1):
            for j in range(1, COLS - 1):
                if board[i][j] == "O":
                    BFS(i, j)