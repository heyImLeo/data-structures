class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        queue = deque([(r,c,1) for r in range(rows) for c in range(cols) if grid[r][c] == 0])
        INF = 2147483647

        while queue:
            row, col, val = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr+row, dc+col

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == INF:
                    grid[nr][nc] = val
                    queue.append((nr, nc, val+1))


