class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        visiting = set()
        graph = defaultdict(list)
        res = []

        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(node):
            if node in visited:
                return True
            
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res