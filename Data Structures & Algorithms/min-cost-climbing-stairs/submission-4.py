class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        
        h0 = cost[0]
        h1 = cost[1]
        for i in range(2, len(cost)):
            temp = h1
            h1 = min(h1, h0) + cost[i]
            h0 = temp
        
        return min(h0, h1)
