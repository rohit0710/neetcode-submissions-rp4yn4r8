class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)

        freq = [[] for _ in range(len(nums))]

        for v, f in count.items():
            freq[f-1].append(v)

        res = []
        for i in range(len(freq)-1, -1, -1):
            if freq[i]:
                res += freq[i][:min(k, len(freq[i]))]
                k -= len(freq[i])
                if k <= 0:
                    break
        return (res)