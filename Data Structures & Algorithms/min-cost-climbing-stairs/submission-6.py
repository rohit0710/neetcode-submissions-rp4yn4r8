class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) == 1:
            return cost[0]
        
        if len(cost) == 2:
            return min(cost)

        h0, h1 = cost[0], cost[1]

        for c in cost[2:]:
            temp = h1
            h1 = min(h0, h1) + c
            h0 = temp

        return min(h1, h0)