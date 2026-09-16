class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] <= interval[0]:
                ans.append(interval)
        return len(intervals) - len(ans)