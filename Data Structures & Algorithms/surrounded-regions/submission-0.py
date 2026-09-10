class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for u, v in directions:
                nr, nc = r+u, v+c
                dfs(nr, nc)
        
        for r in range(rows):
            dfs(r, 0)
        for r in range(rows):
            dfs(r, cols-1)
        for c in range(cols):
            dfs(0, c)
        for c in range(cols):
            dfs(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        