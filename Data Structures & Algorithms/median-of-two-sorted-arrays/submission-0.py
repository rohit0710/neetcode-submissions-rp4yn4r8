class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        
        nums += nums1[i:] + nums2[j:]

        n = len(nums)
        if n % 2 == 0:
            return (nums[n//2] + nums[(n//2)-1])/2.0
        else:
            return (nums[n//2])