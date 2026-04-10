"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        free = [intervals[0].end]
        heapq.heapify(free)
        for i in range(1, len(intervals)):
            if free[0] <= intervals[i].start:
                heapq.heappushpop(free, intervals[i].end)
            else:
                heapq.heappush(free, intervals[i].end)
        return len(free)
