class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i - 1]:
                l,r= i+1, len(nums)-1
                while l < r:
                    if 0 == (nums[i] + nums[l] + nums[r]):
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l +1]:
                            l += 1
                        while l < r and nums[r] == nums[r -1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif 0 < (nums[i] + nums[l] + nums[r]):
                        r -= 1
                    else:
                        l += 1

        return res
