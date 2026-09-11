from heapq import heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        
        minTimes = {} # [(r,c): cost]
        minHeap = [(grid[0][0], 0, 0)] # [(cost, r, c)]

        while minHeap:
            cost, r, c = heappop(minHeap)

            if not 0<=r<rows or not 0<=c<cols or (r, c) in minTimes:
                continue
            
            minTimes[(r, c)] = cost

            if r == rows-1 and c == cols-1:
                return max(minTimes.values())

            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in minTimes:
                    heappush(minHeap, (grid[nr][nc], nr, nc))
        
        return -1
            
            