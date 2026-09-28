class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def _path(r, c):
            if r == n-1 and c == m-1:
                return 1
            
            if not 0<=r<n or not 0<=c<m:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]
            
            down = _path(r+1, c)
            right = _path(r, c+1)
            memo[(r,c)] = down + right
            return memo[(r,c)]

        return _path(0, 0)