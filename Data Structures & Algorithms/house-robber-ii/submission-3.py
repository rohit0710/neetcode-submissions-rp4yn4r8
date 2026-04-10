class Solution:
    def rob(self, house: List[int]) -> int:
        if len(house) == 1:
            return house[0]

        if len(house) == 2:
            return max(house)

        def rob_simple(nums):
            h0, h1 = 0, 0
            for i in range(len(nums)):
                temp = h1
                h1 = max(h1, h0 + nums[i])
                h0 = temp
            return h1
            
        return max(rob_simple(house[1:]), rob_simple(house[:-1]))