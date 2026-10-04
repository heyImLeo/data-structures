class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = deque([-1])
        curMax = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            res.appendleft(curMax)
            curMax = max(curMax, arr[i])
        return list(res)
