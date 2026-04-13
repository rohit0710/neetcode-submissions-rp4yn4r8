from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # memo = [1 for _ in range(len(nums))]

        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] > nums[i]:
        #             memo[i] = max(memo[i], memo[j]+1)

        # return max(memo)

        res = []
        for n in nums:
            ind = bisect_left(res, n)
            if ind == len(res):
                res.append(n)
            else:
                res[ind] = n
        return len(res)