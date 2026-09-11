class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        maxTimes = {}
        maxHeap = [(1, start_node)]

        while maxHeap:
            prob, node = heapq.heappop_max(maxHeap)

            if node == end_node:
                return prob
            
            if node in maxTimes:
                continue
            maxTimes[node] = prob

            for new_node, new_prob in graph[node]:
                probability = new_prob*prob
                heapq.heappush_max(maxHeap, (probability, new_node))
        return 0
