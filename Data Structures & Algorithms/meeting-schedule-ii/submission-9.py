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
        intervals.sort(key= lambda x:x.start)

        heap = [intervals[0].end]

        for i, interval in enumerate(intervals[1:], start=1):
            if heap[0] <= interval.start:
                heapq.heappush(heap, max(heapq.heappop(heap), interval.end))
            else:
                heapq.heappush(heap, interval.end)

        return len(heap)