class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()
        for i,v in enumerate(nums):
            if (target - v) in diff:
                return [diff[target - v], i]
            else:
                diff[v] = i
        return []