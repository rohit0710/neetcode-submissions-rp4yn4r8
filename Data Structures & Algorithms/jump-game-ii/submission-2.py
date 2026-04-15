class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        res = 0
        cur_far = 0
        for i in range(len(nums)-1):
            furthest = max(furthest, i+ nums[i])

            if cur_far == i:
                res += 1
                cur_far = furthest

        return res
