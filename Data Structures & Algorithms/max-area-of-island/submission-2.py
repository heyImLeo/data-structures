class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        max_size = 0

        def dfs(r, c):
            cur_size = 1
            grid[r][c] = 0

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]:
                    cur_size+=dfs(nr, nc)
                    
            return cur_size
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    max_size = max(max_size, dfs(r, c))
        
        return max_size