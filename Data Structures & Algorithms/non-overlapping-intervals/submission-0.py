class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count = 0
        end = intervals[0][-1]
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                end = intervals[i][-1]
            else:
                count += 1
                end = min(end, intervals[i][-1])
        return count