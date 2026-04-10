class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = min(trips, key = lambda x: x[1])[1]
        last = max(trips, key = lambda x: x[2])[2]
        days = last - start + 1
        cur_pass = [0] * (days+1)
        print(start, last)
        for pas, up, off in trips:
            cur_pass[up-start] += pas
            cur_pass[off - start] -= pas
        count = 0
        for pas in cur_pass:
            count += pas
            if count > capacity:
                return False
        return True