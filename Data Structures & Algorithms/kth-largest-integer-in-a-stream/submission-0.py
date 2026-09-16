class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for x in nums:
            self.addToHeap(x)

    def addToHeap(self, val: int):
        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        self.addToHeap(val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)