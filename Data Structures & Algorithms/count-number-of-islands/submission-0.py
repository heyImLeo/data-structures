class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visit = set()
        island = 0

        def dfs(r,c):
            row_in = 0<=r<rows
            col_in = 0<=c<cols

            if not row_in or not col_in or (r,c) in visit or grid[r][c] == "0":
                return False
            
            visit.add((r,c))
            for u,v in directions:
                dfs(u+r, v+c)
            
            return True
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    island+=1
        
        return island