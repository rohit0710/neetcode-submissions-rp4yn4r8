class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl = sum(nums)
        if ttl % 2 != 0:
            return False
        
        target = ttl // 2
        n = len(nums)

        memo = [[False for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n+1):
            memo[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target + 1):
                if nums[i-1] <= j:
                    memo[i][j] = memo[i-1][j] or memo[i-1][j - nums[i-1]]
                else:
                    memo[i][j] = memo[i-1][j]
        return memo[-1][-1]