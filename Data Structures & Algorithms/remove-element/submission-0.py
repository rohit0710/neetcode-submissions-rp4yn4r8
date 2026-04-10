class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p0 = 0
        p = 0
        while p < len(nums):
            if nums[p] != val:
                nums[p], nums[p0] = nums[p0], nums[p]
                p0 += 1
            p += 1
        return p0