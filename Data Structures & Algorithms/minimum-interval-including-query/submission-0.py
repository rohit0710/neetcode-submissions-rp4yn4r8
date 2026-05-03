from _heapq import heappop, heappush
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = dict()
        i = 0 
        n = len(intervals)
        heap = []
        for q in sorted(queries):
            while i < n and intervals[i][0] <= q:
                heappush(heap, (intervals[i][1] - intervals[i][0]+1, intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < q:
                heappop(heap)
            
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]