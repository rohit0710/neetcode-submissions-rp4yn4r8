class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def simple(lis):
            h0, h1 = 0, 0
            for n in lis:
                temp = h1
                h1 = max(h1, h0 + n)
                h0 = temp
            
            return h1
        
        return max(simple(nums[1:]), simple(nums[:-1])) 