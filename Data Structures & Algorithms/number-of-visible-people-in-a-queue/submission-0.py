class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []

        for index, val in enumerate(heights):
            while stack and heights[stack[-1]] <= val:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(index)
        return res