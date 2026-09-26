class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        topo = []

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            node = queue.popleft()
            topo.append(node)

            for new_node in graph[node]:
                indegree[new_node] -= 1
                if indegree[new_node] == 0:
                    queue.append(new_node)
            
        return False if len(topo) != numCourses else True