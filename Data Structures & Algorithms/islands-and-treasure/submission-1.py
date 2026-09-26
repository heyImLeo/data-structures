class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        queue = deque([(r,c,0) for r in range(rows) for c in range(cols) if grid[r][c] == 0])
        INF = 2147483647
        visit = set()

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] != -1 and (nr, nc) not in visit:
                    if grid[nr][nc] == INF:
                        grid[nr][nc] = dist+1
                    visit.add((nr,nc))
                    queue.append((nr, nc, dist+1))
        