class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)

        for i, n in enumerate(nums):
            if n <= 0 or n > l:
                nums[i] = l + 1

        for i,n in enumerate(nums):
            if abs(n) != (l+1):
                print(i, n, abs(nums[n-1]))
                nums[abs(n)-1] = -abs(nums[abs(n)-1])

        for i,n in enumerate(nums):
            if n > 0:
                return i + 1
        return l+1