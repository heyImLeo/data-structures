class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        minHeap = [(0, 0, 0)] # [(effort, row, col)]
        minTimes = {}

        while minHeap:
            effort, row, col = heapq.heappop(minHeap)

            if (row, col) == (rows-1, cols-1):
                return effort

            if (row, col) in minTimes:
                continue
            minTimes[(row, col)] = effort

            for dr, dc in directions:
                nr, nc = dr+row, dc+col
                if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in minTimes:
                    effortAbs = abs(heights[nr][nc] - heights[row][col])
                    heapq.heappush(minHeap, (max(effortAbs, effort), nr, nc))
        
        return None