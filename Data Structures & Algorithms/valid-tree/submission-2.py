class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False
        
        if self.size[rootx] >= self.size[rooty]:
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
        else:
            self.parent[rootx] = rooty
            self.size[rooty] += self.size[rootx]
        
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return False
        
        return True