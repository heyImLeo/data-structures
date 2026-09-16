class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def calcEuclidean(x, y):
            return (x**2 + y**2)
        
        minHeap = []
        ans = []

        for x, y in points:
            heapq.heappush(minHeap, (calcEuclidean(x, y), x, y))
        
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            ans.append([x, y])
        
        return ans