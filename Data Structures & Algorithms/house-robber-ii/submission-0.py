class Solution:
    def rob(self, house: List[int]) -> int:
        if len(house) == 1:
            return house[0]

        if len(house) == 2:
            return max(house)

        def rob_simple(nums):
            dp = [0 for i in range(len(nums))]
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]

        return max(rob_simple(house[1:]), rob_simple(house[:-1]))