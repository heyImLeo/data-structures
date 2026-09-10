class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        atlantic = set()
        pacific = set()

        def dfs(r, c, visit):
            visit.add((r,c))
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visit:
                    dfs(nr, nc, visit)
        
        for r in range(rows):
            dfs(r, 0, pacific)
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
        for c in range(cols):
            dfs(rows-1, c, atlantic)
        
        return list(pacific & atlantic)
