class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1),(-1,1),(1,-1),(-1,-1),(1,1)]
        visit = set((0,0))

        if grid[0][0]:
            return -1
        
        queue = deque([(0,0,1)])

        while queue:
            row, col, val = queue.popleft()

            if (row, col) == (rows-1, cols-1):
                return val
            
            for dr, dc in directions:
                nr, nc = dr+row, dc+col
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 0 and (nr, nc) not in visit:
                    visit.add((nr,nc))
                    queue.append((nr,nc,val+1))
            
        return -1