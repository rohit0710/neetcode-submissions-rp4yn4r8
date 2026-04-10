class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        min_v = nums[0]
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < min_v:
                min_v =  nums[mid]

            if nums[mid] <= nums[j]:
                j = mid- 1
            else:
                i = mid + 1

        return min_v