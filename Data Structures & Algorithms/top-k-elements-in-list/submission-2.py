class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)
        freq = [[] for i in range(max(count.values()))]
        for n, f in count.items():
            freq[f-1].append(n)

        print(freq)
        res = []
        for i in range(len(freq)-1, -1, -1):
            res += freq[i][:min(k, len(freq[i]))]
            k -= len(freq[i])
            if k <= 0 :
                break
        return res
