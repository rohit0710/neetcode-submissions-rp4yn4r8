class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        maxv=minv = nums[0]
        res = maxv
        
        for n in nums[1:]:
            temp = max(n, maxv * n, minv*n)
            minv = min(n, maxv * n, minv*n)
            maxv = temp
            res = max(res, maxv)
        
        return res

