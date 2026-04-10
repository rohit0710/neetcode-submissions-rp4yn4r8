class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        memo = [1 for _ in range(len(nums))]

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    memo[i] = max(memo[i], memo[j]+1)

        return max(memo)