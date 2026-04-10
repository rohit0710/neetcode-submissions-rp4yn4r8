class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = len(nums)
        for i, n in enumerate(nums):
            if n <= 0 or n > m:
                nums[i] = m + 1

        for i in range(m):
            n = abs(nums[i])
            if n < m+1:
                nums[n-1] = abs(nums[n-1]) * -1
        
        for i in range(m):
            if nums[i] > 0:
                return i + 1
        
        return m+1
