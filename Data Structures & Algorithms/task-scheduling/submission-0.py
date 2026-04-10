class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # freq = [0] * 26
        # for task in tasks:
        #     freq[ord(task) - ord("A")] += 1

        count = Counter(tasks)
        freq, cycles = defaultdict(list), []
        for v, f in count.items():
            freq[f].append(v)

        max_f = max(freq.keys())
        idle = (max_f - 1) * n
        count.pop(freq[max_f][0])
        for c,v in count.items():
            idle -= min((max_f - 1), v)
        return len(tasks) + max(0, idle)