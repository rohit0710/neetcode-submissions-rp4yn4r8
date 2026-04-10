class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]

        if len(cost) == 2:
            return min(cost)

        h0, h1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            temp = h1
            h1 = min(h1, h0) +cost[i]
            h0 = temp
        
        return min(h1, h0)
        # dp = [0 for i in range(len(cost) + 1)]
        # for i in range(2, len(dp)):
        #     dp[i] = min(cost[i-2] + dp[i-2], dp[i-1]+ cost[i-1])

        # return dp[-1]