class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            board[r][c] = 'T'
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == 'O':
                    dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r == rows-1 or c == 0 or c == cols-1):
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'