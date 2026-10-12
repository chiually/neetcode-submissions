class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] != 'O':
                return

            board[i][j] = 'T'

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        # go through borders of board
        for r in range(ROWS):
            # if O is on boarder that region is unsurroundable
            if board[r][0] == 'O':
                # use dfs to mark unsurroundable region
                dfs(r, 0)
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1)
                
        for c in range(1, COLS - 1):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        