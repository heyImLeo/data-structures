class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visit = set()

        def dfs(r, c, peri):
            row_in = 0<=r<rows
            col_in = 0<=c<cols
            if not row_in or not col_in or grid[r][c] == 0:
                return 1
            
            if (r,c) in visit:
                return 0
            
            visit.add((r,c))
            peri = 0
            for u, v in directions: 
                peri += dfs(u+r, v+c, peri)
            return peri

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r,c, 0)