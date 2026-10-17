class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                _, ind = stack.pop()
                res[ind] = index - ind
            stack.append((val, index))
        
        return res