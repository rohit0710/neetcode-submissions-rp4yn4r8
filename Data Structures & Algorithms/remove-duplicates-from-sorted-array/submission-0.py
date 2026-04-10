class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        for j in range(len(nums)):
            if nums[i-1] != nums[j]:
                nums[i], nums[j] = nums[j],nums[i]
                i+= 1
        return i
