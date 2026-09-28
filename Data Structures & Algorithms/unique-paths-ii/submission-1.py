class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        def _path(r, c):
            
            if not 0<=r<row or not 0<=c<col or obstacleGrid[r][c] == 1:
                return 0

            if r == row-1 and c == col-1:
                return 1
                
            if (r,c) in memo:
                return memo[(r,c)]
            
            down = _path(r+1, c)
            right = _path(r, c+1)
            memo[(r,c)] = down + right
            return memo[(r,c)]

        return _path(0, 0)