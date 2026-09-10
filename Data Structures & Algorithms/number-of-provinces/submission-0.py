class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        province = 0

        def dfs(city):
            visit.add(city)
            for index, connected in enumerate(isConnected[city]):
                if connected and index not in visit:
                    dfs(index)
        
        for i in range(len(isConnected)):
            if i not in visit:
                dfs(i)
                province+=1
        
        return province