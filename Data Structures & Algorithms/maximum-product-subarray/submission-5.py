class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxv = minv = res = nums[0]

        for n in nums[1:]:
            temp = max(n, maxv * n, minv * n)
            minv = min(n, maxv * n, minv * n)
            maxv = temp
            res = max(res, maxv)
        
        return res