class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_sum = [sum(row) for row in grid]
        col_sum = [sum(col) for col in zip(*grid)]

        ans = 0
        for r in range(len(row_sum)):
            for c in range(len(col_sum)):
                 if grid[r][c] == 1 and (row_sum[r] > 1 or col_sum[c] > 1):
                    ans += 1

        return ans