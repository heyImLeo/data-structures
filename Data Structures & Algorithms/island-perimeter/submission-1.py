class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visit = set()
        peri = 0
        queue = deque([])
        flag = False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    queue.append((r,c))
                    visit.add((r,c))
                    flag = True
                    break
            
            if flag:
                break
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and (nr, nc) not in visit:
                    queue.append((nr, nc))
                    visit.add((nr, nc))
                elif not 0<=nr<rows or not 0<=nc<cols or not grid[nr][nc]:
                    peri+=1
        
        return peri