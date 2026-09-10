class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        queue = deque()

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            queue.append((r, c, 0))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        found = False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break
        
        while queue:
            r, c, distance = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if (nr, nc) in visited:
                    continue

                if grid[nr][nc] == 1:
                    return distance

                visited.add((nr, nc))
                queue.append((nr, nc, distance + 1))

        return -1

                    
