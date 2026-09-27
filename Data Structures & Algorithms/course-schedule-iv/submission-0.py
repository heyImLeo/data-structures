class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        pre = [set() for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        
        queue = deque([x for x in range(numCourses) if indegree[x] == 0 ])

        while queue:
            node = queue.popleft()

            for n in graph[node]:
                pre[n].add(node)
                pre[n].update(pre[node])
                indegree[n]-=1
                if indegree[n] == 0:
                    queue.append(n)

        return [u in pre[v] for u, v in queries]