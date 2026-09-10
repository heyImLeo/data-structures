class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        maxIsland = 0

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or not grid[r][c]:
                return 0
            
            grid[r][c] = 0

            total = 1
            for u, v in directions:
                total += dfs(r+u, c+v)
            
            return total
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    curMax = dfs(r,c)
                    maxIsland = max(maxIsland, curMax)
        
        return maxIsland

        