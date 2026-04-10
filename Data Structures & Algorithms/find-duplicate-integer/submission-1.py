class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            idx =abs(num) -1
            if nums[idx-1] < 0:
                return abs(num)
            nums[idx-1] *= -1
        return -1 
        
    