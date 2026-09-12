class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r, c):
            grid[r][c] = 0
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r==0 or r==rows-1 or c==cols-1 or c==0):
                    dfs(r,c)

        return sum(row.count(1) for row in grid)