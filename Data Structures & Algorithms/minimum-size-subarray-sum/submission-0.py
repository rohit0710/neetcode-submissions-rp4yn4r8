class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        ans = float('inf')
        s = 0
        for j in range(len(nums)):
            s += nums[j]

            while s >= target:
                ans = min(ans, j - i + 1)
                s -= nums[i]
                i += 1
        return ans if ans != float('inf') else 0