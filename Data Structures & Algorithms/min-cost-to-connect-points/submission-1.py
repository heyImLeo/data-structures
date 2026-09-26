class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False]*n
        minHeap = [(0 , 0)] # [(weight, node)]
        total = 0

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            if visited[node]:
                continue
            
            visited[node] = True
            total+=dist

            for v in range(n):
                if not visited[v]:
                    new_dist = abs(points[node][0] - points[v][0]) + abs(points[node][1] - points[v][1])
                    heapq.heappush(minHeap, (new_dist, v))
        
        return total