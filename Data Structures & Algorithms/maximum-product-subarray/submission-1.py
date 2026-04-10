class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_v, max_v = nums[0],nums[0]
        res = max_v
        for v in nums[1:]:
            temp = min(v, min_v*v, max_v*v)
            max_v = max(v, min_v*v, max_v*v)
            min_v = temp
            res = max(res, max_v)
        return res