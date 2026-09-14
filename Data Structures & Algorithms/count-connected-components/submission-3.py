class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        class DSU: 
            def __init__(self, n):
                self.size = [1] * n
                self.parent = list(range(n))
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union_size(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)

                if root_x == root_y:
                    return
                
                if self.size[root_x] > self.size[root_y]:
                    self.parent[root_y] = root_x
                    self.size[root_x] += self.size[root_y]
                else:
                    self.parent[root_x] = root_y
                    self.size[root_y] += self.size[root_x]
                
                return True
        
        dsu = DSU(n)
        for edge in edges:
            dsu.union_size(*edge)
        
        return len(set(dsu.find(i) for i in range(n)))