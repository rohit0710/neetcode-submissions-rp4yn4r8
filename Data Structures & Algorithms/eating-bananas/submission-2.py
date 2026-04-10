class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        if sum(piles) <= h:
            return 1
        res = 0
        minb, maxb = 1, max(piles)
        while minb <= maxb:
            k = (minb + maxb) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/k)
            if time <= h:
                res = k
                maxb = k - 1
            else:
                minb = k + 1

        return res