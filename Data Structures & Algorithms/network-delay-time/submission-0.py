class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))
        
        minHeap = [(0, k)] # [(weight, src)]
        minTimes = {}
        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if node in minTimes:
                continue
            
            minTimes[node] = weight
            for new_node, new_weight in graph[node]:
                if new_node not in minTimes:
                    heapq.heappush(minHeap, (new_weight+weight, new_node))
        
        if len(minTimes) != n:
            return -1
        
        return max(minTimes.values())
