class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        queue = deque()

        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            if not in_bounds(r, c):
                return
            
            if grid[r][c] != 1 or (r, c) in visited:
                return

            visited.add((r, c))
            queue.append((r, c, 0))
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                dfs(nr, nc)
        
        Found = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    Found = True
            
            if Found:
                break
        
        while queue:
            row, col, distance = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr+row, dc+col

                if not in_bounds(nr, nc):
                    continue
                
                if (nr, nc) in visited:
                    continue
                
                if grid[nr][nc] == 1:
                    return distance
                
                queue.append((nr, nc, distance+1))
                visited.add((nr, nc))
        
        

                    
