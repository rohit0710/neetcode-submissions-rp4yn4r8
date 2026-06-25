class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mv, nv = nums[0], nums[0]
        res = mv

        for n in nums[1:]:
            temp = max(n, mv * n, nv * n)
            nv = min(n, nv * n, mv * n)
            mv = temp

            res = max(res, mv)
        
        return res