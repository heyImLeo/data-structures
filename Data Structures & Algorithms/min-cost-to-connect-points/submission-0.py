class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minTimes = {}
        minHeap = [(0 , 0)] # [(weight, node)]
        total = 0

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            if node in minTimes:
                continue
            
            minTimes[node] = dist
            total+=dist

            for v in range(n):
                if v not in minTimes:
                    new_dist = abs(points[node][0] - points[v][0]) + abs(points[node][1] - points[v][1])
                    heapq.heappush(minHeap, (new_dist, v))
        
        return total