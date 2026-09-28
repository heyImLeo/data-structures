class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(grid), len(grid[0])
        def _path(r, c):
            if not 0<=r<rows or not 0<=c<cols:
                return float("inf")
            
            if r == rows-1 and c == cols-1:
                return grid[r][c]
            
            if (r,c) in memo:
                return memo[(r,c)]

            down = grid[r][c] + _path(r+1, c)
            right = grid[r][c] + _path(r, c+1)
            memo[(r,c)] = min(down, right)
            return memo[(r,c)]
        
        return _path(0, 0)