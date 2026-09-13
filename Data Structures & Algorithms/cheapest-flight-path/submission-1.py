class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float('inf')] * n
        distance[src] = 0

        for _ in range(k+1):
            new_dist = distance[:]
            for u, v, w in flights:
                if distance[u] != float('inf') and distance[u] + w < new_dist[v]:
                    new_dist[v] = w + distance[u]
            distance = new_dist
        
        return distance[dst] if distance[dst] != float('inf') else -1