class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union_size(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False
        
        if self.size[x_root] >= self.size[y_root]:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        else:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u, v in edges:
            if not dsu.union_size(u, v):
                return [u,v]
        

        