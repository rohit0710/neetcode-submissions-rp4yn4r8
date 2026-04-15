class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def backtrack(i, total):
            if i == len(nums):
                return total == target

            add = backtrack(i+1, total+nums[i])
            minus = backtrack(i+1, total-nums[i])

            return add + minus
        return backtrack(0, 0)