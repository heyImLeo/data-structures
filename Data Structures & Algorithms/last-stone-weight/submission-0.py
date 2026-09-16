class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        while len(maxHeap) > 1:
            a = heapq.heappop_max(maxHeap)
            b = heapq.heappop_max(maxHeap)
            if a != b:
                if b > a:
                    b, a = a, b
                heapq.heappush_max(maxHeap, a - b)
        
        if maxHeap:
            return maxHeap[0]

        return 0