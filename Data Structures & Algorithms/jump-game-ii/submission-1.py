class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = 0
        cur_far, farthest = 0, 0
        for i in range(len(nums)-1):
            cur_far = max(cur_far, i + nums[i])
            if i == farthest:
                res += 1
                farthest = cur_far
        return res