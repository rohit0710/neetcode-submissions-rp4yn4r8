class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_val = defaultdict()
        self.key_freq = defaultdict()
        self.freq_key = defaultdict(OrderedDict)
        self.minf = 0

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
        oldfreq = self.key_freq[key]
        self.key_freq[key] += 1
        del self.freq_key[oldfreq][key]
        if not self.freq_key[oldfreq]:
            del self.freq_key[oldfreq]
        self.freq_key[oldfreq+1][key] = 1
        if self.minf not in self.freq_key:
            self.minf += 1
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        if key in self.key_val:
            self.get(key)
            self.key_val[key] = value
            return

        if len(self.key_val) == self.capacity:
            del_k, del_v = self.freq_key[self.minf].popitem(last=False)
            del self.key_freq[del_k]
            del self.key_val[del_k]

        self.key_val[key] = value
        self.key_freq[key] = 1
        self.freq_key[1][key] = 1
        self.minf = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)