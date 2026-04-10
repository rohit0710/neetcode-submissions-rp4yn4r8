class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        h0, h1 = 0, 0
        for i in range(len(nums)):
            temp = h1
            h1 = max(h1, h0 + nums[i])
            h0 = temp

        return h1