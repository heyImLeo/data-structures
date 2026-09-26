class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visit, visiting = set(), set()
        res = []
        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(node):
            if node in visiting:
                return False
            
            if node in visit:
                return True
            
            visiting.add(node)
            for new_node in graph[node]:
                if not dfs(new_node):
                    return False
            
            visiting.remove(node)
            visit.add(node)
            res.append(node)
            return True
        
        for node in range(numCourses):
            if node not in visit:
                if not dfs(node):
                    return []
        
        return res
            
        
