class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl = sum(nums)
        if ttl % 2 != 0:
            return False
        
        ttl = ttl // 2

        dp = [[False] * (ttl + 1) for _ in range(len(nums)+1)]
        dp[0][0] = True

        for i in range(len(nums)+1):
            dp[i][0] = True

        for i in range(1, len(nums)+1):
            for j in range(1, ttl+1):
                dp[i][j] = dp[i-1][j]
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
        
        return dp[-1][-1]