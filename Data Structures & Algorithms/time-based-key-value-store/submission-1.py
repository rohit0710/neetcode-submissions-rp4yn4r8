class Info:
    def __init__(self, val='', timestamp=float('-inf')):
        self.val = val
        self.timestamp = timestamp

class TimeMap:

    def __init__(self):
        self.key_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value[key].append(Info(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.key_value[key]
        if not values:
            return ""
        i,j = 0, len(values)-1
        res = ""
        while i <= j:
            mid = (i+j) // 2
            if values[mid].timestamp <= timestamp:
                res = values[mid].val
                i = mid +1
            else:
                j= mid -1

        return res