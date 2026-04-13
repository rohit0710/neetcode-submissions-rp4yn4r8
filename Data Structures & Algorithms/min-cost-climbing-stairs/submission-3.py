class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        
        memo = [0 for _ in range(len(cost)+1)]
        # memo[0] = cost[0]
        # memo[1] = cost[1]
        for i in range(2, len(cost)+1):
            memo[i] = min(cost[i-1]+ memo[i-1], cost[i-2] + memo[i-2])
        return memo[-1]