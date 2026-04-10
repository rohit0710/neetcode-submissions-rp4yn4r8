class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0, len(nums)-1
        while i < j:
            if target == (nums[i] + nums[j]):
                return [i+1,j+1]
            if target < (nums[i] + nums[j]):
                j -= 1
            else:
                i += 1
