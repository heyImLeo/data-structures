class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [(height, index)]
        res = 0
        n = len(heights)

        for index, h in enumerate(heights):
            start = index
            while stack and stack[-1][0] > h:
                val, i = stack.pop()
                area = val * (index - i)
                res = max(res, area)
                start = i
            stack.append((h, start))
            
        while stack:
            height, index = stack.pop()
            width = n - index
            area = height * width
            res = max(res, area)
        return res