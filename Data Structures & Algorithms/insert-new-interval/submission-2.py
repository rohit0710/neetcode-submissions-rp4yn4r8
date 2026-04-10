class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        new_st, new_end = new_interval
        res = []
        for i, (start, end) in enumerate(intervals):
            if new_st > end:
                res.append([start, end])
            elif new_end < start:
                res.append([new_st, new_end])
                return res + intervals[i:]
            else:
                new_st = min(new_st, start)
                new_end = max(new_end, end)
        
        res.append([new_st, new_end])
        return res