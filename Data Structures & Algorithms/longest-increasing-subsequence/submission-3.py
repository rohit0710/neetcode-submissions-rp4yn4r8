from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        for n in nums:
            ind = bisect_left(res, n)
            if ind == len(res):
                res.append(n)
            else:
                res[ind] = n
        
        return len(res)
