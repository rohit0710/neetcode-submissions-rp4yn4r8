class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums)-1
        p = 0
        while p <= p2:
            if nums[p] == 0:
                nums[p], nums[p0] = nums[p0], nums[p]
                p0+= 1
                p += 1
            elif nums[p] == 2:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            else:
                p += 1