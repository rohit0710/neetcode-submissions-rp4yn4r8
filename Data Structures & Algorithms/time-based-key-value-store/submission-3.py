from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map[key]
        if not vals:
            return ""
        ind = bisect_left(vals, timestamp, key=lambda x:x[0])
        if ind >= len(vals) or vals[ind][0] > timestamp:
            ind -= 1
        if ind < 0:
            return ""
        return vals[ind][-1]
