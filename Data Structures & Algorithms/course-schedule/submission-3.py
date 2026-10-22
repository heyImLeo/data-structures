class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        res = 0

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])

        while queue:
            node = queue.popleft()
            res += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return res == numCourses