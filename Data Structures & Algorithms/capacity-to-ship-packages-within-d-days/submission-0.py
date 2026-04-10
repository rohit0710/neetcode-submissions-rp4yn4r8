class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) == days:
            return max(weights)
        if days == 1:
            return sum(weights)
        
        def canShip(cap):
            cur_cap = cap
            ships = 1
            for w in weights:
                if cur_cap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    cur_cap = cap
                cur_cap -= w
            return True
        
        l, r = max(weights), sum(weights)
        res = 0
        while l <= r:
            cap = (l+r)//2
            if canShip(cap):
                res = cap
                r = cap - 1
            else:
                l = cap + 1
        return res