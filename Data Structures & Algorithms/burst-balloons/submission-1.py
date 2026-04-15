class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        self.res = 0
        dp = defaultdict(int)

        # def backtrack(ttl, nums):
        #     if len(nums) < 3:
        #         self.res = max(self.res, ttl)
        #         return 
            
        #     for i in range(1, len(nums)-1):
        #         backtrack(ttl + (nums[i-1] * nums[i] * nums[i+1]), nums[:i] + nums[i+1:])
            
        # backtrack(0, nums)
        # return self.res

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l,r)]
            
            for i in range(l, r+1):
                gain = nums[l-1] * nums[i] * nums[r+1]
                gain += dfs(l, i-1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], gain)
            
            return dp[(l,r)]
        return dfs(1, len(nums)-2)
        
            

