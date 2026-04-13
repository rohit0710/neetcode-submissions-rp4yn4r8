class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        h0, h1 = 0, 0
        for n in nums:
            temp = h1
            h1 = max(h1, h0+n)
            h0 = temp
        
        return h1